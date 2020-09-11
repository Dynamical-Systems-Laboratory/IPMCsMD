#
# Script to split the datasets based on times
#

def split_files(t_last, file_1, file_2, file_orig, dfile = False):
	''' Divide file_orig into file_1 before time t_last
			andd file_2 inclusive and after '''
	# Fist find the indices
	ind_first_end = 0
	ind_last_start = 0
	condition = False
	with open(file_orig, 'r') as fin:
		for i, line in enumerate(fin):
			temp = line.strip().split()
			if dfile:
				condition = str(t_last) in temp
			else:
				condition = (t_last < float(temp[0]))
			if condition:
				ind_first_end = i - 1
				ind_last_start = i
				break
	
	write_to_2nd = False
	with open(file_orig, 'r') as fin:
		with open(file_1, 'w') as fout_1:
			with open(file_2, 'w') as fout_2:
				for i, line in enumerate(fin):
					if write_to_2nd == False:
						fout_1.write(line)
						if i == ind_first_end:
							write_to_2nd = True
					else:
						fout_2.write(line)
	
# End of first dataset (first step not to include)
t_last = 8651918
t_ld = 8660000 

# All files for conversion 
split_files(t_ld, 'pre_efield_nafion.d', 'with_efield_nafion.d', 'efield_nafion.d', True)
#split_files(t_last, 'pre_efield_nafion.rdf', 'with_efield_nafion.rdf', 'nafion.rdf', True)
#split_files(t_last, 'pre_efield_nafion.ion_diff', 'with_efield_nafion.ion_diff', 'nafion.ion_diff')
#split_files(t_last, 'pre_efield_nafion.water_diff', 'with_efield_nafion.water_diff', 'nafion.water_diff')
