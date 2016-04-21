# -*- coding: utf-8 -*-
from time import sleep
from random import randint
from model.channel import Channel


def test_delete_first_channel(app):
    #sleep(1)
    # CREATE IF NOT EXIST (TO IMPLEMENT VIA DB)
    if app.channel.count() == 0:
        app.channel.create(Channel(name='Channel' + str(randint(0, 9999)), service_id="2345", epg_name="epg_name2", offset="3", provider="Provider"))
    old_channels = app.channel.get_channel_list()
    app.channel.delete_first_channel()
    sleep(1)
    new_channels = app.channel.get_channel_list()
    #print "new_channels", new_channels
    assert len(new_channels) == len(old_channels) - 1
    old_channels[0:1] = []
    assert old_channels == new_channels