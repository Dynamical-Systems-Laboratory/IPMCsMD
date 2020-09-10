# ------------------------------------------------------------------
#
#	Postprocessing od LAMMPS RDF and CN values	
#
# ------------------------------------------------------------------

def compute_time_average(fname_in, fname_out, nbins, ncols):
	''' Averages cn and rdf data stored in fname_in 
			and saves it to fname_out '''
	
	#
	# Averages over all time steps in fname_in
	#
	# fname_in - input file with LAMMPS rdf and cf data
	# 	Entries for different time steps have to be delimited
	#	by bin number and only have 2 entries; comments are marked with #
	# fname_out - bin number, radial distance, average 
	#	of each column for all time steps (radial distance 
	#	also average just in case)
	# nbins - number of bins used
	# ncols - number of columns in the input file
	#

	# Final average
	avg_bin = [[0.0]*ncols for _ in range(nbins)]
	# Time step counter
	time_step_count = 0
		 	
	with open(fname_in, 'r') as fin:
		for line in fin:
			tline = line.strip().split()

			# Header or empty
			if ('#' in tline or not tline): 				
				continue

			# Delimiter for the next dataset
			if len(tline) < ncols:
				time_step_count += 1
				continue

			# Data
			for i, col in enumerate(tline):
				if i == 0:
					avg_bin[int(tline[0])-1][i] = int(col)
				else:
					avg_bin[int(tline[0])-1][i] += float(col)
	
			# Small input check
			if not (i == ncols - 1):
				raise ValueError('ERROR: Number of columns encountered inconsistent with supplied')

	# Average and save
	with open(fname_out, 'w') as fout:
		for row in avg_bin:

			# Bin number
			fout.write(str(row[0]) + ' ')

			# Average entries
			trow = [str(x/time_step_count) for x in row[1:]]
			tline = (' ').join(trow) + '\n'
			fout.write(tline)

	



				

			
	
