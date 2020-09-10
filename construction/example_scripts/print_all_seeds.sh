# Copy current version of input checking to each seed directory
# and run it
for i in seed_*/; do
	cd $i/emc_files/
    echo -e "\033[0;31m Random seed from $i \033[0m"
	cat build.emc | grep seed
	cd ../../
done
