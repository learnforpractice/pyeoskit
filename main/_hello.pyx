cdef extern from "hello.hpp":
    object PyInit_wallet();
    object PyInit__eosapi();
    object PyInit_pyobject();
    
wallet = PyInit_wallet()
_eosapi = PyInit__eosapi()
PyInit_pyobject()

cpdef void hello(str strArg):
    "Prints back 'Hello <param>', for example example: hello.hello('you')"
    print("Hello, {}! :)".format(strArg))

cpdef long size():
    "Returns elevation of Nevado Sajama."
    return 21463L

