# -*- coding: utf-8 -*-
from tests import *
from model.channel import Channel, random_channel
import copy
from selenium.common.exceptions import TimeoutException, UnexpectedAlertPresentException


#POSITIVE TESTS
@parameterized([param(channel) for channel in load_from_json("channels_create_positive.json")])
def test_create_channel_positive(channel):
    old_channels = db.channel.get_channels()
    for ch in old_channels:
        if ch.name == channel.name:
            raise Exception("The channel with such name already exists! This channеl wasn't created:", channel.name)
    app.channel.create(channel)
    new_channels = db.channel.get_channels()
    rest.channel.validate_banners(channel, new_channels)
    # assertion
    assert db.channel.count() == len(old_channels) + 1
    # assert len(new_channels) == len(old_channels) + 1
    old_channels.append(channel)
    # print "OLD: ", sorted(old_channels, key=Channel.id_or_max)
    # print "NEW: ", sorted(new_channels, key=Channel.id_or_max)
    assert sorted(old_channels, key=Channel.id_or_max) == sorted(new_channels, key=Channel.id_or_max)

def test_create_channel_with_not_unique_not_required_fields():
    # ENSURE EXIST FEW CHANNELS
    while db.channel.count() < 1:
        rest.channel.create(random_channel())
    old_channels = db.channel.get_channels()
    new_channel = copy.copy(choice(old_channels))
    new_channel.id = None
    new_channel.icon["server_file"] = None
    new_channel.narrow_banner["server_file"] = None
    new_channel.wide_banner["server_file"] = None
    new_channel.name = 'Channel_not_unique_not_required_fields_' + str(randint(0, 9999999))
    app.channel.create(new_channel)
    new_channels = db.channel.get_channels()
    assert db.channel.count() == len(old_channels) + 1
    old_channels.append(new_channel)
    # print "old_channels:", sorted(old_channels, key=Channel.id_or_max)
    # print "new_channels:", sorted(new_channels, key=Channel.id_or_max)
    assert sorted(old_channels, key=Channel.id_or_max) == sorted(new_channels, key=Channel.id_or_max)


# NEGATIVE TESTS
@parameterized([param(channel) for channel in load_from_json("channels_create_negative_required_fields.json")])
def test_create_channel_negative_required_field(channel):
    old_channels = db.channel.get_channels()
    try:
        app.channel.create(channel)
    except TimeoutException, e:
        print "Incorrect channel [%s, %s] wasn't saved (it's OK)" % (channel.name, channel.service_id)
    new_channels = db.channel.get_channels()
    assert app.channel.is_submit_button_present() and sorted(old_channels, key=Channel.id_or_max) == sorted(new_channels, key=Channel.id_or_max)

@parameterized([param(channel) for channel in load_from_json("channels_create_negative_incorrect_banners.json")])
def test_create_channel_negative_incorrect_banner(channel):
    old_channels = db.channel.get_channels()
    try:
        app.channel.create(channel)
    except UnexpectedAlertPresentException, e:
        # sleep(3)
        # alert_text = app.close_alert()
        app.close_alert()
        print "Channel [%s, %s] with incorrect picture wasn't saved (it's OK)" % (channel.name, channel.service_id)
        # print "There was alert with text:", alert_text
    new_channels = db.channel.get_channels()
    assert app.channel.is_submit_button_present() and sorted(old_channels, key=Channel.id_or_max) == sorted(new_channels, key=Channel.id_or_max)

@parameterized([param(channel) for channel in load_from_json("channels_create_negative_input_field_limits.json")])
def test_create_channel_negative_required_field(channel):
    old_channels = db.channel.get_channels()
    app.channel.create(channel)
    new_channels = db.channel.get_channels()
    for ch in new_channels:
        # print "qwe: ", ch, channel
        if ch.name in channel.name and \
            ch.service_id == channel.service_id and \
            ch.epg_name in channel.epg_name and \
            ch.offset == channel.offset and \
            ch.provider in channel.provider and \
            ch.languages == channel.languages and \
            ch.allow_record == channel.allow_record:
            old_channels.append(ch)
    assert sorted(old_channels, key=Channel.id_or_max) == sorted(new_channels, key=Channel.id_or_max)


# def test_channel_with_spec_symbols():
#     pass


def setup_module():
    global db, app, rest
    db = set_db()
    rest = set_rest()
    app = set_app()