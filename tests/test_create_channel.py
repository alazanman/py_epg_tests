# -*- coding: utf-8 -*-
from model.channel import Channel


def test_create_channel(app):
    app.session.login("root", "123")
    app.channel.create(
        Channel(name="1234", service_id="2345", epg_name="epg_name2", offset="3", provider="Provider"))
    app.session.logout()