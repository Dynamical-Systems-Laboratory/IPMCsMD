#!/usr/bin/python3

# ------------------------------------------------------------------
#
#  Test suite for ParamFile class 
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

# Expected converted file 
exp_file = 'nafion.data'

# Converted output file name 
test_output = 'test_out.data'

#
# Test
#

# For now this is literally a shell cp
params = conv.ParamFile(exp_file, test_output)
params.copy_orig()

# Test
print(comp.simple_equal_files(exp_file, test_output))
