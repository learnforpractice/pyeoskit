/*
 * eosapi.hpp
 *
 *  Created on: Oct 8, 2018
 *      Author: newworld
 */

#ifndef MAIN_EOSAPI_HPP_
#define MAIN_EOSAPI_HPP_

#include <vector>
#include <stdint.h>
#include <Python.h>

#include <eosio/chain/name.hpp>
#include <eosio/chain/action.hpp>
#include <eosio/chain/abi_serializer.hpp>
#include <fc/io/json.hpp>

#include "cpp_object.hpp"

using namespace std;
using namespace eosio;
using namespace eosio::chain;

uint64_t s2n_(std::string& str);
void n2s_(uint64_t n, std::string& s);

void pack_args_(string& account, uint64_t action, std::string& _args, std::string& binargs);
void unpack_args_(string& account, uint64_t action, std::string& binargs, std::string& _args );
bool clear_abi_cache_(string& account);
bool set_abi_(string& account, string& _abi);

void pack_abi_(std::string& _abi, std::string& out);

PyObject* gen_transaction_(vector<chain::action>& v, int expiration, std::string& reference_block_id);
PyObject* sign_transaction_(std::string& trx_json_to_sign, std::string& str_private_key, std::string& chain_id);
PyObject* pack_transaction_(std::string& _signed_trx, int compress);

PyObject* create_key_();
PyObject* get_public_key_(std::string& wif_key);

void from_base58_( std::string& pub_key, std::string& raw_pub_key );
void to_base58_( std::string& raw_pub_key, std::string& pub_key );

void recover_key_( string& _digest, string& _sig, string& _pub );

PyObject* unpack_transaction_(std::string& trx);

void sign_digest_(string& _priv_key, string& _digest, string& out);

uint64_t string_to_symbol_(int precision, string& str);
void set_public_key_prefix_(const string& prefix);
void get_public_key_prefix_(string& prefix);

#endif /* MAIN_EOSAPI_HPP_ */
