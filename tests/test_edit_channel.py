# -*- coding: utf-8 -*-
from model.channel import Channel
from random import randint
from time import sleep


def test_edit_first_channel_name(app):
    sleep(1)
    app.channel.edit_first_channel(Channel(name='Edited' + str(randint(0, 9999))))