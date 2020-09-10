# ------------------------------------------------------------------
#
#	Analysis of results related to bulk system density 
#
# ------------------------------------------------------------------

import sys
py_path = '../../../../../postprocessing/'
sys.path.insert(0, py_path)
py_path = '../../../../../postprocessing/io_operations/'
sys.path.insert(0, py_path)

import os
import density_calculations as den_clc 
import io_module as io

#
# Input
#

# .d file from measurement period
dfile = '../nafion.d'
# .d file form pre-measurement period
d_pre_file = '../pre_nafion.d'
# .data file
cwd = os.getcwd()
seed_no = cwd.split('/')[-2]
data_file ='../../../../../construction/constructed_setups/DPD_based/sodium_models/' + seed_no + '/dpd.data' 
# Output files
den_file = 'bulk_density_w_time.txt'
pre_den_file = 'pre_bulk_density_w_time.txt'

#
# Compute density for all time steps and save 
#

time_steps, bulk_density = den_clc.compute_density_all(data_file, dfile)
io.write_data(den_file, [time_steps, bulk_density], 2)

pre_time_steps, pre_bulk_density = den_clc.compute_density_all(data_file, d_pre_file)
io.write_data(pre_den_file, [pre_time_steps, pre_bulk_density], 2)
