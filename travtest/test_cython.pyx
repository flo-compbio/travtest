"""Cython test module."""

#cdef extern from "math.h":
#    long double ABS "fabsl" (long double x)
#    long double NAN "nanl" (const char* tagp)

cimport cython

def get_hello_world(int n):
    cdef int i
    l = []
    for i in range(n):
        l.append('Hello World')
    return l
