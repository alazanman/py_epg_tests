# -*- coding: utf-8 -*-
from model.channel import Channel


def test_edit_first_channel_name(app):
    app.session.login("root", "123")
    app.channel.edit_first_channel(Channel(name="Edited"))
    app.session.logout()