
# add_cython_target(_pyeoskit CXX)

add_library(_pyeoskit MODULE
    ${CMAKE_CURRENT_SOURCE_DIR}/_pyeoskit.cxx
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

add_custom_command(OUTPUT ${CMAKE_CURRENT_SOURCE_DIR}/_pyeoskit.cxx
    COMMAND python3 -m cython --cplus -3 -o ${CMAKE_CURRENT_SOURCE_DIR}/_pyeoskit.cxx _pyeoskit.pyx
    DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/_pyeoskit.pyx
    COMMENT "Creating _pyeoskit.cxx"
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
)

add_custom_command(OUTPUT ${CMAKE_CURRENT_SOURCE_DIR}/pyeoskit/libpyeoskit.a
    COMMAND go build -o libpyeoskit.a -buildmode=c-archive
    COMMAND cp libpyeoskit.bk.h libpyeoskit.h
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

