# Print information about each input file:
# - The random seed used in each run
# 		to check if they are all unique
# - The directory where the .data file and
# 		params come from to see if all is correct
# - The random seed used in the building part

# Run as ./print_all_seeds.sh cn_dir where cn_dir is 
# 	the path to directory where the construction 
#	files are

# Directory and file with original EMC files and random seeds
edir="emc_files/build.emc"

for i in seed_*/; do
	cd $i
	echo -e "\033[0;31m Information for $i \033[0m"
    echo -e "\033[0;34m Random seed\033[0m"
	cat in.nafion_bulk | grep vseed
   	echo -e "\033[0;34m Construction seed\033[0m"
	cat "$1$i${edir}" | grep seed
   	echo -e "\033[0;34m Construction directory\033[0m"
	cat in.nafion_bulk | grep source  
	cat in.nafion_bulk | grep params
	cat in.nafion_bulk | grep data_file
 	cd ../
done
