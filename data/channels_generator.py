# -*- coding: utf-8 -*-
import jsonpickle
import os.path
from random import randint, randrange
from model.channel import Channel
from utils.string_util import random_string

channels_file = "../data/channels.json"
channels_edited_file = "../data/channels_edited.json"
channels_to_generate = 1

channels = [
    # UnicodeDecodeError: 'utf8' codec can't decode byte 0xe2 in position 15: invalid continuation byte
    # Channel(name=random_string('Channel_' + str(randint(0, 9999)), 100), service_id=str(randint(0, 9999)), epg_name='Epg_name_' + str(randint(0, 9999)), offset=str(randint(-23, 23)), provider='Provider_' + str(randint(0, 9999)))
    Channel(name='Channel_' + str(randint(0, 9999999)), service_id=str(randint(0, 65535)),
            epg_name='Epg_name_' + str(randint(0, 9999999)), offset=str(randint(-23, 23)),
            provider='Provider_' + str(randint(0, 9999999)), languages=str(randint(1,4)),
            icon="../data/banners/icon_valid.jpg", narrow_banner="../data/banners/narrow_valid.jpg",
            wide_banner="../data/banners/wide_valid.jpg")
    for i in range(channels_to_generate)
    ]

channels_edited = [
    # UnicodeDecodeError: 'utf8' codec can't decode byte 0xe2 in position 15: invalid continuation byte
    # Channel(name=random_string('Channel_' + str(randint(0, 9999)), 100), service_id=str(randint(0, 9999)), epg_name='Epg_name_' + str(randint(0, 9999)), offset=str(randint(-23, 23)), provider='Provider_' + str(randint(0, 9999)))
    Channel(name='Channel_Edited_' + str(randint(0, 9999999)), service_id=str(randint(0, 65535)),
            epg_name='Epg_name_Edited_' + str(randint(0, 9999999)), offset=str(randint(-23, 23)),
            provider='Provider_Edited_' + str(randint(0, 9999999)))
    for i in range(channels_to_generate)
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