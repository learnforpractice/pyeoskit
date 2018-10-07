cmake_minimum_required(VERSION 3.5.0)

project(hello_cython)

set( CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -fPIC --std=c++14 -stdlib=libc++" )
set( CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -Wall -fPIC" )


find_package(PythonExtensions REQUIRED)
find_package(Cython REQUIRED)

add_subdirectory(hello)
