# cython: c_string_type=str, c_string_encoding=utf8

from cython.operator cimport dereference as deref, preincrement as inc
from cpython.bytes cimport PyBytes_AS_STRING
from libcpp.string cimport string
from libcpp.vector cimport vector
from libcpp.map cimport map
from libcpp cimport bool
from libc.stdlib cimport malloc, free


cdef extern from * :
    ctypedef long long int64_t

cdef extern from "<Python.h>":
    ctypedef long long PyLongObject

    object PyBytes_FromStringAndSize(const char* str, int size)
    int _PyLong_AsByteArray(PyLongObject* v, unsigned char* bytes, size_t n, int little_endian, int is_signed)

cdef extern from "libuuoskit.h" nogil:
    void init_();
    void say_hello_(char* name)

cdef object convert(char *_ret):
    ret = <object>_ret
    free(_ret)
    return ret

def init():
    init_()

def say_hello(char* name):
    say_hello_(name)

