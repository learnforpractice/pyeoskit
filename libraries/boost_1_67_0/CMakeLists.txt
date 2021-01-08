## SORT .cpp by most likely to change / break compile
set( SRCS
    "iostreams/src/zlib.cpp"
    "filesystem/src/codecvt_error_category.cpp"
    "filesystem/src/operations.cpp"
    "filesystem/src/path_traits.cpp"
    "filesystem/src/path.cpp"
    "filesystem/src/portability.cpp"
    "filesystem/src/unique_path.cpp"
    "filesystem/src/utf8_codecvt_facet.cpp"
    "system/src/error_code.cpp"
    "system/src/error_code.cpp"
    "chrono/src/chrono.cpp"
    "chrono/src/process_cpu_clocks.cpp"
    "chrono/src/thread_clock.cpp"
    "date_time/src/gregorian/date_generators.cpp"
    "date_time/src/gregorian/greg_month.cpp"
    "date_time/src/gregorian/greg_weekday.cpp"
    "date_time/src/gregorian/gregorian_types.cpp"
    "date_time/src/posix_time/posix_time_types.cpp"
)

if(WIN32)
    set( SRCS ${SRCS} filesystem/src/windows_file_codecvt.cpp )
endif()

add_library( boost_1_67_0
             STATIC
             ${SRCS}
)

#target_link_libraries( boost_1_67_0 PUBLIC fc )
target_compile_definitions(boost_1_67_0 PUBLIC BOOST_ALL_NO_LIB)

target_include_directories( boost_1_67_0
                            PUBLIC "${CMAKE_CURRENT_SOURCE_DIR}/includes"
                            )

