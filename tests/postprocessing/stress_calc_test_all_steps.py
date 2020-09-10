# ------------------------------------------------------------------
#
#	Tests for stress calculations module 
#
# ------------------------------------------------------------------

import sys
py_path = '../../postprocessing/io_operations/'
sys.path.insert(0, py_path)

import sys
py_path = '../../postprocessing/'
sys.path.insert(0, py_path)

import math
import stress_processing as str_proc 

def load_expected(fname, ntimes, nbins):
	''' Returns expected stress data stored in a file '''

    # Stress components
	directions = ['xx', 'yy', 'zz', 'xy', 'xz', 'yz']                                 
	times = []
	with open(fname, 'r') as fin:
		for line in fin:
			if 'time' in line:
				# Dict entry for each direction
				# List represents values in each bin
				temp = {}
				for dr in directions:
					temp[dr] = []
				for inb in range(nbins):
					line = next(fin)
					line = line.strip().split()
					for idr, dr in enumerate(directions):
						temp[dr].append(float(line[idr]))
				times.append(temp)	
	return times

def equal_flt_arrays(a1, a2):
	''' Check if all elements in float arrays a1 and a2 
			are almost equal '''
	for x,y in zip(a1, a2):
		if not math.isclose(x, y, rel_tol=0.1):
			return False
	return True	

# Input file
dfile = './test_data/stress_test_all_steps.d'

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

f_res = './test_data/stress_results.txt'
exp_stresses = load_expected(f_res, len(times), nbins) 

#
# Compute and compare
#

stresses = str_proc.compute_spatial_stress(dfile, times, nbins, idir, [], True, True)

for exp, tst in zip(exp_stresses, stresses):
	for key, value in exp.items():
		if not equal_flt_arrays(value, tst[key]):
			print(False)
print(True)

