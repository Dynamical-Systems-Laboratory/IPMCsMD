import sys
py_path = '../../../../postprocessing/io_operations/'
sys.path.insert(0, py_path)

import sys
py_path = '../../../../postprocessing/'
sys.path.insert(0, py_path)

import stress_processing as sp
import io_module as io

#
# Input
#

# Input file
dfile = '../water_ion_efield.d'
# Output file
ofile = 'stresses_out_'

# Stress directions
out_file = {'xx' : ofile + 'xx.txt', 'yy' : ofile + 'yy.txt', 'zz' : ofile + 'zz.txt',
				'xy': ofile + 'xy.txt', 'xz': ofile + 'xz.txt', 'yz': ofile + 'yz.txt'}

# Number of bins
nbins = 20
# Direction 
idir = 'x'

# Times at which to compute
times = list(range(2050000,14000000,50000))
times.append(14000000)

#
# Compute stresses as a function of x direction
#

stresses = sp.compute_spatial_stress(dfile, times, nbins, idir)
for str_time in stresses:
	for str_dir, str_value in str_time.items():
		with open(out_file[str_dir], 'a') as fout:
			for val in str_value:
				fout.write(str(val))
				fout.write(' ')
			fout.write('\n')
