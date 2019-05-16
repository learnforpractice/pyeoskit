# cython: c_string_type=str, c_string_encoding=ascii

from cython.operator cimport dereference as deref, preincrement as inc
from libcpp.string cimport string
from libcpp.vector cimport vector
from libcpp.map cimport map
from libcpp cimport bool


from typing import Dict, Tuple, List


cdef extern from * :
    ctypedef unsigned long long int64_t

cdef extern from "wallet_.h":
    object wallet_create_(string& name);
    object wallet_save_(string& name);

    object wallet_open_(string& name);
    object wallet_set_dir_(string& path_name);
    object wallet_set_timeout_(int secs);
    object wallet_list_wallets_();
    object wallet_list_keys_(const string& name, const string& pw);
    object wallet_get_public_keys_();
    object wallet_lock_all_();
    object wallet_lock_(string& name);
    object wallet_unlock_(string& name, string& password);
    object wallet_import_key_(string& name, string& wif_key, bool save);
    object sign_transaction_(string& trx, vector[string]& _public_keys, string& chain_id);
    object sign_digest_(string& _digest, string& _public_key)

def create(string& name) :
    return wallet_create_(name)

def save(string& name) :
    return wallet_save_(name)

def open(string& name):
    return wallet_open_(name)

def set_dir(string& path_name):
    return wallet_set_dir_(path_name)

def set_timeout(secs):
    return wallet_set_timeout_(secs)

def list_wallets() -> List[bytes]:
    return wallet_list_wallets_();

def list_keys(string& name, string& psw) -> Dict[str, str]:
    return wallet_list_keys_(name, psw);

def get_public_keys():
    return wallet_get_public_keys_();

def lock_all():
    return wallet_lock_all_()

def lock(string& name):
    return wallet_lock_(name)

def unlock(string& name, string& password):
    return wallet_unlock_(name, password)

def import_key(string& name, string& wif_key, save=True):
    return wallet_import_key_(name, wif_key, save)

def sign_transaction(string& trx, _public_keys, string& chain_id):
    cdef vector[string] public_keys

    for key in _public_keys:
        public_keys.push_back(key)
    return sign_transaction_(trx, public_keys, chain_id);

def sign_digest(_digest, string& public_key):
    cdef string digest
    if isinstance(_digest, str):
        digest = bytes.fromhex(_digest)
    else:
        digest = _digest
    return sign_digest_(digest, public_key)
