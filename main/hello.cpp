#include "hello.hpp"

extern "C" {
   PyObject* PyInit_wallet();
   PyObject* PyInit__eosapi();
}

PyObject* init_wallet() {
   printf("+++++init wallet.\n");
   return PyInit_wallet();
}

PyObject* init__eosapi() {
   return PyInit__eosapi();
}
