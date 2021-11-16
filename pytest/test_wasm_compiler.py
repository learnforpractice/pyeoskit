import os
import sys
import time
import pytest
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(lineno)d %(module)s %(message)s')
logger=logging.getLogger(__name__)
test_dir = os.path.dirname(__file__)


from pyeoskit import wasmcompiler

class Test(object):

    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass

    def test_compiler(self):
        cpp_src = '''
#include <stdint.h>
extern "C" void apply(uint64_t a, uint64_t b, uint64_t c) {

}
'''
        code = wasmcompiler.compile_cpp_src('hello', cpp_src)
        assert code

    def test_compile_with_eosio_cpp(self):
        cpp_src = r'''
#include <eosio/eosio.hpp>
using namespace eosio;

CONTRACT hello: public contract {
public:
    using contract::contract;
    
    [[eosio::action]]
    void hi( name user) {
        require_auth(user);
        print("hi", user);
    }
};
'''

        code, abi = wasmcompiler.compile_with_eosio_cpp('hello', cpp_src)
        assert code
        assert abi

    def test_go_compiler(self):
        code = '''
package main
func main() {
}
'''
        code, abi = wasmcompiler.compile_go_src('hello', code)
        assert code
