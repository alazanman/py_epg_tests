# -*- coding: utf-8 -*-
from tests import *

# @parameterized([param(rest)])
# def test_rest_func(rest):
def test_rest_func():
    # global rest
    print 'hello1', rest
    print rest.auth('root', '123')
    # rest.auth('root', '123')
    print 'hello2'
    assert 2 == 2


def setup_module():
    global rest
    rest = set_rest()
    print rest
    return rest