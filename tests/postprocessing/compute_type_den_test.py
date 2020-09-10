# ------------------------------------------------------------------
#
#	Tests for compute_type_densities module 
#
# ------------------------------------------------------------------

import sys
py_path = '../../postprocessing/io_operations/'
sys.path.insert(0, py_path)

import sys
py_path = '../../postprocessing/'
sys.path.insert(0, py_path)

import math

import compute_type_densities as ctd

def equal_flt_arrays(a1, a2):
	''' Check if all elements in float arrays a1 and a2 
			are almost equal '''
	for x,y in zip(a1, a2):
		if not math.isclose(x, y, rel_tol=1e-4):
			return False
	return True	

#
# Input
#

# Input file
dfile = './test_data/nd_test.d'

# Atom type
typeID = 2
# Number of bins
nbins = 3
# Direction 
idir = 'x'

# Times at which to compute
times = [5159500, 5160000, 5161000]

#
# Expected results and test
# 

# Returning per volume
nd_exp = [[5.84830e-5, 5.84830e-5, 5.84830e-5], [8.79095e-5, 8.79095e-5, 0.00014652], [0.006060606, 0.0, 0.0121212]]

densities = ctd.compute_spatial_density(dfile, typeID, times, nbins, idir, [], False, True)

for tst, exp in zip(densities, nd_exp):
	if not equal_flt_arrays(tst, exp):
		print(False)
print(True)


