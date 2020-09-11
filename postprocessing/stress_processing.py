# ------------------------------------------------------------------
#
#	Computations related to pressure
#
# ------------------------------------------------------------------

import math 

import sys
py_path = './io_operations/'
sys.path.insert(0, py_path)

import select_d_section as dsec
import post_utils as utils

def compute_spatial_stress(fname, time, nbins, idir, wpos=[], all_steps=False, av_per_atom=False):
	''' Compute spatial distribution of stress '''

	#
	# fname - name of the d file 
	# time - array with simulation times to plot
	# nbins - number of bins in the target direction
	# idir - string representing direction
	# wpos - positions of walls in a non-periodic system
	# all_steps - include all time steps
	# av_per_atom - return average stress per atom rather than total
	#

	# Extract time steps
	time_steps = dsec.extract_all_sections(fname, 'ITEM: TIMESTEP')

	# Extract atom data
	atoms_all_t = dsec.extract_all_sections(fname, 'ITEM: ATOMS')	

	# Extract box dimensions
	box_all_t = dsec.extract_all_sections(fname, 'ITEM: BOX')

	# Direction settings
	# b_ind - index of coordinates in the BOX data
	# d_ind - column with atom positions in that direction in the .d file
	if idir == 'x':
		b_ind = 0
		d_ind = 2 
	elif idir == 'y':
		b_ind = 1
		d_ind = 3
	elif idir == 'z':
		b_ind = 2
		d_ind = 4
	else:
		raise RuntimeError('Wrong direction: ' + idir)
	
	# Stress components
	directions = ['xx', 'yy', 'zz', 'xy', 'xz', 'yz']
	# ..and their position in d file (starts from 0)
	columns = [8, 9, 10, 11, 12, 13]

	stress = []
	for step, atoms, box in zip(time_steps, atoms_all_t, box_all_t):
	
		if (not (int(step[0]) in time)) and (all_steps == False):
			continue
	
		# Spatial bins
		dims = box[b_ind].strip().split()
		if wpos:
			L_0 = wpos[0]
			L_tot = wpos[1] - wpos[0]
		else:
			L_0 = float(dims[0])
			L_tot = float(dims[1]) - L_0
		bin_width = L_tot/nbins
		atoms_in_bins = [0]*nbins

		# Compute volume in A^3
		flt_box = utils.conv_to_float(box)
		# Compute volume in cm^3 then convert to A^3
		cm32A3 = 1.0e24
		vol = utils.compute_volume(flt_box)*cm32A3		
		bin_vol = vol/nbins

		# All stress components
		temp_stress = {}
		for key in directions: 
			temp_stress[key] = [0]*nbins

		# Sum stresses in each bin and each direction	
		for at in atoms:
			at = at.strip().split()
			# So that the binning is simple 
			# Shifted the interval to 0->L_tot
			norm_pos = float(at[d_ind]) - L_0
			ind = max(min(math.floor(norm_pos/bin_width), nbins-1),0)
			atoms_in_bins[ind] += 1
			for key, col in zip(directions, columns):
				temp_stress[key][ind] += float(at[col])

		if av_per_atom:
			# Divide by number of atoms in each bin 
			for key, value in temp_stress.items():
				temp_stress[key] = [x/max(y,1) for x,y in zip(value, atoms_in_bins)]
		else:	
			for key, value in temp_stress.items():
				temp_stress[key] = [x/bin_vol for x in value]
		
		stress.append(temp_stress)
		
	return stress

