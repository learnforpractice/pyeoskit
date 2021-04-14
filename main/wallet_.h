#ifndef WALLET_HPP_
#define WALLET_HPP_

#include <Python.h>
#include <string>
#include <vector>

#include <eosio/chain/transaction.hpp>
using namespace std;

void sign_transaction(eosio::chain::signed_transaction &trx);

/*
 string sign_transaction(txn,keys,id){
 #    const chain::signed_transaction& txn, const flat_set<public_key_type>&
 keys,const chain::chain_id_type& id
 }
 */

string wallet_create_(std::string &name);
bool wallet_open_(std::string &name);
bool wallet_save_(std::string& name);
bool wallet_set_dir_(std::string &path_name);

bool wallet_set_timeout_(uint64_t secs);
string wallet_list_wallets_();
string wallet_list_keys_(const std::string& name, const std::string& pw);
string wallet_get_public_keys_();
bool wallet_lock_all_();
bool wallet_lock_(std::string &name);
bool wallet_unlock_(std::string &name, std::string &password);
bool wallet_import_key_(std::string &name, std::string &wif_key, bool save);
bool wallet_remove_key_(string& name, string& password, const string& pub_key);

string sign_transaction_(string& trx, vector<string>& _public_keys, string& chain_id);
string sign_digest_(string& _digest, string& _public_key);

#endif
