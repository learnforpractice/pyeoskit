cmake_minimum_required(VERSION 3.5.0)

list(APPEND CMAKE_MODULE_PATH "${CMAKE_SOURCE_DIR}/libraries/fc/CMakeModules")
list(APPEND CMAKE_MODULE_PATH "${CMAKE_SOURCE_DIR}/libraries/cmake")
list(APPEND CMAKE_MODULE_PATH "${CMAKE_SOURCE_DIR}/cmake")
include( SetupTargetMacros )

set(PYTHON_LIBRARY "/Users/newworld/anaconda/lib/python3.6/config-3.6m-darwin/libpython3.6m.a")
set(CYTHON_EXECUTABLE "/Users/newworld/anaconda/bin/cython")
set(PYTHON_INCLUDE_DIR "/Users/newworld/anaconda/include/python3.6m")

set(HUNTER_CONFIGURATION_TYPES Release)
set(HUNTER_JOBS_NUMBER 4)
set(HUNTER_CACHE_SERVERS "https://github.com/ethereum/hunter-cache")
set(HUNTER_PASSWORDS_PATH ${CMAKE_CURRENT_SOURCE_DIR}/cmake/Hunter/passwords.cmake)

# In CI builds upload the binaries if the GITHUB_USER_PASSWORD was decrypted
# (only for branches and internal PRs).
if("$ENV{CI}" AND NOT "$ENV{GITHUB_USER_PASSWORD}" STREQUAL "")
    set(run_upload YES)
else()
    set(run_upload NO)
endif()
option(HUNTER_RUN_UPLOAD "Upload binaries to the cache server" ${run_upload})

include(HunterGate)
HunterGate(
    URL "https://github.com/learnforpractice/hunter/archive/v0.20.27.4.tar.gz"
    SHA1 "882c17534196984878955f7d963b02ad7a41c0c4"
    LOCAL
)


project(hello_cython)

set( CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall --std=c++14 -stdlib=libc++" )
set( CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -Wall" )

include(ProjectMPIR)

hunter_add_package(OpenSSL)
find_package(OpenSSL REQUIRED)


hunter_add_package(ZLIB)
find_package(ZLIB CONFIG REQUIRED)

hunter_add_package(Boost COMPONENTS 
    filesystem
    date_time
    system
    chrono
)

find_package(Boost CONFIG REQUIRED
    filesystem
    date_time
    system
    chrono
)


find_package(PythonExtensions REQUIRED)
find_package(Cython REQUIRED)

add_subdirectory(libraries)
add_subdirectory(hello)
