# ------------------------------------------------------------------
#
#  Test suite for AtomsCharge class 
#
# ------------------------------------------------------------------

# Files created by the test best removed before running:
# 
# test_out.data 

import sys
py_path = '../../../construction/'
sys.path.insert(0, py_path)
py_path = '../../common/'
sys.path.insert(0, py_path)

import math
import substitute_partial_charges as sub
import compare_files as comp

#
# Setup
#

# File with rules for conversion
chconv_file = 'nafion_test_charges.txt'

# Unconverted .data file
orig_file = 'nafion_pre_charge.data'

# Expected converted file
exp_file = 'nafion.data'

# Current converted output file name
test_output = 'test_out.data'

#
# Test
#

#
# Preprocessing
#

# Retrieve data file in pieces for easier processing
begining, all_atoms, ending = sub.load_data_file(orig_file)
# Select and group Nafion atoms 
all_types = sub.split_atoms(all_atoms)

# 
# Substitute partial charges
#

sub_charges = sub.SubPCharges(all_atoms, all_types, chconv_file)
sub_charges.double_oxygen()
sub_charges.rest_of_the_chain()
sub_charges.rest_of_nafion()

#
# Write new data file
#

sub_charges.write_data_file(test_output, begining, ending)


#print(comp.equal_files(exp_file, test_output))
