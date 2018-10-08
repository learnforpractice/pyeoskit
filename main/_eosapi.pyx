# cython: c_string_type=str, c_string_encoding=ascii

from cython.operator cimport dereference as deref, preincrement as inc
from libcpp.string cimport string
from libcpp.vector cimport vector
from libcpp.map cimport map
from libcpp cimport bool

import json

cdef extern from * :
    ctypedef long long int64_t
    ctypedef unsigned long long uint64_t

cdef extern from "eosapi.hpp":
    void pack_args_(string& rawabi, uint64_t action, string& _args, string& binargs)
    void unpack_args_(string& rawabi, uint64_t action, string& binargs, string& _args)
    uint64_t s2n_(string& s);
    void n2s_(uint64_t n, string& s);

def N(string& s):
    return s2n_(s)

def s2n(string& s):
    return s2n_(s)

def n2s(uint64_t n):
    cdef string s
    n2s_(n, s)
    return s

def pack_args(string& rawabi, action, _args):
    cdef string binargs
    cdef string args
    args = json.dumps(_args)
    pack_args_(rawabi, N(action), args, binargs)
    return <bytes>binargs

def unpack_args(string& rawabi, action, string& binargs):
    cdef string _args
    unpack_args_(rawabi, N(action), binargs, _args)
    return json.loads(_args)
