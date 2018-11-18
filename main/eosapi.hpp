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

using namespace std;
using namespace eosio;
using namespace eosio::chain;

uint64_t s2n_(std::string& str);
void n2s_(uint64_t n, std::string& s);

void pack_args_(std::string& rawabi, uint64_t action, std::string& _args, std::string& binargs);
void unpack_args_( std::string& rawabi, uint64_t action, std::string& binargs, std::string& _args );
void pack_abi_(std::string& _abi, std::string& out);

PyObject* gen_transaction_(vector<chain::action>& v, int expiration, std::string& reference_block_id);
PyObject* sign_transaction_(std::string& trx_json_to_sign, std::string& str_private_key, std::string& chain_id);
PyObject* pack_transaction_(std::string& _signed_trx, int compress);

PyObject* create_key_();
PyObject* get_public_key_(std::string& wif_key);

#endif /* MAIN_EOSAPI_HPP_ */
