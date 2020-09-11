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

# Input file
dfile = '../water_ion_efield.d'
# Output file
ofile = 'number_density_'

# Atom types (3 - Na+, 4 - Cl-, 1 - O in H2O)
typeID = [1, 3, 4]
out_file = {'1' : ofile + 'h2o.txt', '3' : ofile + 'na.txt', '4' : ofile + 'cl.txt'}

# Number of bins
nbins = 20
# Direction 
idir = 'x'

# Times at which to compute
times = list(range(2050000,14000000,50000))
times.append(14000000)

#
# Compute number density as a function of x direction
#

for ID in typeID:
	densities = ctd.compute_spatial_density(dfile, ID, times, nbins, idir)
	io.write_data(out_file[str(ID)], densities, len(times))
