# ------------------------------------------------------------------
#
#	Spatial distribution of density compuations
#
# ------------------------------------------------------------------

import math 

import sys
py_path = './io_operations/'
sys.path.insert(0, py_path)

import select_d_section as dsec
import post_utils as utils

def compute_spatial_density(fname, typeID, time, nbins, idir, wpos=[], all_steps=False, den=False):
	''' Compute spatial density distribution of given atom type ''' 

	#
	# fname - name of the d file 
	# typeID - atom type as defined in .data file
	# time - array with simulation times to plot
	# nbins - number of bins in the target direction
	# idir - string representing direction
	# wpos - positions of walls in a non-periodic system 
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
	else:
		b_ind = 2
		d_ind = 4

	densities = []
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
		number_density = [0]*nbins		

		# Calculate how many atoms in each bin	
		atom_data = [] 
		for at in atoms:
			at = at.strip().split()
			if at[1] == str(typeID):
				# So that the binning is simple 
				# Shifted the interval to 0->L_tot
				norm_pos = float(at[d_ind]) - L_0
				number_density[max(min(math.floor(norm_pos/bin_width), nbins-1),0)] += 1
		
		# Compute volume in cm^3 then convert to A^3
		cm32A3 = 1.0e24 
		flt_box = utils.conv_to_float(box)
	
		vol = utils.compute_volume(flt_box)*cm32A3		
		bin_vol = vol/nbins
		
		if den:
			# Divide by bin volumes (all volumes equal)
			densities.append([x/bin_vol for x in number_density])
		else:
			densities.append([x for x in number_density])

	return densities

				


