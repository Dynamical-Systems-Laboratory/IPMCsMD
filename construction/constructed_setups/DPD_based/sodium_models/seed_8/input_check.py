#
# Input verification
#

import sys
py_path = '../../../../../tests/common/'
sys.path.insert(0, py_path)

py_path = '../../../../../tests/construction/input_verification'
sys.path.insert(0, py_path)

from colors import *
import utils as utils
import contents_tests as contst
import file_structure_tests as fs

# LAMMPS .data file
lmp_data_file = './dpd.data'
# LAMMPS .params file
lmp_params_file = './dpd.params'

# Atom type conversion (new to old atom labelling)
type_map = {'C':'c', 'F':'f', 'GFOc':'oc', 'GGS':'s', 'GOs':'o=', 
				'Na':'na+', 'WH':'hw', 'WO':'o*'} 

#
# Atoms
#

atoms_check = contst.AtomsCheck(lmp_data_file, lmp_params_file) 
utils.test_pass(atoms_check.correct_atom_types(), 'Atom types')

#
# Interactions
#

int_check = contst.InteractionCheck(lmp_data_file, lmp_params_file, type_map)

# Bonds
utils.test_pass(int_check.correct_interaction_type('Bonds', 'bond_coeff'), 'Bond types')
utils.test_pass(int_check.correct_interaction_components('Bonds'), 'Bond constituents')
utils.test_pass(int_check.removed_spurious_interactions('Bonds', 'Na'), 'No Na+ bonds')

# Angles
utils.test_pass(int_check.correct_interaction_type('Angles', 'angle_coeff'), 'Angle type')
utils.test_pass(int_check.correct_interaction_components('Angles'), 'Angle constituents')
utils.test_pass(int_check.removed_spurious_interactions('Angles', 'Na'), 'No Na+ angles')

# Dihedrals
utils.test_pass(int_check.correct_interaction_type('Dihedrals', 'dihedral_coeff'), 'Dihedral type')
utils.test_pass(int_check.correct_interaction_components('Dihedral'), 'Dihedral constituents')
utils.test_pass(int_check.removed_spurious_interactions('Dihedrals', 'Na'), 'No Na+ dihedrals')

#
# .data file structure tests
#

section_names = ['Masses', 'Atoms', 'Bonds', 'Angles', 'Dihedrals']
data_struct = fs.FileStructure(lmp_data_file, section_names)

utils.test_pass(data_struct.check_atoms_pos(), 'Atom information in data file')
utils.test_pass(data_struct.check_section_structure(), 'Data file section structure')

#
# .data structure of underlying data
#

# Number of columns in each section in a sequence of section_names
column_number = [4, 9, 6, 7, 8, 8]
section_info = [(x, y) for x, y in zip(section_names, column_number)]

# Testing class
data_test = fs.DataStructure(lmp_data_file, section_info)

utils.test_pass(data_test.missing_entries_test(), 'Data file missing entries')
utils.test_pass(data_test.column_number_test(), 'Data file number of columns')

