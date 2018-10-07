cdef extern from "wallet_.h":
    object init_wallet()

wallet = init_wallet()

cpdef void hello(str strArg):
    "Prints back 'Hello <param>', for example example: hello.hello('you')"
    print("Hello, {}! :)".format(strArg))

cpdef long size():
    "Returns elevation of Nevado Sajama."
    return 21463L

