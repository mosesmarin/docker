# define env vars in init.bash
# remove carriage return char before invocation
sed -i 's/\r//' lambda/init.bash
. lambda/init.bash
python3 lambda/runme.py