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
    char* wallet_import_(char* name, char* priv)
    char* wallet_get_public_keys_()

    int64_t transaction_new_(int64_t expiration, char* refBlock, char* chainId);
    void transaction_free_(int64_t _index);
    char* transaction_add_action_(int64_t idx, char* account, char* name, char* data, char* permissions);
    char* transaction_sign_(int64_t idx, char* pub);
    char* transaction_pack_(int64_t idx);

cdef object convert(char *_ret):
    ret = <object>_ret
    free(_ret)
    return ret

def init():
    init_()

def say_hello(char* name):
    say_hello_(name)

def wallet_import(char* name, char* priv):
    cdef char *ret
    ret = wallet_import_(name, priv)
    return convert(ret)

def transaction_new(int64_t expiration, char* refBlock, char* chainId):
    return transaction_new_(expiration, refBlock, chainId)

def transaction_free(int64_t _index):
    transaction_free_(_index)

def transaction_add_action(int64_t idx, char* account, char* name, char* data, char* permissions):
    cdef char *ret
    ret = transaction_add_action_(idx, account, name, data, permissions)
    return convert(ret)

def transaction_sign(int64_t idx, char* pub):
    cdef char *ret
    ret = transaction_sign_(idx, pub)
    return convert(ret)

# char* transaction_pack_(int64_t idx);
def transaction_pack(int64_t idx):
    cdef char *ret
    ret = transaction_pack_(idx)
    return convert(ret)

# char* wallet_get_public_keys_()
def wallet_get_public_keys():
    cdef char *ret
    ret = wallet_get_public_keys_()
    return convert(ret)

