# Quits if no match
# https://stackoverflow.com/a/14505622/2763915
for i in *.py; do
    [ -f "$i" ] || break
    echo -e "\033[0;31m Running test: $i \033[0m"
	python3.6 $i
done
