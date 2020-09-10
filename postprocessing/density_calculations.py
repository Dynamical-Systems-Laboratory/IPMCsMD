#!/usr/local/bin/python3.6

# ------------------------------------------------------------------
#
#	Calculations related to bulk system density 
#
# ------------------------------------------------------------------

import sys
py_path = './io_operations/'
sys.path.insert(0, py_path)

import select_d_section as dsec
import post_utils as utils 

def compute_density_all(data_file, dfile):
	''' Calculate density at all steps in .d file '''
	
	# data_file - LAMMPS .data file 
	# dfile - LAMMPS .d file
	#
	# Returns a list of time steps and a list of corresponding densities
	# time steps are ints, densities are doubles
	#

	# Extract time steps
	time_steps = dsec.extract_all_sections(dfile, 'ITEM: TIMESTEP')

	# Extract box dimensions
	box_dims = dsec.extract_all_sections(dfile, 'ITEM: BOX')

	# Get total system mass in g
	total_mass = utils.compute_total_mass(data_file)

	# Compute densities and convert time steps to ints
	densities = []
	int_steps = []
	for step, box in zip(time_steps, box_dims):

		int_steps.append(int(step[0]))
		
		# Compute volume in cm^3
		flt_box = utils.conv_to_float(box)
		vol = utils.compute_volume(flt_box)

		# Compute and store bulk density in g/cm^3
		densities.append(total_mass/vol)

	return int_steps, densities		


