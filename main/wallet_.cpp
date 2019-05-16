#include <fc/variant.hpp>
#include <fc/io/json.hpp>
#include <eosio/chain/transaction.hpp>

#include <eosio/wallet_plugin/wallet_manager.hpp>

#include <Python.h>

#include "pyobject.hpp"

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

PyObject* sign_transaction_(string& _trx, vector<string>& _public_keys, string& chain_id) {
   try {
      signed_transaction trx = fc::json::from_string(_trx).as<signed_transaction>();
      flat_set<public_key_type> public_keys;

      for (auto key: _public_keys) {
         public_keys.insert(public_key_type(key));
      }

      chain::chain_id_type id(chain_id);
      trx = wm().sign_transaction(trx, public_keys, id);
      string s = fc::json::to_string(trx);
      return py_new_string(s);
   } FC_LOG_AND_DROP();
   return py_new_none();
}

PyObject* sign_digest_(string& _digest, string& _public_key) {
   try {
      chain::digest_type digest(_digest.c_str(), _digest.size());
      public_key_type public_key = public_key_type(_public_key);

      chain::signature_type sig = wm().sign_digest(digest, public_key);
      string s = string(sig);
      return py_new_string(s);
   } FC_LOG_AND_DROP();
   return py_new_none();
}

PyObject* wallet_create_(std::string& name) {
   string password = "";
   try {
      password = wm().create(name);
   } catch (fc::exception& ex) {
      elog(ex.to_detail_string());
   } catch (...) {
   }
   return py_new_string(password);
}

PyObject* wallet_open_(std::string& name) {
   try {
      wm().open(name);
   } catch (fc::exception& ex) {
      elog(ex.to_detail_string());
      return py_new_bool(false);
   } catch (...) {
      return py_new_bool(false);
   }
   return py_new_bool(true);
}

PyObject* wallet_set_dir_(std::string& path_name) {
   try {
      wm().set_dir(path_name);
   } catch (fc::exception& ex) {
      elog(ex.to_detail_string());
      return py_new_bool(false);
   } catch (...) {
      return py_new_bool(false);
   }
   return py_new_bool(true);
}

PyObject* wallet_set_timeout_(uint64_t secs) {
   try {
      wm().set_timeout(secs);
   } catch (fc::exception& ex) {
      elog(ex.to_detail_string());
      return py_new_bool(false);
   } catch (...) {
      return py_new_bool(false);
   }
   return py_new_bool(true);
}

/*
 string sign_transaction(txn,keys,id){
 #    const chain::signed_transaction& txn, const flat_set<public_key_type>&
 keys,const chain::chain_id_type& id
 }
 */

PyObject* wallet_list_wallets_() {
   PyArray arr;
   try {
      auto list = wm().list_wallets();
      for (auto it = list.begin(); it != list.end(); it++) {
         arr.append(*it);
      }
   } catch (fc::exception& ex) {
      elog(ex.to_detail_string());
   } catch (...) {
   }
   return arr.get();
}

PyObject* wallet_list_keys_(const string& name, const string& pw) {
   PyDict results;
   try {
      map<public_key_type, private_key_type> keys = wm().list_keys(name, pw);
      variant v;
      for (auto it = keys.begin(); it != keys.end(); it++) {
         //            to_variant(it.first,v);
         //            results.add(v.as_string(),key_value.second);
         string key = string(it->first);
         string value = string(it->second);
         results.add(key, value);
      }
   } catch (fc::exception& ex) {
      elog(ex.to_detail_string());
   } catch (...) {
   }
   return results.get();
}

PyObject* wallet_get_public_keys_() {
   PyArray results;

   try {
      flat_set<public_key_type> keys = wm().get_public_keys();
      //        variant v;
      for (auto it = keys.begin(); it < keys.end(); it++) {
         //                to_variant(*it,v);
         //                results.append(v.as_string());
         results.append((string)*it);
      }
   } catch (fc::exception& ex) {
      elog(ex.to_detail_string());
   } catch (...) {
   }
   return results.get();
}

PyObject* wallet_lock_all_() {
   try {
      wm().lock_all();
   } catch (fc::exception& ex) {
      elog(ex.to_detail_string());
      return py_new_bool(false);
   } catch (...) {
      return py_new_bool(false);
   }
   return py_new_bool(true);
}

PyObject* wallet_lock_(string& name) {
   try {
      wm().lock(name);
   } catch (fc::exception& ex) {
      elog(ex.to_detail_string());
      return py_new_bool(false);
   } catch (...) {
      return py_new_bool(false);
   }
   return py_new_bool(true);
}

PyObject* wallet_unlock_(string& name, string& password) {
   try {
      wm().unlock(name, password);
   } catch (fc::exception& ex) {
      elog(ex.to_detail_string());
      return py_new_bool(false);
   } catch (...) {
      return py_new_bool(false);
   }
   return py_new_bool(true);
}

PyObject* wallet_import_key_(string& name, string& wif_key, bool save) {
   try {
      wm().import_key(name, wif_key, save);
   } catch (fc::exception& ex) {
      elog(ex.to_detail_string());
      return py_new_bool(false);
   } catch (...) {
      return py_new_bool(false);
   }
   return py_new_bool(true);
}

PyObject* wallet_save_(string& name) {
   try {
      wm().save_wallet(name);
   } catch (fc::exception& ex) {
      elog(ex.to_detail_string());
      return py_new_bool(false);
   } catch (...) {
      return py_new_bool(false);
   }
   return py_new_bool(true);
}
