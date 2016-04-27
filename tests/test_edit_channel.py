# -*- coding: utf-8 -*-
from model.channel import Channel
from random import randint
from random import randrange
from time import sleep


def test_edit_first_channel_name(app):
    #sleep(1)
    # CREATE IF NOT EXIST (TO IMPLEMENT VIA DB)
    if app.channel.count() == 0:
        app.channel.create(
            Channel(name='Channel' + str(randint(0, 9999)), service_id="2345", epg_name="epg_name2", offset="3",
                    provider="Provider"))
    old_channels = app.channel.get_channels()
    channel = Channel(name='Edited' + str(randint(0, 9999)))
    channel.id = old_channels[0].id
    app.channel.edit_first_channel(channel)
    sleep(1)
    new_channels = app.channel.get_channels()
    #print "new_channels", new_channels
    assert len(new_channels) == len(old_channels)
    old_channels[0] = channel
    assert sorted(old_channels, key=Channel.id_or_max) == sorted(new_channels, key=Channel.id_or_max)

def test_edit_some_channel_name(app):
    #sleep(1)
    # CREATE IF NOT EXIST (TO IMPLEMENT VIA DB)
    if app.channel.count() == 0:
        app.channel.create(
            Channel(name='Channel' + str(randint(0, 9999)), service_id="2345", epg_name="epg_name2", offset="3",
                    provider="Provider"))
    old_channels = app.channel.get_channels()
    channel = Channel(name='Edited' + str(randint(0, 9999)))
    index = randrange(len(old_channels))
    channel.id = old_channels[index].id
    app.channel.edit_channel_by_index(index, channel)
    sleep(1)
    new_channels = app.channel.get_channels()
    #print "new_channels", new_channels
    assert len(new_channels) == len(old_channels)
    old_channels[index] = channel
    assert sorted(old_channels, key=Channel.id_or_max) == sorted(new_channels, key=Channel.id_or_max)