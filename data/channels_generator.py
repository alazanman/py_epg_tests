# -*- coding: utf-8 -*-
import jsonpickle
import os.path
from random import randint, randrange, choice
from model.channel import Channel
from utils.string_util import random_string

channels_file = "../data/channels.json"
channels_edited_file = "../data/channels_edited.json"
channels_required_fields_only_file = "../data/channels_required_fields_only.json"
random_channels_to_generate = 1
# current_path = os.getcwd()


def abs_path_to_file(relative_path):
    return os.path.abspath(os.path.join(os.getcwd(), relative_path))


channels = [
    # UnicodeDecodeError: 'utf8' codec can't decode byte 0xe2 in position 15: invalid continuation byte
    # Channel(name=random_string('Channel_' + str(randint(0, 9999)), 100), service_id=str(randint(0, 9999)), epg_name='Epg_name_' + str(randint(0, 9999)), offset=str(randint(-23, 23)), provider='Provider_' + str(randint(0, 9999)))
    Channel(name='Channel_' + str(randint(0, 9999999)), service_id=str(randint(0, 65535)),
            epg_name='Epg_name_' + str(randint(0, 9999999)), offset=str(randint(-23, 23)),
            provider='Provider_' + str(randint(0, 9999999)), languages=sorted(set([str(randint(1,4)) for l in range(randint(1,4))])),
            allow_record=choice([bool(True), bool(False)]),
            icon={"user_file": abs_path_to_file("../data/banners/icon_valid.jpg"), "server_file": None},
            narrow_banner={"user_file": abs_path_to_file("../data/banners/narrow_valid.jpg"), "server_file": None},
            wide_banner={"user_file": abs_path_to_file("../data/banners/wide_valid.jpg"), "server_file": None})
    for i in range(random_channels_to_generate)
    ]

channels_required_fields_only = [
    # UnicodeDecodeError: 'utf8' codec can't decode byte 0xe2 in position 15: invalid continuation byte
    # Channel(name=random_string('Channel_' + str(randint(0, 9999)), 100), service_id=str(randint(0, 9999)), epg_name='Epg_name_' + str(randint(0, 9999)), offset=str(randint(-23, 23)), provider='Provider_' + str(randint(0, 9999)))
    Channel(name='Channel_' + str(randint(0, 9999999)), service_id=str(randint(0, 65535)),
            epg_name='Epg_name_' + str(randint(0, 9999999)), offset=str(randint(-23, 23)),
            provider=None, languages=sorted(set([str(randint(1,4)) for l in range(randint(1,4))])),
            allow_record=False,
            icon={"user_file": None, "server_file": None},
            narrow_banner={"user_file": None, "server_file": None},
            wide_banner={"user_file": None, "server_file": None})
    ]

# os.path.abspath(os.path.join(os.getcwd(), file_path))

channels_edited = [
    # UnicodeDecodeError: 'utf8' codec can't decode byte 0xe2 in position 15: invalid continuation byte
    # Channel(name=random_string('Channel_' + str(randint(0, 9999)), 100), service_id=str(randint(0, 9999)), epg_name='Epg_name_' + str(randint(0, 9999)), offset=str(randint(-23, 23)), provider='Provider_' + str(randint(0, 9999)))
    Channel(name='Channel_Edited_' + str(randint(0, 9999999)), service_id=str(randint(0, 65535)),
            epg_name='Epg_name_Edited_' + str(randint(0, 9999999)), offset=str(randint(-23, 23)),
            provider='Provider_Edited_' + str(randint(0, 9999999)), languages=sorted(set([str(randint(1,4)) for l in range(randint(1,4))])),
            allow_record=choice([bool(True), bool(False)]),
            icon={"user_file": abs_path_to_file("../data/banners/icon_valid_edited.jpg"), "server_file": None},
            # narrow_banner={"user_file": None, "server_file": None},
            narrow_banner={"user_file": abs_path_to_file("../data/banners/narrow_valid_edited.jpg"), "server_file": None},
            # wide_banner={"user_file": None, "server_file": None})
            wide_banner={"user_file": abs_path_to_file("../data/banners/wide_valid_edited.jpg"), "server_file": None})
    for i in range(random_channels_to_generate)
    ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), channels_file)
with open(file, "w") as f:
    # f.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))
    jsonpickle.set_encoder_options("json", indent=2)
    f.write(jsonpickle.encode(channels))

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), channels_edited_file)
with open(file, "w") as f:
    # f.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))
    jsonpickle.set_encoder_options("json", indent=2)
    f.write(jsonpickle.encode(channels_edited))

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), channels_required_fields_only_file)
with open(file, "w") as f:
    # f.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))
    jsonpickle.set_encoder_options("json", indent=2)
    f.write(jsonpickle.encode(channels_required_fields_only))