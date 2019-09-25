# cython: c_string_type=str, c_string_encoding=ascii
from libcpp.string cimport string
from libcpp cimport bool
import os
import sys
import traceback

cdef extern from "block_log_.hpp":
    void *block_log_new(string& path);
    void block_log_free(void *block_log_ptr);
    unsigned int block_log_get_first_block_num_(void *block_log_ptr);
    object block_log_get_head_block_(void *block_log_ptr);
    bool block_log_parse_transactions_(void *block_log_ptr, int start_block, int end_block);
    void block_log_get_transactions_(void *block_log_ptr, int block_num);

    void block_log_parse_actions_(void *block_log_ptr, int start, int end)
    void block_log_parse_raw_actions_(void *block_log_ptr, int start, int end)

    object block_log_get_block_(void *block_log_ptr, int block_num);

g_transaction_callback = None
cdef extern int block_log_on_transaction(int block, object trx):
    global g_transaction_callback
    if g_transaction_callback:
        try:
            g_transaction_callback(block, trx)
        except:
            traceback.print_exc()
            return 0
    return 1

g_raw_action_cb = None
cdef extern int block_log_on_raw_action(int block, string& act):
    global g_raw_action_cb
    if g_raw_action_cb:
        try:
            g_raw_action_cb(block, <bytes>(&act[0]))
        except:
            traceback.print_exc()
            return 0
    return 1

g_action_cb = None
cdef extern int block_log_on_action(int block, string& act):
    global g_action_cb
    if g_action_cb:
        try:
            g_action_cb(block, <bytes>(&act[0]))
        except:
            traceback.print_exc()
            return 0
    return 1

cdef class BlockParser:
    cdef void *c_block_log_ptr

    def __cinit__(self, string& path):
        self.c_block_log_ptr = block_log_new(path)

    def __dealloc__(self):
        block_log_free(self.c_block_log_ptr)
        self.c_block_log_ptr = <void *>0

    def free(self):
        block_log_free(self.c_block_log_ptr)
        self.c_block_log_ptr = <void *>0

    def get_first_block_num(self, ):
        return block_log_get_first_block_num_(self.c_block_log_ptr)

    def get_head_block(self):
        return block_log_get_head_block_(self.c_block_log_ptr)

    def on_transaction(self, block_num, trx):
        print(block_num, trx)

    def parse_transactions(self, int start_block, int end_block):
        global g_transaction_callback
        g_transaction_callback = self.on_transaction
        return block_log_parse_transactions_(self.c_block_log_ptr, start_block, end_block)

    def on_action(self, block_num, trx):
        print(block_num, trx)

    def on_raw_action(self, block_num, trx):
        print(block_num, trx)

    def parse_actions(self, int start_block, int end_block):
        global g_action_cb
        g_action_cb = self.on_action
        return block_log_parse_actions_(self.c_block_log_ptr, start_block, end_block)

    def parse_raw_actions(self, int start_block, int end_block):
        global g_raw_action_cb
        g_raw_action_cb = self.on_raw_action
        return block_log_parse_raw_actions_(self.c_block_log_ptr, start_block, end_block)
