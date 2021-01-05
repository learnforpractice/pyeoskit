Python Toolkit for EOSIO

# Building from Source Code

### Installing Prerequirements(macOS X and linux)

```
python3 -m pip install scikit-build
python3 -m pip install cython==0.28.5
```

### Downloading Source Code

```
git clone https://www.github.com/uuosio/uuoskit
cd uuoskit
git submodule update --init --recursive
```

### Building on macOS
```
./build-mac.sh
```

### Building on Ubuntu
```
./build-linux.sh
```

### Building on Centos
```
CC=gcc CXX=g++ python3 setup.py sdist bdist_wheel  -- -DCMAKE_TOOLCHAIN_FILE=$(pwd)/cmake/polly/gcc-pic.cmake -- -j7
```

### Installation

```
ls dist
python3 -m pip install dist/uuoskit-[SUFFIX].whl
```
