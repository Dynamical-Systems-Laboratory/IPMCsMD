#!/usr/local/bin/python3.6

# ------------------------------------------------------------------
#
#	Processing files for later use	 
#
# ------------------------------------------------------------------

def remove_trailing_spaces(file_in, file_out):
	''' Remove trailing spaces from each line of file, keep newline '''
	
	# file_in, file_out - input and output file names

	with open(file_in, 'r') as fin:
		with open(file_out, 'w') as fout:
			for line in fin:
				line = line.rstrip() + '\n'
				fout.write(line)
