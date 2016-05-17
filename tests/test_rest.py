# -*- coding: utf-8 -*-
from model.channel import Channel


def test_rest(rest, app, db, json_channels):
    print 'hello'
    print rest.auth('root', '123')
    assert 1==1