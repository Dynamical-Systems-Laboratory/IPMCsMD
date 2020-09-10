#!/usr/local/bin/python3.6

# ------------------------------------------------------------------
#
#	Calculations related to coordination number 
#
# ------------------------------------------------------------------

import sys
py_path = './io_operations/'
sys.path.insert(0, py_path)

import math 
import select_d_section as dsec
import post_utils as utils 

def compute_coordination_number_all(dfile, atom_type_1, atom_type_2, dR = 0.1, Rmax = 10, steps = None):
	''' Compute coordination number as a function of distance between 
			two types of atoms at all time steps '''
	
	#
	# dfile - LAMMPS .d file
	# atom_type_1, atom_type_2 - integer atom type IDs as specified in the Masses part of .data file
	# 	atom_type_1 is the type which coordination numbers will be returned (the central atom)
	# dR - width of a single shell for counting atoms at a given distance 
	# Rmax - max radius around the central atom to consider
	# steps - optional list of timesteps to consider, all if not specified 
	#
	# Returns a list of time steps and a list of lists of corresponding coordination numbers
	# with first list being radial distance, and second list the coordination number for 
	# that distance; the radial distance is the center of each shell considered a 
	# single position.
	#
	# Time steps and coordination numbers are ints, radial distances are doubles 
	#

	# Extract time steps
	time_steps = dsec.extract_all_sections(dfile, 'ITEM: TIMESTEP')

	# Extract atom data
	atom_data = dsec.extract_all_sections(dfile, 'ITEM: ATOMS')

	# Compute coordination numbers as function of position 
	# and convert time steps to ints
	cn_all = []
	int_steps = []

	for step, atom in zip(time_steps, atom_data):

		step_int = int(step[0])	
		# If selected steps, then skip ones not needed
		if steps:
			if not (step_int in steps):
				continue		
		int_steps.append(step_int)

		# Retrieve all data for these atom types 
		at_data_1 = utils.get_atom_i_data(atom, atom_type_1, 1, [2,3,4])
		if atom_type_1 == atom_type_2:
			at_data_2 = at_data_1
		else:  
			at_data_2 = utils.get_atom_i_data(atom, atom_type_2, 1, [2,3,4])
	
		# Compute and store distances between each atom in 1 and each atom in 2
		# One sublist per atom from atom type 1
		dist_12 = []
		for at1 in at_data_1:
			temp_dist = []
			for at2 in at_data_2:
				temp_dist.append(utils.compute_distance(at1, at2))
			dist_12.append(temp_dist)

		# Compute coordination numbers
		ri, ci = compute_cn(dist_12, dR, Rmax)
		cn_all.append([ri, ci])
			
	return int_steps, cn_all		

def compute_cn(distances, dR, Rmax):
	''' Compute coordination number as a function
			of radial distance '''

	#
	# distances - distances of each atom to all 
	#				other atoms of interest; list of list,
	#				one sublist per atom
	# dR - shell thickness, A
	# Rmax - max distance to consider, A
	#
	# Returns two lists - nominal distances in A and CNs for each
	#	interval (average over all atoms) as an undrounded float
	#

	# Nominal distance array
	nom_dist = []
	# Number of shells/intervals
	Nint = round(Rmax/dR)
	for i in range(Nint):
		# The nominal distance is middle of an
		# interval
		nom_dist.append((i + 0.5)*dR)

	# Number of hits in every shell/box
	# to get an average		

	# Coordination number for each distance
	# interval, default value is 0
	# Average coordination number
	temp_cn = [0]*Nint
	for at_dist in distances:
		for Ri in sorted(at_dist):
			# Stop if threshold exceeded
			# since the list is sorted
			if Ri > Rmax:
				break
			# To avoid including self
			if math.isclose(Ri, 0.0):
				continue		
			# Increment the right shell/box
			temp_cn[math.floor(Ri/dR)] += 1

	# Cumulative sum for each interval	
	cn = [0]*Nint
	for i in range(Nint):
		cn[i] = sum(temp_cn[0:i+1])

	return nom_dist, list(map(lambda x: x/len(distances), cn))
		 		
		
