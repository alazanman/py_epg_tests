# -*- coding: utf-8 -*-
from model.channel import Channel


def test_rest(rest):
    print 'hello'
    print rest.auth('root', '123')
    print 'hello'
    assert 1 == 1