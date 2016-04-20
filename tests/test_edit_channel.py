# -*- coding: utf-8 -*-
from model.channel import Channel
from random import randint
from time import sleep


def test_edit_first_channel_name(app):
    sleep(1)
    # CREATE IF NOT EXIST (TO IMPLEMENT VIA DB)
    if app.channel.count() == 0:
        app.channel.create(
            Channel(name='Channel' + str(randint(0, 9999)), service_id="2345", epg_name="epg_name2", offset="3",
                    provider="Provider"))
    old_channels = app.channel.get_channel_list()
    app.channel.edit_first_channel(Channel(name='Edited' + str(randint(0, 9999))))
    sleep(1)
    new_channels = app.channel.get_channel_list()
    #print "new_channels", new_channels
    assert len(new_channels) == len(old_channels)