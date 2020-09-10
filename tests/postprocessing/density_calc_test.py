# ------------------------------------------------------------------
#
#	Tests for density_calculations module 
#
# ------------------------------------------------------------------

import sys
py_path = '../../postprocessing/io_operations/'
sys.path.insert(0, py_path)

import sys
py_path = '../../postprocessing/'
sys.path.insert(0, py_path)

import math
import density_calculations as den_clc

# Input files
data_file = './test_data/den_test.data'
dfile = './test_data/den_test.d'

# Total expected mass in g
mtot = 3.9198e-22

# Expected volumes in  cm^3
vol = [1.0259e-19, 1.0238e-19]

# Time steps and expected density in g/cm^3
t_exp = [5159500, 5160000]
rho_exp = [3.8208e-03, 3.8288e-03]

# Compute density and compare
time_steps, bulk_density = den_clc.compute_density_all(data_file, dfile)
for ts, den, ts_exp, d_exp in zip(time_steps, bulk_density, t_exp, rho_exp):
	print('Density: ', str(math.isclose(d_exp, den, rel_tol = 1e-3)))
	print('Time step: ', str(math.isclose(ts_exp, ts, rel_tol = 1e-3)))
	
