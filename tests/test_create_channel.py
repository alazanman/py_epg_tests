# -*- coding: utf-8 -*-
from tests import *
from model.channel import Channel
# from nose_config import *
# from nose_parameterized import parameterized, param


# @parameterized([param(channel) for channel in load_from_json("channels_required_fields_only.json")])
@parameterized([param(channel) for channel in load_from_json("channels.json")] + [param(channel) for channel in load_from_json("channels_required_fields_only.json")])
def test_create_channel(channel):
    old_channels = db.channel.get_channels()
    app.channel.create(channel)
    new_channels = db.channel.get_channels()
    # banners validation
    for ch in new_channels:
        if ch == channel:
            assert rest.compare_files_CRC(channel.icon["user_file"], ch.icon["server_file"])
            assert rest.compare_files_CRC(channel.narrow_banner["user_file"], ch.narrow_banner["server_file"])
            assert rest.compare_files_CRC(channel.wide_banner["user_file"], ch.wide_banner["server_file"])
            break
    # assertion
    assert db.channel.count() == len(old_channels) + 1
    # assert len(new_channels) == len(old_channels) + 1
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
    global db, app, rest
    db = set_db()
    rest = set_rest()
    app = set_app()