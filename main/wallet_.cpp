#include <fc/variant.hpp>
#include <fc/io/json.hpp>
#include <eosio/chain/transaction.hpp>

#include <eosio/wallet_plugin/wallet_manager.hpp>

#include <Python.h>

#include <vector>

#include "pyobject.hpp"

#include "macro.hpp"

using namespace std;
using namespace eosio;
using namespace eosio::chain;
using namespace eosio::wallet;

wallet_manager& wm() {
   static wallet_manager* wm = nullptr;
   if (!wm) {
      wm = new wallet_manager();
   }
   return *wm;
}

string sign_transaction_(string& _trx, vector<string>& _public_keys, string& chain_id) {
   try {
      signed_transaction trx = fc::json::from_string(_trx).as<signed_transaction>();
      flat_set<public_key_type> public_keys;

      for (auto key: _public_keys) {
         public_keys.insert(public_key_type(key));
      }

      chain::chain_id_type id(chain_id);
      trx = wm().sign_transaction(trx, public_keys, id);
      return fc::json::to_string(trx);
   } FC_LOG_AND_DROP();
   return "";
}

string sign_raw_transaction_(vector<char>& _trx, vector<string>& _public_keys, string& chain_id) {
   try {
      signed_transaction trx;
      try {
         transaction t = fc::raw::unpack<transaction>(_trx);
         vector<signature_type> signatures;
         vector<bytes> context_free_data;
         trx = signed_transaction(std::move(t), signatures, context_free_data);
      } catch (...) {
         trx = fc::raw::unpack<signed_transaction>(_trx);
      }

      flat_set<public_key_type> public_keys;

      for (auto key: _public_keys) {
         public_keys.insert(public_key_type(key));
      }

      chain::chain_id_type id(chain_id);
      trx = wm().sign_transaction(trx, public_keys, id);
      return fc::json::to_string(trx);
   } FC_LOG_AND_DROP();
   return "";
}

string sign_digest_(string& _digest, string& _public_key) {
   try {
      chain::digest_type digest(_digest.c_str(), _digest.size());
      public_key_type public_key = public_key_type(_public_key);

      chain::signature_type sig = wm().sign_digest(digest, public_key);
      return string(sig);
   } FC_LOG_AND_DROP();
   return "";
}

string wallet_create_(std::string& name) {
   string password = "";
   try {
      return wm().create(name);
   } FC_LOG_AND_DROP();
   return "";
}

bool wallet_open_(std::string& name) {
   try {
      wm().open(name);
      return true;
   } FC_LOG_AND_DROP();
   return false;
}

bool wallet_save_(string& name) {
   try {
      wm().save_wallet(name);
      return true;
   } FC_LOG_AND_DROP();
   return false;
}

bool wallet_set_dir_(std::string& path_name) {
   try {
      wm().set_dir(path_name);
      return true;
   } FC_LOG_AND_DROP();
   return false;
}

bool wallet_set_timeout_(uint64_t secs) {
   try {
      wm().set_timeout(secs);
      return false;
   } FC_LOG_AND_DROP();
   return true;
}

/*
 string sign_transaction(txn,keys,id){
 #    const chain::signed_transaction& txn, const flat_set<public_key_type>&
 keys,const chain::chain_id_type& id
 }
 */

string wallet_list_wallets_() {
   try {
      std::vector<string> wallets;
      auto list = wm().list_wallets();
      for (auto it = list.begin(); it != list.end(); it++) {
         wallets.push_back(*it);
      }
      return fc::json::to_string(wallets);
   } FC_LOG_AND_DROP();
   return "";
}

string wallet_list_keys_(const string& name, const string& pw) {
   try {
      fc::mutable_variant_object v;
      map<public_key_type, private_key_type> keys = wm().list_keys(name, pw);
      for (auto it = keys.begin(); it != keys.end(); it++) {
         string key = string(it->first);
         string value = string(it->second);
         v.set(key, value);
      }
      return fc::json::to_string(v);
   } FC_LOG_AND_DROP();
   return "";
}

string wallet_get_public_keys_() {
   try {
      std::vector<string> pub_keys;
      flat_set<public_key_type> keys = wm().get_public_keys();
      for (auto it = keys.begin(); it < keys.end(); it++) {
         pub_keys.push_back((string)*it);
      }
      return fc::json::to_string(pub_keys);
   } FC_LOG_AND_DROP();
   return "";
}

bool wallet_lock_all_() {
   try {
      wm().lock_all();
      return true;
   } FC_LOG_AND_DROP();
   return false;
}

bool wallet_lock_(string& name) {
   try {
      wm().lock(name);
      return true;
   } FC_LOG_AND_DROP();
   return false;
}

bool wallet_unlock_(string& name, string& password) {
   try {
      wm().unlock(name, password);
      return true;
   } FC_LOG_AND_DROP();
   return false;
}

bool wallet_import_key_(string& name, string& wif_key, bool save) {
   try {
      wm().import_key(name, wif_key, save);
      return true;
   } FC_LOG_AND_DROP();
   return false;
}

bool wallet_remove_key_(string& name, string& password, const string& pub_key) {
   try {
      wm().remove_key(name, password, pub_key);
      return true;
   } FC_LOG_AND_DROP();
   return false;
}
