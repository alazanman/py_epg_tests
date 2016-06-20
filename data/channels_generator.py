# -*- coding: utf-8 -*-
import jsonpickle
import os.path
from random import randint, randrange, choice
from model.channel import Channel
from nose_config import write_generated_data
from utils.string_util import random_string, random_string_fixed_len
from utils.file_util import abs_path_to_file


channels_positive_file = "data/channels_positive.json"
channels_edited_file = "data/channels_edited.json"
channels_negative_required_fields_file = "data/channels_negative_required_fields.json"
channels_negative_input_field_limits_file = "data/channels_negative_input_field_limits.json"
random_channels_to_generate = 0

channels_positive = [
    # RANDOM CHANNELS (random_channels_to_generate quantity)
    Channel(name=random_string('Channel_random_', 128), service_id=str(randint(0, 65535)),
            epg_name=random_string('Epg_name_', 50), offset=str(randint(-23, 23)),
            provider=random_string('Provider_', 128),
            languages=sorted(set([str(randint(1,4)) for l in range(randint(1,4))])),
            allow_record=choice([bool(True), bool(False)]),
            icon={"user_file": abs_path_to_file("data/banners/icon_valid.jpg"), "server_file": None},
            narrow_banner={"user_file": abs_path_to_file("data/banners/narrow_valid.jpg"), "server_file": None},
            wide_banner={"user_file": abs_path_to_file("data/banners/wide_valid.jpg"), "server_file": None})
    for i in range(random_channels_to_generate)
    ]
channels_positive.extend([
# REQUIRED FIELDS ONLY
Channel(name=random_string('Channel_required_fields_only_', 128), service_id=str(randint(0, 65535)),
        epg_name=random_string('Epg_name_', 128), offset='0', provider='',allow_record=False,
        languages=sorted(set([str(randint(1, 4)) for l in range(randint(1, 4))]))
        ),
# BOUNDARY MIN POSITIVE VALUES
Channel(name=random_string('', 1), service_id=str(0), epg_name=random_string('', 1), offset="-23",
        provider=random_string('', 1), languages=sorted(set([str(1)])), allow_record=False),
# BOUNDARY MAX POSITIVE VALUES
Channel(name=random_string_fixed_len('128_symbols_string_', 128), service_id=str(65535),
        epg_name=random_string_fixed_len('128_symbols_string_', 50), offset="23",
        provider=random_string_fixed_len('128_symbols_string_', 128), languages=[str(4)], allow_record=True)
])

channels_negative_required_fields = [
    # BLANK CHANNEL NAME
    Channel(name='', service_id=str(randint(0, 65535)), epg_name=random_string('Epg_name_', 128), provider='',
            languages=sorted(set([str(randint(1, 4)) for l in range(randint(1, 4))])), allow_record=choice([bool(True), bool(False)])),
    # BLANK EPG NAME
    Channel(name=random_string('Channel_blank_epgname_', 128), service_id=str(randint(0, 65535)), epg_name='',
            provider='', languages=sorted(set([str(randint(1, 4)) for l in range(randint(1, 4))])), allow_record=choice([bool(True), bool(False)])),
    # BLANK OFFSET
    Channel(name=random_string('Channel_blank_offset_', 128), service_id=str(randint(0, 65535)),
            epg_name=random_string('Epg_name_', 50), offset='', provider='',
            languages=sorted(set([str(randint(1, 4)) for l in range(randint(1, 4))])), allow_record=choice([bool(True), bool(False)])),
    # NO LANGUAGES
    Channel(name=random_string('Channel_no_langs_', 128), epg_name=random_string('Epg_name_', 50), provider='',
            languages=[], allow_record=choice([bool(True), bool(False)])),
]

channels_negative_input_field_limits = [
    # TOO LONG CHANNEL NAME
    Channel(name=random_string_fixed_len('129_symbols_string_', 129), service_id=str(randint(0, 65535)),
            epg_name=random_string('Epg_name_', 50), offset=str(randint(-23, 23)),
            provider=random_string('Provider_', 128),
            languages=sorted(set([str(randint(1, 4)) for l in range(randint(1, 4))])),
            allow_record=choice([bool(True), bool(False)])),
    # TOO LONG EPG_NAME
    Channel(name=random_string('Channel_name_', 128), service_id=str(randint(0, 65535)),
            epg_name=random_string_fixed_len('51_symbols_string_', 51), offset=str(randint(-23, 23)),
            provider=random_string('Provider_', 128),
            languages=sorted(set([str(randint(1, 4)) for l in range(randint(1, 4))])),
            allow_record=choice([bool(True), bool(False)])),
    # TOO LONG PROVIDER
    Channel(name=random_string('Channel_name_', 128), service_id=str(randint(0, 65535)),
            epg_name=random_string('EPG_name_', 50), offset=str(randint(-23, 23)),
            provider=random_string_fixed_len('129_symbols_string_', 129),
            languages=sorted(set([str(randint(1, 4)) for l in range(randint(1, 4))])),
            allow_record=choice([bool(True), bool(False)])),
    # TOO LONG CHANNEL NAME 100000
    Channel(name=random_string_fixed_len('10000_symbols_string_', 10000), service_id=str(randint(0, 65535)),
            epg_name=random_string('Epg_name_', 50), offset=str(randint(-23, 23)),
            provider=random_string('Provider_', 128),
            languages=sorted(set([str(randint(1, 4)) for l in range(randint(1, 4))])),
            allow_record=choice([bool(True), bool(False)])),
    # TOO LONG EPG_NAME 100000
    Channel(name=random_string('Channel_name_', 128), service_id=str(randint(0, 65535)),
            epg_name=random_string_fixed_len('10000_symbols_string_', 10000), offset=str(randint(-23, 23)),
            provider=random_string('Provider_', 128),
            languages=sorted(set([str(randint(1, 4)) for l in range(randint(1, 4))])),
            allow_record=choice([bool(True), bool(False)])),
    # TOO LONG PROVIDER 100000
    Channel(name=random_string('Channel_name_', 128), service_id=str(randint(0, 65535)),
            epg_name=random_string('EPG_name_', 50), offset=str(randint(-23, 23)),
            provider=random_string_fixed_len('10000_symbols_string_', 10000),
            languages=sorted(set([str(randint(1, 4)) for l in range(randint(1, 4))])),
            allow_record=choice([bool(True), bool(False)])),
]


channels_edited = [
    # UnicodeDecodeError: 'utf8' codec can't decode byte 0xe2 in position 15: invalid continuation byte
    # Channel(name=random_string('Channel_' + str(randint(0, 9999)), 100), service_id=str(randint(0, 9999)), epg_name='Epg_name_' + str(randint(0, 9999)), offset=str(randint(-23, 23)), provider='Provider_' + str(randint(0, 9999)))
    Channel(name='Channel_Edited_' + str(randint(0, 9999999)), service_id=str(randint(0, 65535)),
            epg_name='Epg_name_Edited_' + str(randint(0, 9999999)), offset=str(randint(-23, 23)),
            # provider='Provider_Edited_' + str(randint(0, 9999999)),
            provider='',
            languages=sorted(set([str(randint(1,4)) for l in range(randint(1,4))])),
            allow_record=choice([bool(True), bool(False)]),
            icon={"user_file": abs_path_to_file("data/banners/icon_valid_edited.jpg"), "server_file": None},
            # narrow_banner={"user_file": None, "server_file": None},
            narrow_banner={"user_file": abs_path_to_file("data/banners/narrow_valid_edited.jpg"), "server_file": None},
            # wide_banner={"user_file": None, "server_file": None})
            wide_banner={"user_file": abs_path_to_file("data/banners/wide_valid_edited.jpg"), "server_file": None})
    for i in range(random_channels_to_generate)
    ]

write_generated_data(channels_positive_file, channels_positive)
write_generated_data(channels_negative_required_fields_file, channels_negative_required_fields)
write_generated_data(channels_negative_input_field_limits_file, channels_negative_input_field_limits)
write_generated_data(channels_edited_file, channels_edited)