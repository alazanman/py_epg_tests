# -*- coding: utf-8 -*-
import jsonpickle
import os.path
from random import randint, randrange, choice
from model.channel import Channel
from nose_config import write_generated_data
from utils.string_util import random_string, random_string_fixed_len
from utils.file_util import abs_path_to_file, random_file_from_dir


channels_create_positive_file = "data/channels_create_positive.json"
channels_create_negative_blank_required_fields_file = "data/channels_create_negative_blank_required_fields.json"
channels_create_negative_input_field_limits_file = "data/channels_create_negative_input_field_limits.json"
channels_create_negative_service_id_out_of_range_file = "data/channels_create_negative_service_id_out_of_range.json"
channels_create_negative_invalid_icon_and_banners_file = "data/channels_create_negative_invalid_icon_and_banners.json"
channels_edit_positive_file = "data/channels_edit_positive.json"
random_channels_to_generate = 1

#=============================CHANNELS CREATION TESTS DATA==========================================
channels_create_positive = [
    # RANDOM CHANNELS (random_channels_to_generate quantity)
    Channel(name=random_string('Channel_random_', 128), service_id=str(randint(0, 65535)),
            epg_name=random_string('Epg_name_', 50), offset=str(randint(-23, 23)),
            provider=random_string('Provider_', 128),
            languages=sorted(set([str(randint(1,4)) for l in range(randint(1,4))])),
            allow_record=choice([bool(True), bool(False)]),
            icon={"user_file": random_file_from_dir("data/banners/valid/icon/"), "server_file": None},
            narrow_banner={"user_file": random_file_from_dir("data/banners/valid/narrow_banner/"), "server_file": None},
            wide_banner={"user_file": random_file_from_dir("data/banners/valid/wide_banner/"), "server_file": None})
    for i in range(random_channels_to_generate)
    ]
channels_create_positive.extend([
# REQUIRED FIELDS ONLY
Channel(name=random_string('Channel_required_fields_only_', 128), service_id=str(randint(0, 65535)),
        epg_name=random_string('Epg_name_', 50), offset='0', provider='',allow_record=False,
        languages=sorted(set([str(randint(1, 4)) for l in range(randint(1, 4))]))
        ),
# BOUNDARY MIN POSITIVE VALUES
Channel(name=random_string('', 1), service_id=str(0), epg_name=random_string('', 1), offset="-23",
        provider=random_string('', 1), languages=sorted(set([str(1)])), allow_record=False),
# BOUNDARY MAX POSITIVE VALUES
Channel(name=random_string_fixed_len('128_symbols_string_', 128), service_id=str(65535),
        epg_name=random_string_fixed_len('50_symbols_string_', 50), offset="23",
        provider=random_string_fixed_len('128_symbols_string_', 128), languages=[str(4)], allow_record=True)
])

channels_create_negative_blank_required_fields = [
    # BLANK CHANNEL NAME
    Channel(name='', service_id=str(randint(0, 65535)), epg_name=random_string('Epg_name_', 50), provider=random_string('Provider_', 128),
            languages=sorted(set([str(randint(1, 4)) for l in range(randint(1, 4))])), allow_record=choice([bool(True), bool(False)])),
    # BLANK SERVICE ID
    Channel(name=random_string('Channel_blank_service_id_', 128), service_id='', epg_name=random_string('Epg_name_', 50),
            provider=random_string('Provider_', 128),
            languages=sorted(set([str(randint(1, 4)) for l in range(randint(1, 4))])),
            allow_record=choice([bool(True), bool(False)])),
    # BLANK EPG NAME
    Channel(name=random_string('Channel_blank_epgname_', 128), service_id=str(randint(0, 65535)), epg_name='',
            provider=random_string('Provider_', 128), languages=sorted(set([str(randint(1, 4)) for l in range(randint(1, 4))])), allow_record=choice([bool(True), bool(False)])),
    # BLANK OFFSET
    Channel(name=random_string('Channel_blank_offset_', 128), service_id=str(randint(0, 65535)),
            epg_name=random_string('Epg_name_', 50), offset='', provider=random_string('Provider_', 128),
            languages=sorted(set([str(randint(1, 4)) for l in range(randint(1, 4))])), allow_record=choice([bool(True), bool(False)])),
    # NO LANGUAGES
    Channel(name=random_string('Channel_no_langs_', 128), epg_name=random_string('Epg_name_', 50), provider=random_string('Provider_', 128),
            languages=[], allow_record=choice([bool(True), bool(False)])),
]

channels_create_negative_input_field_limits = [
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
    # TOO LONG CHANNEL NAME 1000
    Channel(name=random_string_fixed_len('1000_symbols_string_', 1000), service_id=str(randint(0, 65535)),
            epg_name=random_string('Epg_name_', 50), offset=str(randint(-23, 23)),
            provider=random_string('Provider_', 128),
            languages=sorted(set([str(randint(1, 4)) for l in range(randint(1, 4))])),
            allow_record=choice([bool(True), bool(False)])),
    # TOO LONG EPG_NAME 1000
    Channel(name=random_string('Channel_name_', 128), service_id=str(randint(0, 65535)),
            epg_name=random_string_fixed_len('1000_symbols_string_', 1000), offset=str(randint(-23, 23)),
            provider=random_string('Provider_', 128),
            languages=sorted(set([str(randint(1, 4)) for l in range(randint(1, 4))])),
            allow_record=choice([bool(True), bool(False)])),
    # TOO LONG PROVIDER 1000
    Channel(name=random_string('Channel_name_', 128), service_id=str(randint(0, 65535)),
            epg_name=random_string('EPG_name_', 50), offset=str(randint(-23, 23)),
            provider=random_string_fixed_len('1000_symbols_string_', 1000),
            languages=sorted(set([str(randint(1, 4)) for l in range(randint(1, 4))])),
            allow_record=choice([bool(True), bool(False)])),
]

channels_create_negative_service_id_out_of_range = [
    # TOO BIG SERVICE ID
    Channel(name=random_string('129_symbols_string_', 128), service_id='65536',
            epg_name=random_string('Epg_name_', 50), offset=str(randint(-23, 23)),
            provider=random_string('Provider_', 128),
            languages=sorted(set([str(randint(1, 4)) for l in range(randint(1, 4))])),
            allow_record=choice([bool(True), bool(False)])),
    # NEGATIVE SERVICE ID
    Channel(name=random_string('129_symbols_string_', 128), service_id='-1',
            epg_name=random_string('Epg_name_', 50), offset=str(randint(-23, 23)),
            provider=random_string('Provider_', 128),
            languages=sorted(set([str(randint(1, 4)) for l in range(randint(1, 4))])),
            allow_record=choice([bool(True), bool(False)])),
]

channels_create_negative_invalid_icon_and_banners = [
    # CHANNELS WITH INVALID ICON
    Channel(name=random_string('Channel_random_', 128), service_id=str(randint(0, 65535)),
            epg_name=random_string('Epg_name_', 50), offset=str(randint(-23, 23)),
            provider=random_string('Provider_', 128),
            languages=sorted(set([str(randint(1,4)) for l in range(randint(1,4))])),
            allow_record=choice([bool(True), bool(False)]),
            icon={"user_file": abs_path_to_file("data/banners/invalid/icon/" + f), "server_file": None})
    for f in (os.listdir(os.path.join(os.getcwd(), "data/banners/invalid/icon/")))
]
channels_create_negative_invalid_icon_and_banners.extend([
     # CHANNELS WITH INVALID NARROW BANNER
     Channel(name=random_string('Channel_random_', 128), service_id=str(randint(0, 65535)),
             epg_name=random_string('Epg_name_', 50), offset=str(randint(-23, 23)),
             provider=random_string('Provider_', 128),
             languages=sorted(set([str(randint(1, 4)) for l in range(randint(1, 4))])),
             allow_record=choice([bool(True), bool(False)]),
             narrow_banner={"user_file": abs_path_to_file("data/banners/invalid/narrow_banner/" + f), "server_file": None})
     for f in (os.listdir(os.path.join(os.getcwd(), "data/banners/invalid/narrow_banner/")))
     ])
channels_create_negative_invalid_icon_and_banners.extend([
     # CHANNELS WITH INVALID WIDE BANNER
     Channel(name=random_string('Channel_random_', 128), service_id=str(randint(0, 65535)),
             epg_name=random_string('Epg_name_', 50), offset=str(randint(-23, 23)),
             provider=random_string('Provider_', 128),
             languages=sorted(set([str(randint(1, 4)) for l in range(randint(1, 4))])),
             allow_record=choice([bool(True), bool(False)]),
             narrow_banner={"user_file": random_file_from_dir("data/banners/valid/narrow_banner/"), "server_file": None},
             wide_banner={"user_file": abs_path_to_file("data/banners/invalid/wide_banner/" + f), "server_file": None})
     for f in (os.listdir(os.path.join(os.getcwd(), "data/banners/invalid/wide_banner/")))
     ])
#=============================CHANNELS EDIT TESTS DATA==========================================
channels_edit_positive = [
    Channel(name=random_string('Channel_Edited__random_', 128), service_id=str(randint(0, 65535)),
            epg_name=random_string('Epg_name_Edited_', 50), offset=str(randint(-23, 23)),
            provider=random_string('Provider_Edited_', 128),
            languages=sorted(set([str(randint(1,4)) for l in range(randint(1,4))])),
            allow_record=choice([bool(True), bool(False)]),
            icon={"user_file": random_file_from_dir("data/banners/valid/icon/"), "server_file": None},
            narrow_banner={"user_file": random_file_from_dir("data/banners/valid/narrow_banner/"), "server_file": None},
            wide_banner={"user_file": random_file_from_dir("data/banners/valid/wide_banner/"), "server_file": None})
    for i in range(random_channels_to_generate)
    ]

write_generated_data(channels_create_positive_file, channels_create_positive)
write_generated_data(channels_create_negative_blank_required_fields_file, channels_create_negative_blank_required_fields)
write_generated_data(channels_create_negative_input_field_limits_file, channels_create_negative_input_field_limits)
write_generated_data(channels_create_negative_service_id_out_of_range_file, channels_create_negative_service_id_out_of_range)
write_generated_data(channels_create_negative_invalid_icon_and_banners_file, channels_create_negative_invalid_icon_and_banners)
write_generated_data(channels_edit_positive_file, channels_edit_positive)


# def random_file_in_dir(relative_path):
#     random_file = choice(os.listdir(os.path.join(os.getcwd(), relative_path)))
#     return abs_path_to_file(random_file)