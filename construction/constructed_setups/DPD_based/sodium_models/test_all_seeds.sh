# Copy current version of input checking to each seed directory
# and run it
for i in seed_*/; do
	cp input_check.py $i 
	cd $i
    echo -e "\033[0;31m Running test: $i \033[0m"
	python3.6 input_check.py
	cd ../
done
