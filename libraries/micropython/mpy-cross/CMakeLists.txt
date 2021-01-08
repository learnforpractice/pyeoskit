
set(SRC
main.c
../py/modarray.c
../py/nlrpowerpc.c
../py/emitcommon.c
../py/objnone.c
../py/frozenmod.c
../py/emitnx64.c
../py/reader.c
../py/modmicropython.c
../py/objreversed.c
../py/nlrthumb.c
../py/nlr.c
../py/profile.c
../py/nativeglue.c
../py/objgenerator.c
../py/malloc.c
../py/ringbuf.c
../py/objzip.c
../py/objnamedtuple.c
../py/objproperty.c
../py/map.c
../py/objobject.c
../py/builtinimport.c
../py/objint_mpz.c
../py/emitinlinextensa.c
../py/objtype.c
../py/bc.c
../py/emitbc.c
../py/asmarm.c
../py/pystack.c
../py/objboundmeth.c
../py/objstr.c
../py/objtuple.c
../py/scheduler.c
../py/objfun.c
../py/showbc.c
../py/parse.c
../py/asmthumb.c
../py/objdeque.c
../py/asmxtensa.c
../py/objmodule.c
../py/objarray.c
../py/modbuiltins.c
../py/gc.c
../py/objint_longlong.c
../py/objfilter.c
../py/obj.c
../py/objpolyiter.c
../py/stream.c
../py/modthread.c
../py/objset.c
../py/objcell.c
../py/nlrx64.c
../py/asmx86.c
../py/modsys.c
../py/emitinlinethumb.c
../py/modio.c
../py/objbool.c
../py/runtime.c
../py/parsenum.c
../py/warning.c
../py/modstruct.c
../py/parsenumbase.c
../py/builtinhelp.c
../py/unicode.c
../py/emitnxtensa.c
../py/mpprint.c
../py/compile.c
../py/formatfloat.c
../py/emitnthumb.c
../py/qstr.c
../py/runtime_utils.c
../py/modmath.c
../py/mpz.c
../py/objgetitemiter.c
../py/sequence.c
../py/objdict.c
../py/nlrsetjmp.c
../py/opmethods.c
../py/nlrx86.c
../py/objslice.c
../py/objstringio.c
../py/asmx64.c
../py/objlist.c
../py/smallint.c
../py/builtinevex.c
../py/modcmath.c
../py/nlrxtensa.c
../py/modgc.c
../py/objmap.c
../py/repl.c
../py/lexer.c
../py/modcollections.c
../py/asmbase.c
../py/emitglue.c
../py/emitnx86.c
../py/objcomplex.c
../py/persistentcode.c
../py/vm.c
../py/objattrtuple.c
../py/objfloat.c
../py/objstrunicode.c
../py/stackctrl.c
../py/scope.c
../py/mpstate.c
../py/objsingleton.c
../py/objrange.c
../py/argcheck.c
../py/objexcept.c
../py/binary.c
../py/emitnxtensawin.c
../py/pairheap.c
../py/objint.c
../py/moduerrno.c
../py/objclosure.c
../py/vstr.c
../py/emitnarm.c
../py/objenumerate.c
gccollect.c
../lib/utils/gchelper_generic.c
)

if(WIN32)
    set(SRC ${SRC} ../ports/windows/fmode.c)
endif()

add_library(micropython ${SRC})

if (APPLE)
    target_compile_options(micropython PRIVATE -DBUILD_LIB )
elseif(WIN32)
    target_compile_options(micropython PRIVATE -DBUILD_LIB)
else()
    target_compile_options(micropython PRIVATE -DBUILD_LIB -fPIC)
endif()

set(INCS    ${CMAKE_CURRENT_SOURCE_DIR}/extmod/uuosio/intx/include
    ${CMAKE_CURRENT_SOURCE_DIR}/extmod/uuosio/include
    ${CMAKE_CURRENT_SOURCE_DIR}
    ${CMAKE_CURRENT_SOURCE_DIR}/..
)

if(WIN32)
    set(INCS ${INCS} ${CMAKE_CURRENT_SOURCE_DIR}/../ports/windows/msvc)
endif()

target_include_directories(micropython PRIVATE ${INCS})

# add_executable(mpy-cross ${SRC})

# #target_compile_options(micropython PRIVATE -DMAX_MEMORY_SIZE=131072 ${PYTHON_FLAGS}) # -Wno-visibility)

# target_include_directories(mpy-cross
#    PRIVATE
#    ${CMAKE_CURRENT_SOURCE_DIR}/extmod/uuosio/intx/include
#    ${CMAKE_CURRENT_SOURCE_DIR}/extmod/uuosio/include
#    ${CMAKE_CURRENT_SOURCE_DIR}
#    ${CMAKE_CURRENT_SOURCE_DIR}/..
# )


