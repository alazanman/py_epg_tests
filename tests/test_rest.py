# -*- coding: utf-8 -*-
from tests import *

# @parameterized([param(rest)])
# def test_rest_func(rest):
def test_rest_authentication():
    print 'rest auth started'
    # rest.auth('root', '123')
    print 'rest auth done'
    assert 2 == 2


def setup_module():
    global rest
    rest = set_rest()
    # print rest
    # return rest