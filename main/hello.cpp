#include "hello.hpp"

extern "C" {
   PyObject* PyInit_wallet();
   PyObject* PyInit__eosapi();
   PyObject* PyInit_block_log();
}

PyObject* init_wallet() {
   printf("+++++init wallet.\n");
   return PyInit_wallet();
}

PyObject* init__eosapi() {
   return PyInit__eosapi();
}

PyObject* init_block_log() {
   return PyInit_block_log();
}
