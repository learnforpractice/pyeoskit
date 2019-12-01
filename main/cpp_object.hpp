#pragma once
#include <string>
using namespace std;

void pack_cpp_object_(int type, string& msg, string& packed_message);
void unpack_cpp_object_(int type, string& packed_message, string& msg);

enum {
    handshake_message_type,
    chain_size_message_type,
    go_away_message_type,
    time_message_type,
    notice_message_type,
    request_message_type,
    sync_request_message_type,
    signed_block_type,         // which = 7
    packed_transaction_type
};
