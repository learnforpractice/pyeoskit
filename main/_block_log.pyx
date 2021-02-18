# cython: c_string_type=str, c_string_encoding=utf8
from libcpp.string cimport string
from libcpp cimport bool
import os
import sys
import traceback

cdef extern from * :
    ctypedef long long int64_t
    ctypedef unsigned long long uint64_t
    ctypedef unsigned int uint32_t

cdef extern from "block_log_.hpp":
    void *block_log_new(string& path);
    void block_log_free(void *block_log_ptr);

    unsigned int block_log_get_first_block_num_(void *block_log_ptr);
    object block_log_read_block_by_num_(void *block_log_ptr, unsigned int block_num);

    object block_log_get_head_block_(void *block_log_ptr);
    bool block_log_parse_transactions_(void *block_log_ptr, int start_block, int end_block);
    void block_log_get_transactions_(void *block_log_ptr, int block_num);

    void block_log_parse_actions_(void *block_log_ptr, int start, int end)
    void block_log_parse_raw_actions_(void *block_log_ptr, int start, int end)

    object block_log_get_block_(void *block_log_ptr, int block_num);

    bool block_log_append_block_(void *block_log_ptr, string& _block)

    void block_log_repair_log(string& data_dir, uint32_t truncate_at_block, string& backup_dir)


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
    cdef string c_block_log_path

    def __cinit__(self, string& path):
        self.c_block_log_ptr = block_log_new(path)
        assert self.c_block_log_ptr, 'bad block log ptr'
        self.c_block_log_path = path

    def __dealloc__(self):
        block_log_free(self.c_block_log_ptr)
        self.c_block_log_ptr = <void *>0

    def free(self):
        block_log_free(self.c_block_log_ptr)
        self.c_block_log_ptr = <void *>0

    def get_first_block_num(self):
        return block_log_get_first_block_num_(self.c_block_log_ptr)

    def get_head_block_num(self):
        first_block_num = self.get_first_block_num()
        block_log_path = self.c_block_log_path
        blocks_index_path = os.path.join(block_log_path, 'blocks.index')
        block_count = os.path.getsize(blocks_index_path)//8
        return first_block_num + block_count - 1

    def read_block_by_num(self, block_num):
        return block_log_read_block_by_num_(self.c_block_log_ptr, block_num)

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

    def append_block(self, block):
        block_log_append_block_(self.c_block_log_ptr, block)

    def repair_block(self, uint32_t truncate_at_block):
        cdef string backup_dir
        block_log_repair_log(self.c_block_log_path, truncate_at_block, backup_dir)
        return backup_dir
