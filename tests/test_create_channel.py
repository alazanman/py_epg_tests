# -*- coding: utf-8 -*-
from tests import *
from model.channel import Channel, random_channel
import copy


# @parameterized([param(channel) for channel in load_from_json("channels_required_fields_only.json")])
@parameterized([param(channel) for channel in load_from_json("channels.json")])
def test_create_channel_positive(channel):
    old_channels = db.channel.get_channels()
    app.channel.create(channel)
    new_channels = db.channel.get_channels()
    rest.channel.validate_banners(channel, new_channels)
    # assertion
    assert db.channel.count() == len(old_channels) + 1
    # assert len(new_channels) == len(old_channels) + 1
    old_channels.append(channel)
    assert sorted(old_channels, key=Channel.id_or_max) == sorted(new_channels, key=Channel.id_or_max)


def test_create_channel_with_not_unique_not_required_fields():
    # ENSURE EXIST FEW CHANNELS
    while db.channel.count() < 1:
        rest.channel.create(random_channel())
    old_channels = db.channel.get_channels()
    new_channel = copy.copy(choice(old_channels))
    new_channel.id = None
    new_channel.name = 'Channel_not_unique_not_required_fields_' + str(randint(0, 9999999))
    new_channel.epg_name = 'Epg_name_not_unique_not_required_fields_' + str(randint(0, 9999999))
    app.channel.create(new_channel)
    new_channels = db.channel.get_channels()
    rest.channel.validate_banners(new_channel, new_channels)
    assert db.channel.count() == len(old_channels) + 1
    old_channels.append(new_channel)
    assert sorted(old_channels, key=Channel.id_or_max) == sorted(new_channels, key=Channel.id_or_max)


@parameterized([param(channel) for channel in load_from_json("channels.json")])
def test_create_channel_negative():
    pass


def test_channel_with_spec_symbols():
    pass


def setup_module():
    global db, app, rest
    db = set_db()
    rest = set_rest()
    app = set_app()