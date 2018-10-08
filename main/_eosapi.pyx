# cython: c_string_type=str, c_string_encoding=ascii

from cython.operator cimport dereference as deref, preincrement as inc
from libcpp.string cimport string
from libcpp.vector cimport vector
from libcpp.map cimport map
from libcpp cimport bool


cdef extern from * :
    ctypedef long long int64_t
    ctypedef unsigned long long uint64_t

cdef extern from "eosapi.hpp":
    void pack_args(string& rawabi, uint64_t code, uint64_t action, string& _args, string& binargs);
    void unpack_args( string& rawabi, uint64_t code, uint64_t action, string& binargs, string& _args );
