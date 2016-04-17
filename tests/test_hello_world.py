from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *

from travtest import test_cython

def test_print():
    l = test_cython.get_hello_world(2)
    assert tuple(l) == ('Hello World', 'Hello World')
