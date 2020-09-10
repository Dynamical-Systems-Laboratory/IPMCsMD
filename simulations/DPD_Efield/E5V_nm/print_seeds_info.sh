# Print information about each input file:
# - The directory where the .restart file is 
# - The strenght of the electric field 

for i in seed_*/; do
	cd $i
	echo -e "\033[0;31m Information for $i \033[0m"
    echo -e "\033[0;34m Restart file\033[0m"
	cat in.nafion_efield | grep read_restart 
   	echo -e "\033[0;34m Electric field strength\033[0m"
	cat in.nafion_efield | grep sys_efld
 	cd ../
done
