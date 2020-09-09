# ------------------------------------------------------------------
#
#   Module for converting the EMC DPD input into target input 
#
# ------------------------------------------------------------------

import sys, os
py_path = '../postprocessing/io_operations/'
sys.path.insert(0, py_path)

import time

import extract_data_file as ed

def move_atom_columns(data_file, new_data_file):
	''' Moves colums in the Atom file to meet LAMMPS format '''
	
	#
	# data_file - file name
	#
	# Moves column 6 (molecule type) to column 2 and column 7 
	#	(partial charge) to column 4 (numbering starts with 1)
	#
	# Format requirements from:
	# https://lammps.sandia.gov/doc/2001/data_format.html

	# Read atom section
	with open(data_file, 'r') as fin:
		data = ed.extract_data_section(fin, 'Atoms')

	# Modify the section
	for i, atom in enumerate(data):
		entry = atom.strip().split()
		data[i] = (' ').join([entry[0], entry[5], entry[1], entry[6], entry[2], entry[3], entry[4], entry[7], entry[8]])
		
	# Save into modified file
	found_atoms = False			
	with open(data_file, 'r') as fin:
		with open(new_data_file, 'w') as fout:
			for iline in fin:

				# Pre-Atoms portion - just write
				if ('Atoms' not in iline) and (found_atoms == False):
					fout.write(iline)
					continue

				# Atoms - write new data
				if 'Atoms' in iline:
					found_atoms = True
					fout.write('Atoms\n\n')
					iline = next(fin)
					for oline in data:
						fout.write(oline + '\n')
						iline = next(fin)
					continue

				# The remaining of data file - no change
				if found_atoms == True:
					fout.write(iline)  			
		
def exclude_ion_interactions(data_file, new_data_file, ionIDs, col):
	''' Removes ion from bond, angle, and dihedral info in data_file '''

	#
	# data_file - data file
	# ionIDs - list of type IDs of the target ions; types are strings
	# col - column (indexing from 1) where the atom type (as appears in Masses) data occurs
	#			this is to make it independent of column shifting operation
	#
	# This assumes that there are types for interactions of Na in the params file
	#	so it does not alter the type IDs. It changes the interaction ID accordingly
	#	as it is listed in data file, upon removal.
	#

	# Create a map of ionIDs : ion type ID
	with open(data_file, 'r') as fin:
		data = ed.extract_data_section(fin, 'Atoms')

	ion_ID_map = {}
	for line in data:
		line = line.strip().split()
		if line[col-1] in ionIDs:
			ion_ID_map[line[0]] = line[col-1]

	# Read and write until Bonds encountered 	    
	with open(data_file, 'r') as fin:
		with open(new_data_file, 'w') as fout:
			for iline in fin:
				if not ('Bonds' in iline):
					fout.write(iline)
					continue
				if 'Bonds' in iline:
					break

	# Read each section, modify, and write
	num_bonds = int_remove_write('Bonds', data_file, new_data_file, ion_ID_map, [2, 3])
	num_angles = int_remove_write('Angles', data_file, new_data_file, ion_ID_map, [2, 3, 4])
	num_dihedrals = int_remove_write('Dihedrals', data_file, new_data_file, ion_ID_map, [2, 3, 4, 5])

	# Now change the header
	temp_file = 'dpd_temp.data.' + str(int(time.time()))
	copy_data_file(new_data_file, temp_file)
	
	with open(temp_file, 'r') as fin:	
		with open(new_data_file, 'w') as fout:
			for line in fin:
				if 'bonds' in line:
					line = line.strip().split()
					fout.write(str(num_bonds) + ' bonds\n')
					continue
				if 'angles' in line:
					line = line.strip().split()
					fout.write(str(num_angles) + ' angles\n')
					continue
				if 'dihedrals' in line:
					line = line.strip().split()
					fout.write(str(num_dihedrals) + ' dihedrals\n')
					continue
				fout.write(line)
	
	# And remove the temporary file
	os.remove(temp_file)
	
def int_remove_write(tag, infile, outfile, ion_map, int_cols):
	''' Remove specific ions from tag section of infile and append to outfile '''

	# tag - section name, 'Bonds', 'Angles'
	# infile - input data file
	# outfile - output data file, appends - so needs to end before new section
	# ion_map - atom simulation ID : atom type
	# int_cols - list of integers representing columns with atom id in this interaction type

	# Read tagged section
	with open(infile, 'r') as fin:
		data = ed.extract_data_section(fin, tag)

	# Remove target ions
	new_data = []
	int_ind = 1
	for line in data:
		line = line.strip().split()
		skip_line = False
		for i in int_cols:
			if (line[i] in ion_map):
				skip_line = True
				break
		if skip_line == False:
			line[0] = str(int_ind)
			new_data.append((' ').join(line))
			int_ind += 1

	# Append to output file
	with open(outfile, 'a') as fout:
		if tag == 'Bonds':
			fout.write(tag + '\n\n')
		else:
			fout.write('\n' + tag + '\n\n')
		for line in new_data:
			fout.write(line + '\n')	

	return int_ind - 1

def copy_data_file(data_in, data_out):
	''' Copy data_in to data_out '''
	
	# Quick solution, fix later

	with open(data_in, 'r') as fin:
		with open(data_out, 'w') as fout:
			for line in fin:
				fout.write(line)
		
