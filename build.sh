python3 src/check_modification.py src/uuoskit
CC=clang CXX=clang++ python3 setup.py sdist bdist_wheel
if [ $? -eq 0 ]; then
./install.sh
fi
# End: build.sh

