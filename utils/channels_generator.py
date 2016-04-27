# -*- coding: utf-8 -*-
import jsonpickle
import os.path
from random import randint
from model.channel import Channel
from utils.string_util import random_string


path_to_file = "../data/channels.json"
channels_to_generate = 1

testdata = [
    # UnicodeDecodeError: 'utf8' codec can't decode byte 0xe2 in position 15: invalid continuation byte
    # Channel(name=random_string('Channel_' + str(randint(0, 9999)), 100), service_id=str(randint(0, 9999)), epg_name='Epg_name_' + str(randint(0, 9999)), offset=str(randint(-23, 23)), provider='Provider_' + str(randint(0, 9999)))
    Channel(name='Channel_' + str(randint(0, 9999)), service_id=str(randint(0, 9999)),
            epg_name='Epg_name_' + str(randint(0, 9999)), offset=str(randint(-23, 23)),
            provider='Provider_' + str(randint(0, 9999)))
    for i in range(channels_to_generate)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), path_to_file)

with open(file, "w") as f:
    # f.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))
    jsonpickle.set_encoder_options("json", indent=2)
    f.write(jsonpickle.encode(testdata))