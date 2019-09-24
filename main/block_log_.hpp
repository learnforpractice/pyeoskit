#pragma once
#include <string>
//#include <micropython/mpeoslib.h>
#include <Python.h>

using namespace std;

void block_log_parse_transactions_(string& path, int start_block, int end_block);
void block_log_parse_raw_transactions_(string& path, int start, int end);

int block_on_action(int block, PyObject* trx);
PyObject* block_log_get_block_(string& path, int block_num);
