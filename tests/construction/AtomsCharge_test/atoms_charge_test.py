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
import compass_to_oplsaa as conv
import compare_files as comp

#
# Setup
#

# File with rules for conversion
chconv_file = 'ctest_rules.txt'

# Unconverted .data file
emc_file = 'emc_nafion.data'

# Expected converted file
exp_file = 'nafion.data'

# Current converted output file name
test_output = 'test_out.data'

#
# Test
#

# Charge conversion class instance
# i.e. charge conversion rules
conv_rules = conv.ChargeConv(chconv_file)

# Convert and save
atoms_pc = conv.AtomsCharge(emc_file, conv_rules)
atoms_pc.write_all_new_atoms(test_output)

print(comp.equal_files(exp_file, test_output))


