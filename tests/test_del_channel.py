# -*- coding: utf-8 -*-
from time import sleep
from random import randint
from model.channel import Channel


def test_delete_first_channel(app):
    sleep(1)
    # CREATE IF NOT EXIST (TO IMPLEMENT VIA DB)
    if app.channel.count() == 0:
        app.channel.create(Channel(name='Channel' + str(randint(0, 9999)), service_id="2345", epg_name="epg_name2", offset="3", provider="Provider"))
    app.channel.delete_first_channel()