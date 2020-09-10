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

#
# Ion information
#

ion_spec = 'ca+'
ion_charge = '+2'
ion_mass = '2020.0'
# In Angstroms (current units)
ion_radius = 3.05
# Number of species without the ion (based on Mass entries)
nspec = 8
# Number of atoms before adding ions
natoms = 22 

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
add_ion = conv.AddIon(test_output, ion_spec, ion_charge, ion_mass, ion_radius)
ncation = add_ion.add_cation(nspec, natoms)
add_ion.write_all(test_output)

# Test
print(comp.equal_files(exp_file, test_output))
