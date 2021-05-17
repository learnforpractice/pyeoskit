# cython: c_string_type=str, c_string_encoding=utf8

from cython.operator cimport dereference as deref, preincrement as inc
from libcpp.string cimport string
from libcpp.vector cimport vector
from libcpp.map cimport map
from libcpp cimport bool

import json
from uuoskit import config

cdef extern from * :
    ctypedef long long int64_t
    ctypedef unsigned long long uint64_t
    ctypedef int __uint128_t

cdef extern from "uuosapi.hpp":
    void *malloc(size_t size);

    void pack_cpp_object_(int _type, string& msg, string& packed_message)
    void unpack_cpp_object_(int _type, string& packed_message, string& msg)

    bool pack_args_(string& account, uint64_t action, string& _args, string& binargs)
    bool unpack_args_(string& account, uint64_t action, string& binargs, string& _args)
    bool clear_abi_cache_(string& account);
    bool is_abi_cached_(string& account);

    void pack_abi_type_(string& account, string& struct_name, string& _args, string& _binargs);
    void unpack_abi_type_(string& account, string& struct_name, string& _binargs, string& _args );

    bool set_abi_(string& account, string& _abi);

    void pack_abi_(string& _abi, string& out);
    void unpack_abi_(string& _packed_abi, string& out);

    uint64_t s2n_(string& s);
    void n2s_(uint64_t n, string& s);

    void memcpy(char* dst, char* src, size_t len)

    cdef cppclass permission_level:
        permission_level()
        uint64_t    actor
        uint64_t permission

    cdef cppclass action:
        action()
        uint64_t                    account
        uint64_t                    name
        vector[permission_level]    authorization
        vector[char]                data

    string gen_transaction_(vector[action]& v, int expiration, string& reference_block_id);
    string sign_transaction_(string& trx_json_to_sign, string& str_private_key, string& chain_id);
    string pack_transaction_(string& _signed_trx, int compress)
    string unpack_transaction_(string& trx)

    bool create_key_(string& pub, string& priv)
    string get_public_key_(string& wif_key)

    void from_base58_( string& pub_key, string& raw_pub_key );
    void to_base58_( string& raw_pub_key, string& pub_key );

    void recover_key_( string& _digest, string& _sig, string& _pub );
    void sign_digest_(string& _priv_key, string& _digest, string& out);

    uint64_t string_to_symbol_(int precision, string& str);
    void set_public_key_prefix_(const string& prefix);
    void get_public_key_prefix_(string& prefix);

    size_t micropython_compile_src(const char *src, char *output, size_t output_size, const char *source_file);

    void get_last_error_(string& error)
    void set_last_error_(const string& error);

def N(string& s):
    return s2n_(s)

def s2n(string& s):
    return s2n_(s)

def n2s(uint64_t n):
    cdef string s
    n2s_(n, s)
    return s

def string_to_symbol(int precision, string& _str):
    return string_to_symbol_(precision, _str)

def pack_args(string& account, action, string& args):
    cdef string binargs
    success = pack_args_(account, N(action), args, binargs)
    return success, <bytes>binargs

def unpack_args(string& account, action, string& binargs):
    cdef string args
    success = unpack_args_(account, N(action), binargs, args)
    return success, args

def pack_abi_type(string& account, string& struct_name, string& _args):
    cdef string _binargs
    pack_abi_type_(account, struct_name, _args, _binargs)
    return <bytes>_binargs

def unpack_abi_type(string& account, string& struct_name, string& _binargs):
    cdef string _args
    unpack_abi_type_(account, struct_name, _binargs, _args)
    return <bytes>_args

def clear_abi_cache(string& account):
    return clear_abi_cache_(account)

def is_abi_cached(string& account):
    return is_abi_cached_(account)

def set_abi(string& account, string& abi):
    return set_abi_(account, abi)

def pack_abi(string& _abi):
    cdef string out
    pack_abi_(_abi, out)
    return <bytes>out

def unpack_abi(string& _packed_abi):
    cdef string out
    unpack_abi_(_packed_abi, out)
    return out

def gen_transaction(actions, int expiration, string& reference_block_id):
    cdef vector[action] v
    cdef action act
    cdef permission_level per
    cdef vector[permission_level] pers

    v = vector[action]()
    for a in actions:
        act = action()
        account = a[0]
        action_name = a[1]
        act.account = s2n(account)
        act.name = s2n(action_name)
        pers = vector[permission_level]()
        for auth in a[3]:
            per = permission_level()
            per.actor = s2n(auth)
            per.permission = s2n(a[3][auth])
            pers.push_back(per)
        act.authorization = pers

        args = a[2]
#        if isinstance(args, dict):
#            args = pack_args(account, action_name, args)
        act.data.resize(0)
        act.data.resize(len(args))
        memcpy(act.data.data(), args, len(args))
        v.push_back(act)

    return gen_transaction_(v, expiration, reference_block_id)

def sign_transaction(string& trx_json_to_sign, string& str_private_key, string& chain_id):
    return sign_transaction_(trx_json_to_sign, str_private_key, chain_id)

def pack_transaction(string& _signed_trx, int compress):
    return pack_transaction_(_signed_trx, compress)

def unpack_transaction(string& trx):
    return unpack_transaction_(trx)

def create_key():
    cdef string pub
    cdef string priv
    create_key_(pub, priv)
    return {'public': pub, 'private': priv}

def get_public_key(string& wif_key):
    return get_public_key_(wif_key)

def from_base58(string& pub_key):
    cdef string raw_pub_key
    from_base58_(pub_key, raw_pub_key)
    return <bytes>raw_pub_key

def to_base58(string& raw_pub_key):
    cdef string pub_key
    to_base58_(raw_pub_key, pub_key)
    return pub_key

def recover_key(string& digest, string& sig):
    cdef string pub
    recover_key_( digest, sig, pub );
    return pub

def pack_cpp_object(int _type, string& msg):
    cdef string packed_message
    pack_cpp_object_(_type, msg, packed_message)
    return <bytes>packed_message

def unpack_cpp_object(int _type, string& packed_message):
    cdef string msg
    unpack_cpp_object_(_type, packed_message, msg)
    return <bytes>msg

def sign_digest(string& _priv_key, string& _digest):
    cdef string out
    sign_digest_(_priv_key, _digest, out)
    return out

def set_public_key_prefix(const string& prefix):
    set_public_key_prefix_(prefix)

def get_public_key_prefix():
    cdef string prefix
    get_public_key_prefix_(prefix)
    return prefix

def compile_py(file_name, src, src_type = 0):
    cdef vector[char] output
    cdef size_t size

    output.resize(len(src) * 2 + 128)
    size = micropython_compile_src(src, output.data(), output.size(), f"{file_name}.py")
    if not size:
        return None
    return <bytes>string(output.data(), size)

def get_last_error():
    cdef string error
    get_last_error_(error)
    return error

def set_last_error(const string& error):
    set_last_error_(error)

