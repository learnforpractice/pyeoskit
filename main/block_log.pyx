# cython: c_string_type=str, c_string_encoding=ascii
from libcpp.string cimport string
from libcpp cimport bool
import os
import sys
import traceback

cdef extern from "block_log_.hpp":
    void block_log_parse_transactions_(string& path, int start_block, int end_block)
    void block_log_parse_raw_transactions_(string& path, int start, int end);
    object block_log_get_block_(string& path, int block_num);

callback = None
cdef extern int block_on_action(int block, object trx):
    global callback
    if callback:
        try:
            callback(block, trx)
        except:
            traceback.print_exc()
            return 0
    return 1

def  parse_transactions(string& path, start, end, cb):
    global callback
    callback = cb
    block_log_parse_transactions_(path, start, end)

raw_action_cb = None
cdef extern int block_on_raw_action(int block, string act):
    global raw_action_cb
    if raw_action_cb:
        try:
            raw_action_cb(block, <bytes>act)
        except:
            traceback.print_exc()
            return 0
    return 1

def parse_raw_transactions(string& path, start, end, cb):
    global raw_action_cb
    raw_action_cb = cb
    block_log_parse_raw_transactions_(path, start, end);

def get_block(string& path, int block_num):
    return block_log_get_block_(path, block_num)
