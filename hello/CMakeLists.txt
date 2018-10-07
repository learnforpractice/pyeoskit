
add_cython_target(_hello CXX)
add_cython_target(wallet CXX)

add_library(_hello MODULE ${_hello} ${wallet})
target_link_libraries( _hello fc wallet_plugin)

target_include_directories( _hello
            PUBLIC  "${CMAKE_CURRENT_SOURCE_DIR}/include" 
            PUBLIC  "${CMAKE_SOURCE_DIR}/libraries/include" 
            PUBLIC  "${CMAKE_SOURCE_DIR}/libraries/eosiolib" 
            PUBLIC  "${CMAKE_SOURCE_DIR}/libraries/chainbase/include"
            PUBLIC  "${CMAKE_SOURCE_DIR}/libraries/wallet_plugin"
            PUBLIC "${PYTHON_INCLUDE_DIR}"
)


python_extension_module(_hello)

install(TARGETS _hello LIBRARY DESTINATION hello)
