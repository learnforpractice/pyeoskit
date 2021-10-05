
add_cython_target(_uuoskit CXX)

add_library(_uuoskit MODULE
    ${_uuoskit}
)

python_extension_module(_uuoskit)

add_dependencies(_uuoskit build_uuoskit)

target_link_libraries(_uuoskit ${CMAKE_CURRENT_SOURCE_DIR}/uuoskit/libuuoskit.a)

target_include_directories(_uuoskit PRIVATE 
    ${CMAKE_CURRENT_SOURCE_DIR}/uuoskit
)

if (WIN32)
    add_compile_definitions(MS_WIN64)
endif()

add_custom_command(OUTPUT ${CMAKE_CURRENT_SOURCE_DIR}/uuoskit/libuuoskit.a
    COMMAND go build -o libuuoskit.a -buildmode=c-archive
    DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/uuoskit/lib.go
    DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/uuoskit/main.go
    COMMENT "Creating libuuoskit.a"
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/uuoskit
)

add_custom_target(build_uuoskit ALL
    COMMAND echo "Building libuuoskit.a"
    DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/uuoskit/libuuoskit.a
    # to make quotes printable,for example
    VERBATIM
)

install(TARGETS _uuoskit LIBRARY DESTINATION pysrc)

