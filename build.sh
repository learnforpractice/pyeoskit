python3 src/check_modification.py src/uuoskit
CC=clang CXX=clang++ python3 setup.py sdist bdist_wheel --plat-name macosx-10.9-x86_64 -- -- -j$(sysctl -n hw.logicalcpu)
if [ $? -eq 0 ]; then
./install.sh
fi
# End: build.sh

