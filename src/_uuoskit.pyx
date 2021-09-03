# cython: c_string_type=str, c_string_encoding=ascii

from cython.operator cimport dereference as deref, preincrement as inc
from cpython.bytes cimport PyBytes_AS_STRING
from libcpp.string cimport string
from libcpp.vector cimport vector
from libcpp.map cimport map
from libcpp cimport bool
from libc.stdlib cimport malloc, free


cdef extern from * :
    ctypedef long long int64_t
    ctypedef unsigned long long uint64_t

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
    char* abiserializer_set_contract_abi_(char* account, char* abi, int length);
    char* abiserializer_pack_action_args_(char* contractName, char* actionName, char* args, int args_len);
    char* abiserializer_unpack_action_args_(char* contractName, char* actionName, char* args);

    char* abiserializer_pack_abi_type_(char* contractName, char* actionName, char* args, int args_len);
    char* abiserializer_unpack_abi_type_(char* contractName, char* actionName, char* args);

    uint64_t s2n_(char* s);
    char* n2s_(uint64_t n);

    uint64_t sym2n_(char* symbol, uint64_t precision)

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

#     char* abiserializer_set_contract_abi_(char* account, char* abi, int length);
def abiserializer_set_contract_abi(char* account, abi):
    cdef char *ret
    ret = abiserializer_set_contract_abi_(account, abi, len(abi))
    return convert(ret)

#    char* abiserializer_pack_action_args_(char* contractName, char* actionName, char* args, int args_len);
def abiserializer_pack_action_args(char* contractName, char* actionName, args):
    cdef char *ret
    print("++++++++abiserializer_pack_action_args:", contractName, actionName)
    ret = abiserializer_pack_action_args_(contractName, actionName, args, len(args))
    return convert(ret)

#    char* abiserializer_unpack_action_args_(char* contractName, char* actionName, char* args);
def abiserializer_unpack_action_args(char* contractName, char* actionName, char* args):
    cdef char *ret
    ret = abiserializer_unpack_action_args_(contractName, actionName, args)
    return convert(ret)

#char* abiserializer_pack_abi_type_(char* contractName, char* actionName, char* args, int args_len);
def abiserializer_pack_abi_type(char* contractName, char* actionName, args):
    cdef char *ret
    ret = abiserializer_pack_abi_type_(contractName, actionName, args, len(args))
    return convert(ret)

#char* abiserializer_unpack_abi_type_(char* contractName, char* actionName, char* args);
def abiserializer_unpack_abi_type(char* contractName, char* actionName, char* args):
    cdef char *ret
    ret = abiserializer_unpack_abi_type_(contractName, actionName, args)
    return convert(ret)

#uint64_t s2n(char* s);
def s2n(char* s):
    return s2n_(s)

#    char* n2s(uint64_t n);
def n2s(uint64_t n):
    cdef char *ret
    ret = n2s_(n)
    return convert(ret)

#symbol to uint64_t
def sym2n(char* symbol, uint64_t precision):
    return sym2n_(symbol, precision)

def n2sym(n):
    sym = int.to_bytes(n, 8, 'little')
    return f'{sym[0]},'+ sym[1:].rstrip(b'\x00').decode()
