# ------------------------------------------------------------------
#
#	RDF and CN related analysis	
#
# ------------------------------------------------------------------

import sys
py_path = '../../../../../postprocessing/'
sys.path.insert(0, py_path)
py_path = '../../../../../postprocessing/io_operations/'
sys.path.insert(0, py_path)

import cn_and_rdf_lmp as crl
import io_module as io

#
# Input
#

# RDF and CN intput file
rdf_file = '../nafion.rdf'

# Output file
out_file = 'rdf_cn_averaged.txt'

# Number of bins
nbins = 300

# Number of columns
ncols = 10

crl.compute_time_average(rdf_file, out_file, nbins, ncols)


