#!/usr/local/bin/python3.6

# ------------------------------------------------------------------
#
#	Module for extracting data from .d files 				  
#
# ------------------------------------------------------------------ 

def extract_all_sections(dfile, section_name):
	''' Collect data from all .d file sections
			of specified type '''

	# dfile - .d file to extract from
	# section_name - name of the section/ ITEM
	#
	# Best if the name is either full or near full,
	# or at least includes ITEM: NAME - otherwise
	# other sections may be collected too because
	# this function checks for presence in a line 
	# and not equality (due to newlines and extra space)
	#
	# Returns a list of nested lists:
	# [[section_1], ..., [section_N]]
	# with each section consisting of string elements, 
	# each element representing a line of the section
	# as a single string - so section_k is
	# ['line_1', ..., 'line_n']
	# 

	section_data = []
	# Found new section, appending data
	# Assumes next section always begins with
	# ITEM
	flag_append = False
	# If False, the section is last in the 
	# file and needs to be appended separately
	found_item = False
	with open (dfile, 'r') as fin:
		for line in fin:
			if section_name in line:
				found_item = False
				flag_append = True
				# Data for this step
				one_section = []
				# Move to data
				line = next(fin)
			# Collect for this section
			if flag_append:
				if 'ITEM' in line:
					section_data.append(one_section)
					flag_append = False
					found_item = True
				else:
					one_section.append(line)
	# Account delimited with ITEM the last section not 
	if not found_item:
		section_data.append(one_section)
	return section_data

def extract_atom_type_data(dfile, atom_type):
	''' Collects all data of a given atom type and returns the 
			data as floats '''

	# dfile - LAMMPS .d file
	# atom_type - atom type ID as defined in .data file
	#
	# Returns list of times and nested list of atom information:
	# [[[atom_0], [atom_1]], ... , [time step N]]

	# Extract time steps
	time_steps = extract_all_sections(dfile, 'ITEM: TIMESTEP')

	# Extract atom data
	atoms_all_t = extract_all_sections(dfile, 'ITEM: ATOMS')	

	atoms_data_all = []
	for step, atoms in zip(time_steps, atoms_all_t):
		single_step_data = [] 
		for at in atoms:
			at = at.strip().split()
			if at[1] == str(atom_type):
				single_step_data.append([float(x) for x in at])
		atoms_data_all.append(single_step_data)

	return time_steps, atoms_data_all
 
