import sys
py_path = '../../../../../postprocessing/io_operations/'
sys.path.insert(0, py_path)

import sys
py_path = '../../../../../postprocessing/'
sys.path.insert(0, py_path)

import compute_type_densities as ctd
import io_module as io

#
# Input
#

# Input files
dfile = '../efield_nafion.d'
# Output files
ofile = 'number_density_'
pre_ofile = 'pre_number_density_'

# Atom types (6 - Na+, 4 - S, 8 - O in H2O)
typeID = [6, 4, 8]
out_file = {'8' : ofile + 'h2o.txt', '6' : ofile + 'na.txt', '4' : ofile + 's.txt'}
pre_out_file = {'8' : pre_ofile + 'h2o.txt', '6' : pre_ofile + 'na.txt', '4' : pre_ofile + 's.txt'}

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
# Compute number density as a function of x direction
#

for ID in typeID:
	densities = ctd.compute_spatial_density(dfile, ID, times, nbins, idir)
	io.write_data(out_file[str(ID)], densities, len(times))

	pre_densities = ctd.compute_spatial_density(dfile, ID, pre_times, nbins, idir)
	io.write_data(pre_out_file[str(ID)], pre_densities, len(pre_times))

