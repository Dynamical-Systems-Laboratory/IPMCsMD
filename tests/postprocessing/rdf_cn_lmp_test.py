#!/usr/local/bin/python3.6

# ------------------------------------------------------------------
#
#	Tests for module for postprocessing of CN and RDF from
#		LAMMPS
#
# ------------------------------------------------------------------

import sys
py_path = '../../postprocessing/'
sys.path.insert(0, py_path)

import math
import cn_and_rdf_lmp as crl

def equal_flt_arrays(a1, a2):
	''' Check if all elements in float arrays a1 and a2 
			are almost equal '''
	for x,y in zip(a1, a2):
		if not math.isclose(x, y, rel_tol=1e-4):
			return False
	return True	

def load_and_split(fname):
	''' Read data from file fname and return it as 
			nested lists list per line '''

	data = []
	with open(fname, 'r') as fin:
		for line in fin:
			data.append(line.strip().split())
	return data
			
# Input file
in_file = './test_data/cn_rdf_test_in.rdf'
# Output file
out_file = './test_data/cn_rdf_test_out.rdf'
# File with expected values
exp_file = './test_data/cn_rdf_test_exp.rdf'

# Number of bins
nbins = 9
# Expected number of colums
ncol = 10

# Average CNs and RDFs
crl.compute_time_average(in_file, out_file, nbins, ncol)

# Compare outcome to expected
out_data = load_and_split(out_file)
exp_data = load_and_split(exp_file)
for tst,exp in zip(out_data, exp_data):
	tst = list(map(float, tst))
	exp = list(map(float, exp))
	if not equal_flt_arrays(tst, exp):
		print(False)
print(True)


