/*
 * hello.hpp
 *
 *  Created on: Oct 8, 2018
 *      Author: newworld
 */

#ifndef MAIN_HELLO_HPP_
#define MAIN_HELLO_HPP_

#include <Python.h>

PyObject* init_wallet();
PyObject* init__eosapi();

extern "C" {
   PyObject* PyInit_wallet();
   PyObject* PyInit__eosapi();
   PyObject* PyInit_pyobject();
}

#endif /* MAIN_HELLO_HPP_ */
