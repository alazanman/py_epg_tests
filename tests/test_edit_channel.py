# -*- coding: utf-8 -*-
from tests import *
from model.channel import Channel
from random import randint
from random import choice
from time import sleep


@parameterized([param(channel) for channel in load_from_json("channels_edited.json")])
def test_edit_some_channel(channel_edited):
    # channel_edited = json_channels_edited
    while db.channel.count() < 3:
        # TO IMPLEMENT VIA DB
        app.channel.create(
            Channel(name='Channel' + str(randint(0, 9999999)), service_id=str(randint(0, 65535)),
                    epg_name='Epg_name_' + str(randint(0, 9999999)), offset=str(randint(-23, 23)),
                    provider='Provider_' + str(randint(0, 9999999))))
    old_channels = db.channel.get_channels()
    channel = choice(old_channels)
    channel_edited.id = channel.id
    app.channel.edit_channel_by_id(channel.id, channel_edited)
    # sleep(1)
    new_channels = db.channel.get_channels()
    # print old_channels, type(old_channels)
    old_channels.remove(channel)
    old_channels.append(channel_edited)
    assert len(new_channels) == len(old_channels)
    # print sorted(old_channels, key=Channel.id_or_max)
    # print sorted(new_channels, key=Channel.id_or_max)
    assert sorted(old_channels, key=Channel.id_or_max) == sorted(new_channels, key=Channel.id_or_max)
    if check_ui():
        assert sorted(app.channel.get_channels(), key=Channel.id_or_max) == sorted(new_channels, key=Channel.id_or_max)

    # def test_edit_some_channel(app, db, check_ui, json_channels_edited):
    #     channel_edited = json_channels_edited
    #     while db.channel.count() < 3:
    #         # TO IMPLEMENT VIA DB
    #         app.channel.create(
    #             Channel(name='Channel' + str(randint(0, 9999999)), service_id=str(randint(0, 65535)),
    #                     epg_name='Epg_name_' + str(randint(0, 9999999)), offset=str(randint(-23, 23)),
    #                     provider='Provider_' + str(randint(0, 9999999))))
    #     old_channels = db.channel.get_channels()
    #     channel = choice(old_channels)
    #     channel_edited.id = channel.id
    #     app.channel.edit_channel_by_id(channel.id, channel_edited)
    #     sleep(1)
    #     new_channels = db.channel.get_channels()
    #     # print old_channels, type(old_channels)
    #     old_channels.remove(channel)
    #     old_channels.append(channel_edited)
    #     assert len(new_channels) == len(old_channels)
    #     # print sorted(old_channels, key=Channel.id_or_max)
    #     # print sorted(new_channels, key=Channel.id_or_max)
    #     assert sorted(old_channels, key=Channel.id_or_max) == sorted(new_channels, key=Channel.id_or_max)
    #     if check_ui:
    #         assert sorted(app.channel.get_channels(), key=Channel.id_or_max) == sorted(new_channels,
    #                                                                                    key=Channel.id_or_max)

# def test_edit_last_channel_name(app, db, check_ui):

# def test_edit_first_channel_name(app, db, check_ui):
#     # CREATE IF NOT EXIST (TO IMPLEMENT VIA DB)
#     while db.channel.count() < 3:
#         # TO IMPLEMENT VIA DB
#         app.channel.create(
#             Channel(name='Channel' + str(randint(0, 9999999)), service_id=str(randint(0, 65535)), epg_name='Epg_name_' + str(randint(0, 9999999)), offset=str(randint(-23, 23)), provider='Provider_' + str(randint(0, 9999999))))
#     old_channels = db.channel.get_channels()
#     channel = Channel(name='First_Edited_' + str(randint(0, 9999999)))
#     channel.id = old_channels[0].id
#     app.channel.edit_first_channel(channel)
#     sleep(1)
#     new_channels = db.channel.get_channels()
#     #print "new_channels", new_channels
#     assert len(new_channels) == len(old_channels)
#     print old_channels[0]
#     print channel
#     old_channels[0] = channel
#     assert sorted(old_channels, key=Channel.id_or_max) == sorted(new_channels, key=Channel.id_or_max)
#     if check_ui:
#         assert sorted(app.channel.get_channels(), key=Channel.id_or_max) == sorted(new_channels, key=Channel.id_or_max)

def setup_module():
    global db, app
    db = set_db()
    app = set_app()