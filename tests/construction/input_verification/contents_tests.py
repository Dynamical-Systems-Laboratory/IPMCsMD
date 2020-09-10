#!/usr/bin/python3

# ------------------------------------------------------------------
#
#	Suite for testing correctness of contents defined in
#		.data class including all interactions and Atoms data
#
# ------------------------------------------------------------------

# In the following, a tag is defined as symbolic representation
# from EMC LAMMPS input files, e.g. c, f etc. while ID is the numeric
# representation
#
# A tag in .params file has to have the same order of atoms as in 
# the .data file, i.e. c,f is not the same as f,c; blank spaces 
# between atoms (c, f) are fine

import sys
py_path = '../../common/'
sys.path.insert(0, py_path)

import extract_data as ed

class BaseCheck:
	''' Base class for .data file conceptual verifications '''
	 
	def __init__(self, data_file, params_file):
		''' Creates a dict of atom tags : atom IDs '''
			
		# data_file, params_file - LAMMPS .data and .params
		# files respectively
		
		self.data_file = data_file
		self.params_file = params_file
		
		self.atom_IDs = {}
		# Get the data from Masses section
		with open(self.data_file, 'r') as fin:
			atom_data = ed.extract_data_section(fin, 'Masses')
		
		# Make an atom tag : atom ID dictionary
		for atom in atom_data:
			atom = atom.strip().split()
			# Assumes space between # and the tag
			self.atom_IDs[atom[-1]] = atom[0]

class InteractionCheck(BaseCheck):
	''' Class for interaction tests '''

	def __init__(self, data_file, params_file):
		# data_file, params_file - LAMMPS .data and .params
		# files respectively 
		BaseCheck.__init__(self, data_file, params_file) 

	def correct_interaction_type(self, data_name, params_name):
		''' Compare tags and IDs in .param and .data files for given 
				interaction type to check if they match'''
		
		# data_name - name of the .data file section e.g. Bonds, Angles
		# params_name - name of the .params file section; section is
		#	distinguished by the actual coefficient name present in 
		#	each line that defines it e.g. bond_coeff, angle_coeff
		# 
		# Returns True if tags are equal and IDs correspond to one
		# another

		# Get the .data section
		with open(self.data_file, 'r') as fin:
			data = ed.extract_data_section(fin, data_name)

		# Get the .params section as a tag : ID dictionary
		with open(self.params_file, 'r') as fin:
			params = ed.extract_params_dict(fin, params_name)

		# Compare - this also assumes that elements in the tags
		# have the same order i.e. c,f and not f,c
		for line in data:
			line = line.strip().split()

			# Find the begining of atom list 
			ind = line.index('#') + 1
			# The prepare the tag to be just a list of atoms
			tag = tuple(' '.join(line[ind:]).strip().split(','))
			# Now compare the tags and IDs
			if not (params[tag] == int(line[1])):
				return False

		return True

	def correct_interaction_components(self, data_name):
		''' Check if atom types that constitute interaction
				tag match atom IDs in the interaction entry '''

		# data_name - name of the .data file section e.g. Bonds, Angles
		#
		# Returns True if all atom IDs in interactions entry match the
		# nominal IDs according to interaction tags

		# Get the target .data section and the Atoms section
		with open(self.data_file, 'r') as fin:
			data = ed.extract_data_section(fin, data_name)
		with open(self.data_file, 'r') as fin:
			all_atoms_data = ed.extract_data_section(fin, 'Atoms')

		# Compare
		for line in data:
			line = line.strip().split()
			# Find the begining of atom tag list 
			atom_ind = line.index('#') + 1

			# Check each atom - ind serves to 
			# simultaneously navigate through atom IDs
			# range accounts for # character
			atom_list = ' '.join(line[atom_ind:]).split(',')
			for ind, atom in zip(range(2, atom_ind - 1), atom_list):
				# Remove any whitespace
				atom.replace(' ', '')
				
				# Fetch this atom's type ID from Atoms list, assumes IDs 
				# i.e. first column in Atoms data, are sequential
				atom_type_ID = int(all_atoms_data[int(line[ind])-1].strip().split()[2])
				
				# Test if the same IDs 
				if not (int(self.atom_IDs[atom]) == atom_type_ID):
					return False

		return True

class AtomsCheck(BaseCheck):
	''' Class for verifying correctness of Atoms
			section in LAMMPS .data file '''
	
	def __init__(self, data_file, params_file):
		''' Loads Atoms section from the .data file ''' 
		
		# data_file, params_file - LAMMPS .data and .params file

		BaseCheck.__init__(self, data_file, params_file)

		with open(self.data_file, 'r') as fin:
			self.atoms = ed.extract_data_section(fin, 'Atoms')

	def correct_atom_types(self):
		''' Verify if each atom type corresponds to its atom tag '''
		
		# Tags are used for partial charge distribution so this 
		# is important

		# Compare
		for line in self.atoms:

			# Entries for this atom
			line = line.strip().split()
			# Atom tag
			atom_tag = line[-1]
			
			# Comparison
			if not (self.atom_IDs[atom_tag] == line[2]):
				return False

		return True
			
# Example demonstrates the usage and also tests the first 
# setup used for simulations
if __name__ == '__main__':

	# LAMMPS .data file
	lmp_data_file = './test_data/nafion.data'
	# LAMMPS .params file
	lmp_params_file = './test_data/nafion.params'

	#
	# Atoms
	#

	atoms_check = AtomsCheck(lmp_data_file, lmp_params_file) 
	print(atoms_check.correct_atom_types())
   
	#
	# Interactions
	#

	int_check = InteractionCheck(lmp_data_file, lmp_params_file)

	# Bonds
	print(int_check.correct_interaction_type('Bonds', 'bond_coeff'))
	print(int_check.correct_interaction_components('Bonds'))
	
	# Angles
	print(int_check.correct_interaction_type('Angles', 'angle_coeff'))
	print(int_check.correct_interaction_components('Angles'))

	# Dihedrals
	print(int_check.correct_interaction_type('Dihedrals', 'dihedral_coeff'))
	print(int_check.correct_interaction_components('Dihedral'))



