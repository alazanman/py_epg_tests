# -*- coding: utf-8 -*-
from model.channel import Channel
from time import sleep
import pytest
from data.channels import testdata


# @pytest.mark.parametrize("channel", testdata, ids=[repr(x) for x in testdata])
def test_create_channel(app, data_channels):
    # sleep(1)
    channel = data_channels
    old_channels = app.channel.get_channel_list()
    # print "old_channels", old_channels
    # channel = Channel(name='Channel' + str(randint(0, 9999)), service_id="2345", epg_name="epg_name2", offset="3", provider="Provider")
    app.channel.create(channel)
    sleep(1)
    new_channels = app.channel.get_channel_list()
    # print "new_channels", new_channels
    # assert app.channel.count() == len(old_channels) + 1     # VIA DB
    assert len(new_channels) == len(old_channels) + 1
    old_channels.append(channel)
    assert sorted(old_channels, key=Channel.id_or_max) == sorted(new_channels, key=Channel.id_or_max)