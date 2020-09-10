#!/usr/bin/python3

# ------------------------------------------------------------------
#
#  Functions for file comparisons 
#
# ------------------------------------------------------------------

import math
	
def equal_files(fname_1, fname_2):
	''' Determines equality of two files '''
	# fname_1, fname_2 - file names
	# Returns True if equal, False otherwise
	# Uses comparison for floats with 1e-5 relative tolerance

	# Read both files
	with open(fname_1, 'r') as fin_1:
		file_1 = fin_1.readlines()
	with open(fname_2, 'r') as fin_2:
		file_2 = fin_2.readlines()

	# Remove the header with version info
	if 'LAMMPS' in file_1[0]:
		file_1 = file_1[1:]
	if 'LAMMPS' in file_2[0]:
		file_2 = file_2[1:]

	# Compare line by line
	for data_1, data_2 in zip(file_1, file_2):
		data_1 = data_1.strip().split()
		data_2 = data_2.strip().split()

		for d1,d2 in zip(data_1, data_2):
			# If d1 is a string without numbers, compare directly
			if not any(i.isdigit() for i in d1):
				if not (d1 == d2):
					return False
				else:
					continue

			# If it's a number
			if not math.isclose(float(d1), float(d2), rel_tol=1e-4):
				return False

	return True

def simple_equal_files(fname_1, fname_2):
	''' Determines equality of two files using comparison operator '''
	# fname_1, fname_2 - file names
	# Returns True if equal, False otherwise
	# Whitespae differences or floating point comparisons will
	# result in inequality

	# Read both files
	with open(fname_1, 'r') as fin_1:
		file_1 = fin_1.readlines()
	with open(fname_2, 'r') as fin_2:
		file_2 = fin_2.readlines()

	# Return comparison outcome
	return file_1 == file_2
