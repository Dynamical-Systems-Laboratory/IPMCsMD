#!/usr/bin/python3

# ------------------------------------------------------------------
#
#  Test suite for ChargeConv class 
#
# ------------------------------------------------------------------

import sys
py_path = '../../../construction/'
sys.path.insert(0, py_path)

import math
import compass_to_oplsaa as conv

#
# Supporting functions
#

def test_bond_charges(bonds, conv_rules):
    ''' Checks if all converted values equal to expected'''

    # bonds - dictionary of bond keys vs. expected charge values
    # conv_rules - instance of ChargeConv class
    # Returns True if everything is correct, False otherwise

    # For each entry in bonds, check if
    # equal to expected
    for key, value in bonds.items():
    
        # Converted
        atom_charge, cf, cf_charge = conv_rules.get_charge(key)
    
        # If no value detected
        if atom_charge == False:
            # For an expected value not equal to False 
            # the value can only be associated with 
            # a '//c,f' entry
            if value:
                if '//c,f' not in key:
                    return False
            elif not (value == atom_charge):
                return False

        # General case
        if not math.isclose(float(atom_charge), value, rel_tol=1e-5):
            return False

        # //c,f case
        if cf:
            cf_key = key + '//c,f'
            if not math.isclose(bonds[cf_key], float(cf_charge), rel_tol=1e-5):
                return False

    return True

#
# Setup
#

# File with rules for conversion
chconv_file = 'ctest_rules.txt'

#
# Bonds to test
#

# Key is the bond,
# value is the expected charge
bonds = {}

# Regular bonds
bonds['cl,s'] = -0.5765
bonds['c,oc#c,oc'] = -0.317

# Different bond order 
bonds['o=,s#o=,s#cl,s#c,s'] = 1.2787

# Case with //c,f
bonds['c,c#c,f#c,f#c,f'] =  0.34600000
bonds['c,c#c,f#c,f#c,f//c,f'] = -0.09890000

# Non-existent bond (False will also be returned by
# stand-alone //c,f bond
bonds['not#there'] = False

#
# Test
#

# Charge conversion class instance
# i.e. charge conversion rules
conv_rules = conv.ChargeConv(chconv_file)

print(test_bond_charges(bonds, conv_rules))


















