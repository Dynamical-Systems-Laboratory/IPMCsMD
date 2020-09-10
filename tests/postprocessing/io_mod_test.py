#!/usr/local/bin/python3.6

# ------------------------------------------------------------------
#
#	Tests for IO module 
#
# ------------------------------------------------------------------

import sys
py_path = '../../postprocessing/io_operations/'
sys.path.insert(0, py_path)

import sys
py_path = '../../postprocessing/'
sys.path.insert(0, py_path)

import math
import io_module as io

#
# Supporting functions
#

def correct_array_io(test_arrays, ncol, file_out):
	''' Check if written array equal to expected '''
	# True if after reading equal to test_arrays 
	# components
	
	for i, data in enumerate(test_arrays):
		
		array_file = file_out + str(i) + '.txt'
		io.write_data(array_file, data, ncol[i])
		
		with open(array_file, 'r') as fin:
			wrote_array = fin.readlines();
	
		# Convert to int and do a direct comparison

		# Number of rows
		if not (len(wrote_array) == len(data[0])):
			return False

		# Content
		for iwa, line in enumerate(wrote_array):
			line = line.strip().split()
			# Check number of columns
			if not(len(line) ==	ncol[i]):
				return False
			# If empty line
			if not line:
				return False
			for jwa, entry in enumerate(line):
				if not (int(entry) == data[jwa][iwa]):
					return False
	return True

#
# Test
#

# File to write to
file_out = './test_data/io_mod_test_out_'

# Contents (each sub-array is a specific test)
# Uses ints and a direct comparison
test_arrays = [[[1, 2, 3], [2, 4, 6]], [[4, 5, 6], [7, 8, 9], [10, 11, 12]]]
test_arrays.append([[1,2], [3,4], [5,6], [7,8]])
ncol = [2,3,4]

# Write, load, and compare to expected
print(correct_array_io(test_arrays, ncol, file_out))
