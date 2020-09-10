#!/usr/bin/python3

# ------------------------------------------------------------------
#
#  Test suite for DataFile class 
#
# ------------------------------------------------------------------

# Files created by the test best removed before running:
# 
# test_out_w_Cl.data
# test_out.data

import sys
py_path = '../../../construction/'
sys.path.insert(0, py_path)
py_path = '../../common/'
sys.path.insert(0, py_path)

import math
import compass_to_oplsaa as conv
import compare_files as comp

#
# Setup
#

# File with rules for conversion
chconv_file = 'ctest_rules.txt'

# Unconverted .data file
emc_file = 'emc_nafion.data'

# Expected converted file with Cl-
exp_file_w_Cl = 'nafion_w_Cl.data'
# Expected converted file without Cl-
exp_file = 'nafion.data'

# Converted output file name with Cl-
test_output_w_Cl = 'test_out_w_Cl.data'
# Converted output file name without Cl-
test_output = 'test_out.data'

#
# Test
#

# Charge conversion class instance
# i.e. charge conversion rules
conv_rules = conv.ChargeConv(chconv_file)

# Convert partial charges
atoms_pc = conv.AtomsCharge(emc_file, conv_rules)

# Create .data file with Cl-
write_data_w_Cl = conv.DataFile(emc_file, test_output_w_Cl)
# Write to file with converted charges
write_data_w_Cl.write_all(atoms_pc.new_atoms_data)
# Test
print(comp.equal_files(exp_file_w_Cl, test_output_w_Cl))

# Create .data file without Cl-
write_data = conv.DataFile(emc_file, test_output)
# Write to file with converted charges
write_data.write_all(atoms_pc.new_atoms_data)
# Substitute Cl- with O in the Masses section
write_data.sub_Cl()
# Test
print(comp.equal_files(exp_file, test_output))


