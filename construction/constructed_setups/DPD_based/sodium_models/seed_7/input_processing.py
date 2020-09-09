# ------------------------------------------------------------------
#
#  Convert DPD data file into the target one 
#
# ------------------------------------------------------------------

import sys, os
py_path = '../../../../'
sys.path.insert(0, py_path)

py_path = '../../../../../postprocessing/io_operations/'
sys.path.insert(0, py_path)

import dpd_input_processing as dpd
import extract_data_file as ed

#
# Input
#

# Test input data file
data_in = 'dpd.data'
# Output file name
data_out = 'dpd_temp_out.data'

#
# Conversion
#

# Ion IDs for removal
# This part tests if it is correct for one atom ion
ionIDs = ['6']
# Atoms column where the nominal (Masses) type ID is
# Indexing from 1
atom_type_col = 3

# For now.. need to deal with file copying in
# an entirely different way
dpd.move_atom_columns(data_in, data_out)
dpd.copy_data_file(data_out, data_in)
dpd.exclude_ion_interactions(data_in, data_out, ionIDs, atom_type_col)
dpd.copy_data_file(data_out, data_in)

os.remove('dpd_temp_out.data')
