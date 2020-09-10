#!/usr/local/bin/python3.6

# ------------------------------------------------------------------
#
#	Tests for coordination_number_calculations module 
#
# ------------------------------------------------------------------

import sys
py_path = '../../postprocessing/io_operations/'
sys.path.insert(0, py_path)

import sys
py_path = '../../postprocessing/'
sys.path.insert(0, py_path)

import math
import coordination_number_calculations as cn_clc

def equal_flt_arrays(a1, a2):
	''' Check if all elements in float arrays a1 and a2 
			are almost equal '''
	for x,y in zip(a1, a2):
		if not math.isclose(x, y, rel_tol=1e-3):
			return False
	return True	

# Input .d file
dfile = './test_data/cn_test.d'

# Types 
type_1 = 5
type_2 = 9

# Cutoff
Rmax = 1.0
# Shell radius
dR = 0.2

# Time steps for collection
t_exp = [5159500, 516]

# Expected compartment coordinates
r_exp = [0.1, 0.3, 0.5, 0.7, 0.9]

# Expected average coordination numbers for each step
cn_exp = [[0.0, 0.333, 0.333, 0.333, 2.0], [0.0, 0.333, 0.333, 0.333, 1.333]]

# Compute CN and compare
time_steps, cn_comp = cn_clc.compute_coordination_number_all(dfile, type_1, type_2, dR, Rmax, t_exp)

print('Time steps: ', str(equal_flt_arrays(time_steps, t_exp)))
for i in range(len(t_exp)):
	print('Radial distance: ', str(equal_flt_arrays(cn_comp[i][0], r_exp)))
	print('CN: ', str(equal_flt_arrays(cn_comp[i][1], cn_exp[i])))

	print(cn_comp)
