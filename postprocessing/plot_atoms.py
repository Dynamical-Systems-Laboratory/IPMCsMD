# ------------------------------------------------------------------
#
#	Atom visualization module 
#
# ------------------------------------------------------------------

from mayavi import mlab
import numpy as np

import sys
py_path = './io_operations/'
sys.path.insert(0, py_path)

import select_d_section as dsec
import post_utils as utils

def plot_atom_type(fname, atomID, colors, time):
	''' Visualize all atoms of certain type during the simulation '''

	# fname - name of the d file 
	# atomID - atom type as defined in .data file
	# colors - colors, list of RGB tuples, one per time step
	# time - array with simulation times to plot

	# Extract time steps
	time_steps = dsec.extract_all_sections(fname, 'ITEM: TIMESTEP')

	# Extract atom data
	atoms_all_t = dsec.extract_all_sections(fname, 'ITEM: ATOMS')	

	ist = 0
	for step, atoms in zip(time_steps, atoms_all_t):
		if not (int(step[0]) in time):
			continue
		atom_data = [] 
		for at in atoms:
			at = at.strip().split()
			if at[1] == str(atomID):
				atom_data.append([float(at[2]), float(at[3]), float(at[4])])

		atom_np = np.array(atom_data, dtype=np.float32)
		mlab.points3d(atom_np[:,0], atom_np[:,1], atom_np[:,2], color = colors[ist])
		ist += 1
	
	mlab.show()
		
def plot_atom_ID(fname, atomID, colors, time):
	''' Visualize an atom with given ID during the simulation '''

	# fname - name of the d file 
	# atomID - atom ID
	# colors - colors, list of RGB tuples, one per time step
	# time - array with simulation times

	# Extract time steps
	time_steps = dsec.extract_all_sections(fname, 'ITEM: TIMESTEP')

	# Extract atom data
	atoms_all_t = dsec.extract_all_sections(fname, 'ITEM: ATOMS')	

	ist = 0
	for step, atoms in zip(time_steps, atoms_all_t):
		if not (int(step[0]) in time):
			continue
		atom_data = [] 
		for at in atoms:
			at = at.strip().split()
			if at[0] == str(atomID):
				atom_data.append([float(at[2]), float(at[3]), float(at[4])])

		atom_np = np.array(atom_data, dtype=np.float32)
		mlab.points3d(atom_np[:,0], atom_np[:,1], atom_np[:,2], color = colors[ist])
		ist += 1
	
	mlab.show()
