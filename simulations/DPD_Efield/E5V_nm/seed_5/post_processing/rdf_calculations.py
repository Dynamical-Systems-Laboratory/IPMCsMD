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
rdf_file = '../with_efield_nafion.rdf'
# RDF and CN intput file
pre_rdf_file = '../pre_efield_nafion.rdf'

# Output files
out_file = 'rdf_cn_averaged.txt'
pre_out_file = 'pre_rdf_cn_averaged.txt'

# Number of bins
nbins = 300

# Number of columns
ncols = 10

# Part with the electric field
crl.compute_time_average(rdf_file, out_file, nbins, ncols)
# Part before that
crl.compute_time_average(pre_rdf_file, pre_out_file, nbins, ncols)

