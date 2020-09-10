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
import membrane_conductivity as mc

# Input .d file
dfile = './test_data/mem_cond_test.d'

# Atom type to consider
atom_type = 3

# Atom charge in C
atom_charge = 1.602e-19

# Strenght of the electric field in V/m
efield = 0.001e10

# Column with velocity parallel to efield
vel_col = 5

# Expected values
exp_time = [5159500, 5160000] 
exp_cond = [2.0456e+05, 3.1296e+04]
exp_ave = 117928

# Time averaged conductivity
ave_cond, time, cond = mc.compute_average_conductivity(dfile, atom_type, atom_charge, efield, vel_col)

# Compare
if not math.isclose(ave_cond, exp_ave, rel_tol=1e-3):
	print(False)

for t, te, c, ce in zip(time, exp_time, cond, exp_cond):
	if not math.isclose(float(t[0].strip()), te, rel_tol=1e-3):
		print(False)
	if not math.isclose(c, ce, rel_tol=1e-3):
		print(False)

print(True)


