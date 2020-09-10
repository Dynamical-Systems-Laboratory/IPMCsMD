# ------------------------------------------------------------------
#
#	Module for importing thermo information	
#
# ------------------------------------------------------------------

def import_and_save_thermo(fname_in, fname_out):
	''' Loads thermo from log file fname_in and saves it
			to fname_out '''

	data = read_thermo(fname_in)
	with open (fname_out, 'w') as fout:
		for row in data:
			fout.write((' ').join(map(str,row)))
			fout.write('\n')

def read_thermo(fname_in):
	''' Loads thermo from fnam_in log file '''

	data = []
	with open (fname_in, 'r') as fin:
		for line in fin:
			if "Step Time" in line:
				line = next(fin)
				while not ("Loop time" in line):
					line = line.strip().split()
					temp_data = []
					for col in line:
						temp_data.append(float(col))
					data.append(temp_data)
					line = next(fin)
	return data

