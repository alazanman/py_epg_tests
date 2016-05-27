# -*- coding: utf-8 -*-
from tests import *
from model.channel import Channel
# from nose_config import *
# from nose_parameterized import parameterized, param


@parameterized([param(channel) for channel in load_from_json("channels.json")])
def test_create_channel(channel):
    # rest.auth('root', '123')
    old_channels = db.channel.get_channels()
    app.channel.create(channel)
    new_channels = db.channel.get_channels()
    assert db.channel.count() == len(old_channels) + 1
    assert len(new_channels) == len(old_channels) + 1
    old_channels.append(channel)
    assert sorted(old_channels, key=Channel.id_or_max) == sorted(new_channels, key=Channel.id_or_max)



# # def test_create_channel(rest, app, db, json_channels):
# def test_create_channel(app, db, json_channels):
#     # rest.auth('root', '123')
#     channel = json_channels
#     old_channels = db.channel.get_channels()
#     app.channel.create(channel)
#     new_channels = db.channel.get_channels()
#     assert db.channel.count() == len(old_channels) + 1
#     assert len(new_channels) == len(old_channels) + 1
#     old_channels.append(channel)
#     assert sorted(old_channels, key=Channel.id_or_max) == sorted(new_channels, key=Channel.id_or_max)

def setup_module():
    global db, app
    db = set_db()
    app = set_app()