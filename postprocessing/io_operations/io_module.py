#!/usr/local/bin/python3.6

# ------------------------------------------------------------------
#
#	Module for general I/O operations 				  
#
# ------------------------------------------------------------------ 

def write_data(fname, data, num_col):
	''' Save data with a fixed number of columns to file '''

	#
	# fname - file name
	# data - data set in a form of nested lists, one list per column
	# num_col - number of columns in the data
	# 

	with open(fname, 'w') as fout:
		for i in range(len(data[0])):
			for col in range(num_col):
				fout.write(str(data[col][i]))
				fout.write(' ')
			fout.write('\n')

