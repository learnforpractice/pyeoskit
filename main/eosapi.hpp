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

#include <eosio/chain/name.hpp>
#include <eosio/chain/abi_serializer.hpp>
#include <fc/io/json.hpp>

using namespace std;
using namespace eosio;
using namespace eosio::chain;


void pack_args(string& rawabi, uint64_t code, uint64_t action, string& _args, bytes& binargs);
void unpack_args( string& rawabi, uint64_t code, uint64_t action, string& binargs, string& _args );


#endif /* MAIN_EOSAPI_HPP_ */
