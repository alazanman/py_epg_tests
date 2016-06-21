# -*- coding: utf-8 -*-
from tests import *
from random import choice
from random import randint
from model.channel import Channel
from model.channel import random_channel


def test_delete_some_channel():
    while db.channel.count() < 3:
        rest.channel.create(random_channel())
    old_channels = db.channel.get_channels()
    channel = choice(old_channels)
    app.channel.delete_channel_by_id(channel.id)
    new_channels = db.channel.get_channels()
    assert db.channel.count() == len(old_channels) - 1
    assert len(new_channels) == len(old_channels) - 1
    old_channels.remove(channel)
    assert sorted(old_channels, key=Channel.id_or_max) == sorted(new_channels, key=Channel.id_or_max)
    # if check_ui():
    #     assert sorted(app.channel.get_channels(), key=Channel.id_or_max) == sorted(new_channels, key=Channel.id_or_max)

def test_delete_first_channel():
    while db.channel.count() < 3:
        rest.channel.create(random_channel())
    old_channels = app.channel.get_channels()
    app.channel.delete_channel_by_index(0)
    # sleep(1)
    new_channels = app.channel.get_channels()
    # print "new_channels", new_channels
    assert len(new_channels) == len(old_channels) - 1
    old_channels[0:1] = []
    assert old_channels == new_channels

def test_delete_last_channel():
    while db.channel.count() < 3:
        rest.channel.create(random_channel())
    old_channels = app.channel.get_channels()
    channels_count = db.channel.count()
    app.channel.delete_channel_by_index(channels_count - 1)
    # sleep(1)
    new_channels = app.channel.get_channels()
    # print "new_channels", new_channels
    assert len(new_channels) == len(old_channels) - 1
    old_channels[channels_count-1:channels_count] = []
    assert old_channels == new_channels

def setup_module():
    global db, app
    db = set_db()
    app = set_app()