#include <eosio/net_plugin/protocol.hpp>
#include <Python.h>
#include <string>
#include <vector>
#include <fc/io/json.hpp>
#include <fc/io/raw.hpp>
#include <fc/variant.hpp>

#include "cpp_object.hpp"

using namespace std;
using namespace eosio;

template<typename T>
static void pack_cpp_object(string& msg, string& packed_message)
{
    try {
        auto _msg = fc::json::from_string(msg).as<T>();
        auto _packed_message = fc::raw::pack<T>(_msg);
        packed_message = string(_packed_message.data(), _packed_message.size());
    } FC_LOG_AND_DROP();
}

template<typename T>
static void unpack_cpp_object(string& packed_message, string& msg) {
    try {
        T _msg;
        fc::datastream<const char*> ds( packed_message.c_str(), packed_message.size() );
        fc::raw::unpack(ds, _msg);
        msg = fc::json::to_string(fc::variant(_msg));
    }FC_LOG_AND_DROP();
}

void pack_cpp_object_(int type, string& msg, string& packed_message) {
    if (type == handshake_message_type) {
        pack_cpp_object<handshake_message>(msg, packed_message);
    } else if (type == chain_size_message_type) {
        pack_cpp_object<chain_size_message>(msg, packed_message);
    } else if (type == go_away_message_type) {
        pack_cpp_object<go_away_message>(msg, packed_message);
    } else if (type == time_message_type) {
        pack_cpp_object<time_message>(msg, packed_message);
    } else if (type == notice_message_type) {
        pack_cpp_object<notice_message>(msg, packed_message);
    } else if (type == request_message_type) {
        pack_cpp_object<request_message>(msg, packed_message);
    } else if (type == sync_request_message_type ) {
        pack_cpp_object<sync_request_message>(msg, packed_message);
    } else if (type == signed_block_type) {
        pack_cpp_object<signed_block>(msg, packed_message);
    } else if (type == packed_transaction_type) {
        pack_cpp_object<packed_transaction>(msg, packed_message);
    }
}

void unpack_cpp_object_(int type, string& packed_message, string& msg) {
    if (type == handshake_message_type) {
        unpack_cpp_object<handshake_message>(packed_message, msg);
    } else if (type == chain_size_message_type) {
        unpack_cpp_object<chain_size_message>(packed_message, msg);
    } else if (type == go_away_message_type) {
        unpack_cpp_object<go_away_message>(packed_message, msg);
    } else if (type == time_message_type) {
        unpack_cpp_object<time_message>(packed_message, msg);
    } else if (type == notice_message_type) {
        unpack_cpp_object<notice_message>(packed_message, msg);
    } else if (type == request_message_type) {
        unpack_cpp_object<request_message>(packed_message, msg);
    } else if (type == sync_request_message_type ) {
        unpack_cpp_object<sync_request_message>(packed_message, msg);
    } else if (type == signed_block_type) {
        unpack_cpp_object<signed_block>(packed_message, msg);
    } else if (type == packed_transaction_type) {
        unpack_cpp_object<packed_transaction>(packed_message, msg);
    } else {
        unpack_cpp_object<eosio::select_ids<fc::sha256>>(packed_message, msg);
    }
}

