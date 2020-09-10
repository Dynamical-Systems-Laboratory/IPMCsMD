#!/usr/bin/python3

# ------------------------------------------------------------------
#
#  Test suite for AddIon class 
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

# Converted output file name 
test_output = 'test_out.data'


# Hydronium input information
# Number of species and type IDs for H, O, H, H  
nspec = 10
spec = [9, 10, 9, 9]
# Number of atoms and molecules before 
# adding ions
natoms = 22
nmol = 4
# Number of bonds and angles before
# additions
nbonds = 18
nangles = 10

#
# Test
#

# Charge conversion class instance
# i.e. charge conversion rules
conv_rules = conv.ChargeConv(chconv_file)

# Convert partial charges
atoms_pc = conv.AtomsCharge(emc_file, conv_rules)

# Create .data file 
write_data = conv.DataFile(emc_file, test_output)
# Write to file with converted charges
write_data.write_all(atoms_pc.new_atoms_data)
# Substitute Cl- with O in the Masses section
write_data.sub_Cl()

# Add ion and save
add_h3o = conv.AddHydronium(test_output, spec, nspec)
nhydro = add_h3o.add_hydronium(nmol, natoms, nbonds, nangles)
add_h3o.write_all(test_output)
print(nhydro)

# Test
print(comp.equal_files(exp_file, test_output))
