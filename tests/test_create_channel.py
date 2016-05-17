# -*- coding: utf-8 -*-
from model.channel import Channel


def test_create_channel(rest, app, db, json_channels):
# def test_create_channel(app, db, json_channels):
    rest.auth('root', '123')
    channel = json_channels
    old_channels = db.channel.get_channels()
    app.channel.create(channel)
    new_channels = db.channel.get_channels()
    assert db.channel.count() == len(old_channels) + 1
    assert len(new_channels) == len(old_channels) + 1
    old_channels.append(channel)
    assert sorted(old_channels, key=Channel.id_or_max) == sorted(new_channels, key=Channel.id_or_max)