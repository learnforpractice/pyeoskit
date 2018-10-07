include(ExternalProject)

set(prefix "${CMAKE_BINARY_DIR}/deps")
set(MPIR_LIBRARY "${prefix}/lib/${CMAKE_STATIC_LIBRARY_PREFIX}mpz${CMAKE_STATIC_LIBRARY_SUFFIX}")
set(MPIR_INCLUDE_DIR "${prefix}/include")

ExternalProject_Add(mpir
    PREFIX "${prefix}"
    DOWNLOAD_NAME mpir-cmake.tar.gz
    DOWNLOAD_NO_PROGRESS TRUE
    URL https://github.com/learnforpractice/mpir/archive/mpir-2.7.0-shared.tar.gz
    URL_HASH SHA256=8062a00defe7dd0c3888627ee4b341141c6be5adb8247f15638de731608dc58f
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=<INSTALL_DIR>
        -DCMAKE_BUILD_TYPE=Release
        -DMPIR_GMP=On
    BUILD_BYPRODUCTS "${MPIR_LIBRARY}"
)

add_library(MPIR::mpir STATIC IMPORTED)
set_property(TARGET MPIR::mpir PROPERTY IMPORTED_CONFIGURATIONS Release)
set_property(TARGET MPIR::mpir PROPERTY IMPORTED_LOCATION_RELEASE ${MPIR_LIBRARY})
set_property(TARGET MPIR::mpir PROPERTY INTERFACE_INCLUDE_DIRECTORIES ${MPIR_INCLUDE_DIR})
add_dependencies(MPIR::mpir mpir)
