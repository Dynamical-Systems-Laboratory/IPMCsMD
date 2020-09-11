import sys
py_path = '../../../../../postprocessing/io_operations/'
sys.path.insert(0, py_path)

import sys
py_path = '../../../../../postprocessing/'
sys.path.insert(0, py_path)

import glob, os
import stress_processing as sp
import io_module as io

#
# Input
#

# Input file
dfile = '../efield_nafion.d'
# Output file
ofile = 'stresses_out_'
pre_ofile = 'pre_stresses_out_'

# Remove all old files because this code appends
for filename in glob.glob(ofile + '*.txt'):
	os.remove(filename)
for filename in glob.glob(pre_ofile + '*.txt'):
	os.remove(filename)

# Stress directions
out_file = {'xx' : ofile + 'xx.txt', 'yy' : ofile + 'yy.txt', 'zz' : ofile + 'zz.txt',
				'xy': ofile + 'xy.txt', 'xz': ofile + 'xz.txt', 'yz': ofile + 'yz.txt'}
pre_out_file = {'xx' : pre_ofile + 'xx.txt', 'yy' : pre_ofile + 'yy.txt', 'zz' : pre_ofile + 'zz.txt',
				'xy': pre_ofile + 'xy.txt', 'xz': pre_ofile + 'xz.txt', 'yz': pre_ofile + 'yz.txt'}

# Number of bins
nbins = 20
# Direction 
idir = 'x'

# Times at which to compute
times = list(range(8660000,11650000,10000))
times.append(11650000)

pre_times = list(range(8160000,8650000,10000))
pre_times.append(8650000)

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

stresses = sp.compute_spatial_stress(dfile, pre_times, nbins, idir)
for str_time in stresses:
	for str_dir, str_value in str_time.items():
		with open(pre_out_file[str_dir], 'a') as fout:
			for val in str_value:
				fout.write(str(val))
				fout.write(' ')
			fout.write('\n')



