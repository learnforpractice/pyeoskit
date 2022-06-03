
add_cython_target(_pyeoskit CXX)

add_library(_pyeoskit MODULE
    ${_pyeoskit}
)

python_extension_module(_pyeoskit)

add_dependencies(_pyeoskit build_pyeoskit)

target_include_directories(_pyeoskit PRIVATE 
    ${CMAKE_CURRENT_SOURCE_DIR}/pyeoskit
)

if (WIN32)
    add_compile_definitions(MS_WIN64)
    SET(BUILD_TARGET pyeoskit.lib)
    # SET(BUILD_LIB_CMD go build -o pyeoskit.dll -buildmode=c-shared && cmake -E copy pyeoskit.dll ${CMAKE_CURRENT_SOURCE_DIR}/../pysrc/pyeoskit.dll && cmake -E copy libpyeoskit.bk.h libpyeoskit.h)
    SET(BUILD_LIB_CMD go build -o pyeoskit.dll -buildmode=c-shared && cmake -E copy pyeoskit.dll ${CMAKE_CURRENT_SOURCE_DIR}/../pysrc/pyeoskit.dll && gendef pyeoskit.dll && lib /def:pyeoskit.def /machine:x64 /out:pyeoskit.lib)
else()
    SET(BUILD_TARGET libpyeoskit.a)
    SET(BUILD_LIB_CMD go build -o libpyeoskit.a -buildmode=c-archive)
endif()

target_link_libraries(_pyeoskit ${CMAKE_CURRENT_SOURCE_DIR}/pyeoskit/${BUILD_TARGET})

add_custom_command(OUTPUT ${CMAKE_CURRENT_SOURCE_DIR}/pyeoskit/${BUILD_TARGET}
    COMMAND ${BUILD_LIB_CMD}
    DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/pyeoskit/lib.go
    DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/pyeoskit/main.go
    COMMENT "Creating ${BUILD_TARGET}"
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/pyeoskit
)

add_custom_target(build_pyeoskit ALL
    COMMAND echo "Building ${BUILD_TARGET}"
    DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/pyeoskit/${BUILD_TARGET}
    # to make quotes printable,for example
    VERBATIM
)

install(TARGETS _pyeoskit LIBRARY DESTINATION pysrc)
