#!/usr/local/bin/python3.6

# ------------------------------------------------------------------
#
#	Various postprocessing utility functions 
#
# ------------------------------------------------------------------

import sys
py_path = './io_operations/'
sys.path.insert(0, py_path)

import extract_data_file as dataf 
import math

def conv_to_float(data):
	''' Convert single string data into a nested list of floats '''
	
	output = []
	for entry in data:
		temp = entry.strip().split()
		output.append(list(map(float, temp)))

	return output

def compute_distance(c1, c2):
	''' Compute distance between two points '''
	# c1, c2 - lists with x, y, z coordinates

	dxdx = (c1[0]-c2[0])*(c1[0]-c2[0])
	dydy = (c1[1]-c2[1])*(c1[1]-c2[1])
	dzdz = (c1[2]-c2[2])*(c1[2]-c2[2])

	return math.sqrt(dxdx + dydy + dzdz)

def compute_total_mass(data_file):
	''' Calculate the total mass of all atoms based on a .data file '''
	
	# data_file - LAMMPS .data file
	#
	# Returns mass in g
	#

	# Extract atom types and all atom data
	# Turn atom types into a dict
	with open(data_file, 'r') as fin:
		atom_types = make_atom_type_dict(dataf.extract_data_section(fin, 'Masses'))
	with open(data_file, 'r') as fin:
		atom_data = dataf.extract_data_section(fin, 'Atoms')

	# Accumulate total mass while looping through atom data
	total_mass = 0.0
	for atom in atom_data:
		atom = atom.strip().split()
		total_mass += atom_types[atom[2]][0]

	# Convert from amu to grams and return
	amu2g = 1.66054e-24
	total_mass *= amu2g 

	return total_mass

def compute_volume(box):
	''' Compute volume of a rectangular box '''
	
	# box - nested list of box coordinates
	#	[[x0, xf], [y0, yf], [z0, zf]]
	#
	# Returns volume in cm^3
	#

	# Dimensions in each direction
	dx = box[0][1] - box[0][0] 
	dy = box[1][1] - box[1][0] 
	dz = box[2][1] - box[2][0] 

	# Conversion from Angstroms^3 to cm^3
	a32cm3 = 1e-24

	# Volume in 
	return dx*dy*dz*a32cm3 

def make_atom_type_dict(data):
	''' Creates a dictionary with atom type information 
			from the data retrieved by extract_data_section '''

    # data - nested list with inner lists being each line of data as a single 
    # string that corresponds to .data file Masses section
	#
	# Returns a dictionary with key being the atom type ID (first column, integer)
	#	as a string and values being a tuple of atom masses and tags; masses are 
	#	doubles

	type_dict = {}
	for atom_type in data:
		atom_type = atom_type.strip().split()
		type_dict[atom_type[0]] = tuple([float(atom_type[1]), atom_type[-1]]) 

	return type_dict

def get_atom_i_data(data, atom_type, ID_cl, data_cls):
	''' Retrieve numeric data for atom_type in the dataset
			data '''

	#
	# data - dataset with each individual line being a string
	# atom_type - atom integer ID 
	# ID_cl - column in the data where atom IDs are located
	# data_cls - list of columns to extract
	#
	# Column numbering starts from 0
	#
	# Returns a list of nested lists of data for each line/row
	# for that atom; return data are floats
	#	

	output = []

	data_flt = conv_to_float(data)
	for line in data_flt:
		if line[ID_cl] == atom_type:
			temp = []
			for cl in data_cls:
				temp.append(line[cl])
			output.append(temp)

	return output		
		



  


			





  
