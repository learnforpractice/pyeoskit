CC=clang CXX=clang++ python3.7 setup.py sdist bdist_wheel  -- -DCMAKE_TOOLCHAIN_FILE=$(pwd)/cmake/polly/clang-fpic.cmake -- -j$(nproc)

