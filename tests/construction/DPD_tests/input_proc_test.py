# ------------------------------------------------------------------
#
#  Test suite for post-processing of input from DPD 
#
# ------------------------------------------------------------------

# Files that need to be there to run the test
#
# test_in_Na.data
# out_Na_expected.data

# Files created by the test best removed before running:
# 
# test_out_Na.data

import sys
py_path = '../../../construction/'
sys.path.insert(0, py_path)

py_path = '../../common/'
sys.path.insert(0, py_path)

py_path = '../../../postprocessing/io_operations'
sys.path.insert(0, py_path)

import dpd_input_processing as dpd
import compare_files as comp

#
# Input
#

# Test input data file
data_in = 'test_in_Na.data'
# Expected data file after processing
data_exp = 'out_Na_expected.data'
# Output file name
data_out = 'test_out_Na.data'
# Temporary file name
data_temp = 'test_out_temp.data'

#
# Conversion
#

# Ion IDs for removal
# This part tests if it is correct for one atom ion
ionIDs = ['6']
# Atoms column where the nominal (Masses) type ID is
# Indexing from 1
atom_type_col = 3

dpd.move_atom_columns(data_in, data_out)
dpd.copy_data_file(data_out, data_temp)
dpd.exclude_ion_interactions(data_temp, data_out, ionIDs, atom_type_col)

#
# Test
#

print(comp.equal_files(data_exp, data_out))
