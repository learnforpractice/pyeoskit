#pragma once
#include <string>
//#include <micropython/mpeoslib.h>
#include <Python.h>

using namespace std;

void *block_log_new(string& path);
void block_log_free(void *block_log_ptr);
uint32_t block_log_get_first_block_num_(void *block_log_ptr);
PyObject* block_log_read_block_by_num_(void *block_log_ptr, uint32_t block_num);
PyObject* block_log_get_head_block_(void *block_log_ptr);
bool block_log_parse_transactions_(void *block_log_ptr, int start_block, int end_block);
void block_log_get_transactions_(void *block_log_ptr, int block_num);

void block_log_parse_actions_(void *block_log_ptr, int start, int end);
void block_log_parse_raw_actions_(void *block_log_ptr, int start, int end);

PyObject* block_log_get_block_(void *block_log_ptr, int block_num);
