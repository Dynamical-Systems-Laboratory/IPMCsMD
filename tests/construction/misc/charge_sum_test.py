#!/usr/bin/python3

# ------------------------------------------------------------------
#
#  Test for charge_sum function
#
# ------------------------------------------------------------------

import sys
py_path = '../../../construction/'
sys.path.insert(0, py_path)

import math
import compass_to_oplsaa as conv

def check_charge(atoms, exp_charge):
    ''' Compute total charge and compare with expected '''
    # atoms - instance of AtomsCharge class
    # exp_charge - expected charge (float)
    
    new_charge = conv.charge_sum(atoms.new_atoms_data, False)
    return math.isclose(new_charge, exp_charge, rel_tol = 1e-5)


#
# Setup
#

# File with rules for conversion
chconv_file = 'ctest_rules.txt'

# Unconverted .data file
emc_file = 'emc_nafion.data'

# Expected charge
exp_charge = 1.328 

#
# Test
#

# Charge conversion class instance
# i.e. charge conversion rules
conv_rules = conv.ChargeConv(chconv_file)

# Convert partial charges
atoms_pc = conv.AtomsCharge(emc_file, conv_rules)

# Test
print(check_charge(atoms_pc, exp_charge))
