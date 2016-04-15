# -*- coding: utf-8 -*-
from model.channel import Channel


def test_edit_first_channel_name(app):
    app.channel.edit_first_channel(Channel(name="Edited"))