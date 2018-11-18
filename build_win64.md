```
set PATH=%PATH%;C:\Program Files (x86)\Windows Kits\10\bin\10.0.17763.0\x64
set INCLUDE=%INCLUDE%;H:\pyeoskit\pthreads4
set LIBPATH=%LIBPATH%;C:\Boost\lib

set LIB=%LIB%;C:\boost_1_67_0\lib64-msvc-14.0
```

```
prebuild
https://sourceforge.net/projects/boost/files/boost-binaries
```
```
b2.exe --with-filesystem --with-chrono --with-system --with-date_time --with-iostreams toolset=msvc link=static threading=multi release stage install
```
```
b2.exe --with-filesystem --with-iostreams -s ZLIB_SOURCE="H:\boost_1_67_0\zlib1211" ZLIB_INCLUDE="H:\boost_1_67_0\zlib1211" toolset=msvc link=static threading=multi release
```

```
python setup.py sdist bdist_wheel -G "Visual Studio 14 2015 Win64"
python setup.py sdist bdist_wheel -G "NMake Makefiles" -- -DBOOST_ROOT="C:/boost_1_67_0"
python setup.py sdist bdist_wheel -G "Ninja"
```

```
b2.exe --with-iostreams -s BZIP2_SOURCE=H:\boost_1_67_0\bzip2-master -s ZLIB_SOURCE=H:\boost_1_67_0\zlib1211 toolset=msvc link=static threading=multi release stage
```

