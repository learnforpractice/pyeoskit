
add_cython_target(_hello CXX)
add_cython_target(_eosapi CXX)
add_cython_target(wallet CXX)
add_cython_target(pyobject CXX)

set(SRCS ${_hello} 
         ${_eosapi} 
         ${wallet} 
         ${pyobject}
         wallet_.cpp 
         pyobject.cpp 
         main.cpp 
         eosapi.cpp
         hello.cpp)

add_library(_hello MODULE ${SRCS})

if (WIN32)
    set(EXTRA_LIBS Userenv.lib CRYPT32.lib)
endif(WIN32)

if (APPLE)
else()
    set(EXTRA_LIBS util)
endif()

target_link_libraries( _hello fc wallet_plugin eosio_chain eos_utilities ${EXTRA_LIBS})

add_executable(hello ${SRCS})

target_link_libraries(hello fc wallet_plugin eosio_chain eos_utilities 
${PYTHON_LIBRARY} ${EXTRA_LIBS})

set(INCS   "${CMAKE_CURRENT_SOURCE_DIR}" 
           "${CMAKE_CURRENT_SOURCE_DIR}/include" 
           "${CMAKE_SOURCE_DIR}/libraries/chain/include" 
           "${CMAKE_SOURCE_DIR}/libraries/eosiolib" 
           "${CMAKE_SOURCE_DIR}/libraries/chainbase/include"
           "${CMAKE_SOURCE_DIR}/libraries/wallet_plugin"
           "${PYTHON_INCLUDE_DIR}"
           )

target_include_directories( _hello
            PUBLIC  "${INCS}"
)

target_include_directories( hello
            PUBLIC  "${INCS}"
)

python_extension_module(_hello)

install(TARGETS _hello LIBRARY DESTINATION main)
