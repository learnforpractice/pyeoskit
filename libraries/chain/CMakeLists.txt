configure_file(${CMAKE_CURRENT_SOURCE_DIR}/include/eosio/chain/core_symbol.hpp.in ${CMAKE_CURRENT_BINARY_DIR}/include/eosio/chain/core_symbol.hpp)
configure_file(${CMAKE_CURRENT_SOURCE_DIR}/genesis_state_root_key.cpp.in ${CMAKE_CURRENT_BINARY_DIR}/genesis_state_root_key.cpp)

file(GLOB HEADERS "include/eosio/chain/*.hpp" "include/eosio/chain/contracts/*.hpp")
#find_package(LevelDB)

set(PYTHON3 "LD_LIBRARY_PATH=${CMAKE_SOURCE_DIR}/externals/python;${CMAKE_SOURCE_DIR}/externals/python/dist/bin/python3")

add_custom_command(
    OUTPUT ${CMAKE_CURRENT_SOURCE_DIR}/rpc_interface/rpc_interface_.wrap.cpp
    COMMAND ${PYTHON3} -m cython --cplus ${CMAKE_CURRENT_SOURCE_DIR}/rpc_interface/rpc_interface_.pyx -o ${CMAKE_CURRENT_SOURCE_DIR}/rpc_interface/rpc_interface_.wrap.cpp
    DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/rpc_interface/rpc_interface_.pyx
)

file(GLOB HEADERS "include/eosio/chain/*.hpp"
                  "include/eosio/chain/webassembly/*.hpp"
                  "${CMAKE_CURRENT_BINARY_DIR}/include/eosio/chain/core_symbol.hpp" )

## SORT .cpp by most likely to change / break compile
add_library( eosio_chain
             STATIC
              abi_serializer.cpp
              asset.cpp
              name.cpp
              transaction.cpp
              exceptions.cpp
              ${HEADERS}
             )

#add_library(secp256k STATIC IMPORTED)
#set_property(TARGET secp256k PROPERTY IMPORTED_LOCATION "${CMAKE_SOURCE_DIR}/build/deps/lib/libsecp256k1.a")

if ("${CMAKE_BUILD_TYPE}" STREQUAL "Debug")
   target_compile_options(eosio_chain PUBLIC -DDEBUG)
endif()

target_link_libraries( eosio_chain PUBLIC fc )

target_include_directories( eosio_chain
                            PUBLIC ${Boost_INCLUDE_DIR}
                            PUBLIC "${CMAKE_CURRENT_SOURCE_DIR}/include"
                            PUBLIC "${CMAKE_CURRENT_BINARY_DIR}/include"
                            PUBLIC "${CMAKE_CURRENT_SOURCE_DIR}/../wasm-jit/Include"
                            PUBLIC "${CMAKE_CURRENT_SOURCE_DIR}/../../externals/binaryen/src"
                            PUBLIC ${CMAKE_SOURCE_DIR}/libraries/chain
                            PUBLIC ${CMAKE_SOURCE_DIR}/libraries/chainbase/include
                            PUBLIC ${CMAKE_SOURCE_DIR}/externals/python/Include
                            PUBLIC ${CMAKE_SOURCE_DIR}/externals/python
                            PUBLIC ${CMAKE_SOURCE_DIR}/contracts
                            PUBLIC ${CMAKE_SOURCE_DIR}/libraries/vm_manager
                            PUBLIC ${CMAKE_SOURCE_DIR}/libraries/vm/vm_wasm
                            PUBLIC ${CMAKE_SOURCE_DIR}/externals/thrift/src
                            PUBLIC ${CMAKE_SOURCE_DIR}/externals/magic_get/include
                            )

