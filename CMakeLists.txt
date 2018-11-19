cmake_minimum_required(VERSION 3.5.0)

list(APPEND CMAKE_MODULE_PATH "${CMAKE_SOURCE_DIR}/libraries/fc/CMakeModules")
list(APPEND CMAKE_MODULE_PATH "${CMAKE_SOURCE_DIR}/libraries/cmake")
list(APPEND CMAKE_MODULE_PATH "${CMAKE_SOURCE_DIR}/cmake")
include( SetupTargetMacros )

#set(PYTHON_LIBRARY "/Users/newworld/anaconda/lib/python3.6/config-3.6m-darwin/libpython3.6m.a")
#set(CYTHON_EXECUTABLE "/Users/newworld/anaconda/bin/cython")
#set(PYTHON_INCLUDE_DIR "/Users/newworld/anaconda/include/python3.6m")

if (NOT WIN32)
set(CYTHON_EXECUTABLE "${CMAKE_SOURCE_DIR}/cython")
endif(NOT WIN32)

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


project(pyeoskit)

if( WIN32 )
#looks like this flag can have different default on some machines.
SET(CMAKE_SHARED_LINKER_FLAGS "${CMAKE_SHARED_LINKER_FLAGS} /SAFESEH:NO")
SET(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} /SAFESEH:NO")

# Probably cmake has a bug and vcxproj generated for executable in Debug conf. has disabled debug info
set(CMAKE_EXE_LINKER_FLAGS_DEBUG "${CMAKE_EXE_LINKER_FLAGS_DEBUG} /DEBUG")

set( CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -DLIEF_DISABLE_FROZEN=on" )

else( WIN32 ) # Apple AND Linux
    if( APPLE )
        # Apple Specific Options Here
        message( STATUS "Configuring EOSIO on OS X" )
        set( CMAKE_CXX_FLAGS "${CMAKE_C_FLAGS} -Wall --std=c++14 -Wno-deprecated-declarations" )
    else( APPLE )
        # Linux Specific Options Here
        message( STATUS "Configuring EOSIO on Linux" )

        set( CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall --std=c++14 -fPIC" )
        set( CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -Wall -fPIC" )
    endif( APPLE )
endif( WIN32 )

include(ProjectMPIR)

hunter_add_package(OpenSSL)
find_package(OpenSSL REQUIRED)


hunter_add_package(ZLIB)
find_package(ZLIB CONFIG REQUIRED)


#set(BOOST_ROOT "C:/boost_1_67_0")

find_package(Boost 1.67.0 COMPONENTS
    iostreams
    date_time
    system 
    chrono
    filesystem
#    zlib
#    bzlib2
)

message(STATUS "${Boost_LIBRARY_DIRS}++++++++++++++++"${Boost_LIBRARIES})
 
find_package(PythonExtensions REQUIRED)
find_package(Cython REQUIRED)

add_subdirectory(libraries)
add_subdirectory(main)
