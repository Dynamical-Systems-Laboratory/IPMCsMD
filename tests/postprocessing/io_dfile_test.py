# ------------------------------------------------------------------
#
#	Tests for d file IO module 
#
# ------------------------------------------------------------------

import sys
py_path = '../../postprocessing/io_operations/'
sys.path.insert(0, py_path)

import sys
py_path = '../../postprocessing/'
sys.path.insert(0, py_path)

import math
import select_d_section as sds

#
# Supporting functions
#

def atom_type_loading_test(dfile_in, ftimes_exp, fdata_exp):
	''' Check the functionality to load single atom 
			type from a dfile'''

	#
	# dfile_in - hardcoded sample dfile
	# ftimes_exp - file with expected time data
	# fdata_exp - file with expected atom data
	#

	# Extract data
	times, data = sds.extract_atom_type_data(dfile_in, 3)

	# Compare to expected
	
	# Times
	with open(ftimes_exp, 'r') as fin:
		for iln, line in enumerate(fin):
			line = line.strip().split()
			# Compares as strings since they're directly 
			# copy/pasted
			temp_t = times[iln][0].strip()
			if not (temp_t == line[0]):
				return False 

	# Data
	flat_data = [item for sublist in data for item in sublist]
	with open(fdata_exp, 'r') as fin:
		for iln, line in enumerate(fin):
			line = line.strip().split()
			# Compares as floats
			for fd, ld in zip(flat_data[iln], line):
				if not math.isclose(float(fd), float(ld), rel_tol=1e-4):
					return False			
	return True

#
# Test
#

# Inpute file
dfile_in = 'test_data/dfile_io.d'
# Files with expected data
exp_times_file = 'test_data/dfile_test_exp_times.d'
exp_data_file = 'test_data/dfile_test_exp_data.d'

# Test
print(atom_type_loading_test(dfile_in, exp_times_file, exp_data_file))
