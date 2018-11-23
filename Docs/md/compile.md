### 安装编译依赖工具(macOS X and linux)

```
python3 -m pip install scikit-build
python3 -m pip install cython==0.28.5
```

### 安装编译依赖工具(Windows)

#### 安装 Visual Studio

https://visualstudio.microsoft.com/zh-hans/thank-you-downloading-visual-studio/?sku=Community&rel=15


####安装 Windows-10-sdk

https://developer.microsoft.com/en-us/windows/downloads/windows-10-sdk


####安装 Python

https://www.python.org/downloads/


####安装 boost

https://sourceforge.net/projects/boost/files/boost-binaries/1.67.0/boost_1_67_0-msvc-14.1-64.exe/download


#### 安装 Python packages
```
python -m pip install scikit-build
python -m pip install cython==0.28.5
```

###  下载源代码

```
git clone https://www.github.com/learnforpractice/pyeoskit
cd pyeoskit
git submodule update --init --recursive
```

### 在Windows下编译
```
set PATH=%PATH%;"C:\Program Files (x86)\Windows Kits\10\bin\10.0.17763.0\x64"
set LIB=%LIB%;C:\local\boost_1_67_0\lib64-msvc-14.1"
set BOOST_ROOT=C:\local\boost_1_67_0
python setup.py sdist bdist_wheel -G "NMake Makefiles"
```

### 在 macOS X上编译
```
CC=clang CXX=clang++ python3 setup.py sdist bdist_wheel --plat-name macosx-10.9-x86_64
```

### 在Ubuntu上编译
```
CC=clang CXX=clang++ python3 setup.py sdist bdist_wheel  -- -DCMAKE_TOOLCHAIN_FILE=$(pwd)/cmake/polly/clang-fpic.cmake -- -j7
```

### 在Centos编译
```
CC=gcc CXX=g++ python3 setup.py sdist bdist_wheel  -- -DCMAKE_TOOLCHAIN_FILE=$(pwd)/cmake/polly/gcc-pic.cmake -- -j7
```

编译成功后即可通过下面的命令来进行安装
```
python3 -m pip install dist/pyeoskit-[SUFFIX].whl
```
注意在Windows平台下python3应该改成python
