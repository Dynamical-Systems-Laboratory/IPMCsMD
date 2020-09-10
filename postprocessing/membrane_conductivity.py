# ------------------------------------------------------------------
#
#	Bulk membrane electric conductivity calculations 	
#
# ------------------------------------------------------------------

import sys
py_path = './io_operations/'
sys.path.insert(0, py_path)

import select_d_section as dsec
import post_utils as utils

def compute_average_conductivity(dfile, atom_type, atom_charge, efield, vel_col):
	''' Computes electric conductivity averaged across all	steps in the d file '''

	# dfile - LAMMPS .d file
	# atom_type - atom type ID as defined in .data file
	# atom_charge - atom charge in C
	# efield - strength of the electric field in V/m
	# vel_col - column number for velocity component parallel
	#				to the electric field direction
	#
	# Returns average conductivity in S/m, time steps in fs, and 
	#	a list of conductivities in S/m for each time step

	# Collect all data for this type of atom
	time, data = dsec.extract_atom_type_data(dfile, atom_type)

	# For each time compute average velocity over all atoms
	# convert to m/s
	Afs2ms = 1.0e5
	vel_w_time = []
	natom = len(data[0])
	for step, frame in zip(time, data):
		ave_frame = 0.0
		for line in frame:
			ave_frame += line[vel_col]
		vel_w_time.append(ave_frame/len(frame)*Afs2ms)

	# Average velocity across all time steps
	ave_vel_tot = sum(vel_w_time)/len(vel_w_time) 

	# Average volume at each time step
	# Extract box dimensions, compute volumes at each step in m^3
	cm32m3 = 1.0e-6
	box_dims = dsec.extract_all_sections(dfile, 'ITEM: BOX')
	vols = []
	for box in box_dims:
		flt_box = utils.conv_to_float(box)
		vols.append(utils.compute_volume(flt_box)*cm32m3) 
		
	# Average electric conductivities over time steps
	# and within time steps
	cond_w_time = [vel/vol*natom*atom_charge/efield for vel, vol in zip(vel_w_time, vols)]
	ave_cond = sum(cond_w_time)/len(cond_w_time)

	return ave_cond, time, cond_w_time



