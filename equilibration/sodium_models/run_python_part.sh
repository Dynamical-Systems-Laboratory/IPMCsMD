#
# Execute the python part of post-processing
#

# Copies all the code from post_processing 
# directory to each seed directory, then runs 
# the python scripts one by one

# Directory in each seed where post_processing is ran
pdir="post_processing/"

for i in seed_*/; do

	# Copy all files
	cp post_processing/*.py "$i${pdir}"
	cd "$i${pdir}"
	echo -e "\033[0;31m Processing $i \033[0m"

	# Run python scripts one by one
	for j in *.py; do
    	[ -f "$j" ] || break
    	echo -e "\033[0;32m ---> Running $j \033[0m"
		python3.6 $j
	done

 	cd ../../
done
