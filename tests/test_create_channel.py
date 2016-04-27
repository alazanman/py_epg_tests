# -*- coding: utf-8 -*-
from model.channel import Channel
from time import sleep
import pytest
from data.channels import testdata


# @pytest.mark.parametrize("channel", testdata, ids=[repr(x) for x in testdata])
def test_create_channel(app, db, json_channels):
    # sleep(1)
    print "get_channels_count1: ", db.get_channels_count()
    channel = json_channels
    old_channels = db.get_channels()
    # print "old_channels", old_channels
    # channel = Channel(name='Channel' + str(randint(0, 9999)), service_id="2345", epg_name="epg_name2", offset="3", provider="Provider")
    print "get_channels_count2: ", db.get_channels_count(), len(old_channels)
    app.channel.create(channel)
    # sleep(1)
    print "get_channels_count3: ", db.get_channels_count()
    new_channels = db.get_channels()
    print "get_channels_count4: ", db.get_channels_count(), len(new_channels)
    # print "new_channels", new_channels
    # print type(db.get_channels_count()), type((len(old_channels) + 1))
    print "test ", db.get_channels_count(), len(old_channels)
    assert db.get_channels_count() == len(old_channels) + 1
    print "get_channels_count: ", db.get_channels_count()
    assert len(new_channels) == len(old_channels) + 1
    old_channels.append(channel)
    assert sorted(old_channels, key=Channel.id_or_max) == sorted(new_channels, key=Channel.id_or_max)