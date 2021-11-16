
add_cython_target(_pyeoskit CXX)

add_library(_pyeoskit MODULE
    ${_pyeoskit}
)

python_extension_module(_pyeoskit)

add_dependencies(_pyeoskit build_pyeoskit)

target_link_libraries(_pyeoskit ${CMAKE_CURRENT_SOURCE_DIR}/pyeoskit/libpyeoskit.a)

target_include_directories(_pyeoskit PRIVATE 
    ${CMAKE_CURRENT_SOURCE_DIR}/pyeoskit
)

if (WIN32)
    add_compile_definitions(MS_WIN64)
endif()

add_custom_command(OUTPUT ${CMAKE_CURRENT_SOURCE_DIR}/pyeoskit/libpyeoskit.a
    COMMAND go build -o libpyeoskit.a -buildmode=c-archive
    DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/pyeoskit/lib.go
    DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/pyeoskit/main.go
    COMMENT "Creating libpyeoskit.a"
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/pyeoskit
)

add_custom_target(build_pyeoskit ALL
    COMMAND echo "Building libpyeoskit.a"
    DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/pyeoskit/libpyeoskit.a
    # to make quotes printable,for example
    VERBATIM
)

install(TARGETS _pyeoskit LIBRARY DESTINATION pysrc)

