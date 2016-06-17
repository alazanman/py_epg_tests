# -*- coding: utf-8 -*-
import jsonpickle
import os.path
from random import randint, randrange, choice
from model.channel import Channel
from nose_config import write_generated_data
from utils.string_util import random_string
from utils.file_util import abs_path_to_file


channels_file = "data/channels.json"
channels_edited_file = "data/channels_edited.json"
channels_required_fields_only_file = "data/channels_required_fields_only.json"
random_channels_to_generate = 1

channels = [
    # RANDOM CHANNELS (random_channels_to_generate quantity)
    Channel(name='Channel_random' + str(randint(0, 9999999)), service_id=str(randint(0, 65535)),
            epg_name='Epg_name_' + str(randint(0, 9999999)), offset=str(randint(-23, 23)),
            provider='Provider_' + str(randint(0, 9999999)),
            languages=sorted(set([str(randint(1,4)) for l in range(randint(1,4))])),
            allow_record=choice([bool(True), bool(False)]),
            icon={"user_file": abs_path_to_file("data/banners/icon_valid.jpg"), "server_file": None},
            narrow_banner={"user_file": abs_path_to_file("data/banners/narrow_valid.jpg"), "server_file": None},
            wide_banner={"user_file": abs_path_to_file("data/banners/wide_valid.jpg"), "server_file": None})
    for i in range(random_channels_to_generate)
    ]
channels.extend([
# REQUIRED FIELDS ONLY
Channel(name='Channel_required_fields_only_' + str(randint(0, 9999999)), service_id=str(randint(0, 65535)),
        epg_name='Epg_name_' + str(randint(0, 9999999)), offset=str(randint(-23, 23)),
        provider=None, languages=sorted(set([str(randint(1, 4)) for l in range(randint(1, 4))])),
        allow_record=False,
        icon={"user_file": None, "server_file": None},
        narrow_banner={"user_file": None, "server_file": None},
        wide_banner={"user_file": None, "server_file": None}),
# BOUNDARY MIN POSITIVE VALUES
Channel(name=str(randint(0, 9)),
        service_id=str(0),
        epg_name=str(randint(0, 9)),
        offset=str(-23),
        provider=str(randint(0, 9)),
        languages=sorted(set([str(1)])),
        allow_record=False,
        icon={"user_file": None, "server_file": None},
        narrow_banner={"user_file": None, "server_file": None},
        wide_banner={"user_file": None, "server_file": None}),
# BOUNDARY MAX POSITIVE VALUES
Channel(name='_3_5_7_9_12_15_18_21_24_27_30_33_36_39_42_45_48_51_54_57_60_63_66_69_72_75_78_81_84_87_90_93_96_100_104_108_112_116_120_1' + str(randint(9000000, 9999999)),
        service_id=str(65535),
        epg_name='_3_5_7_9_12_15_18_21_24_27_30_33_36_39_42_4' + str(randint(9000000, 9999999)),
        offset=str(23),
        provider='_3_5_7_9_12_15_18_21_24_27_30_33_36_39_42_45_48_51_54_57_60_63_66_69_72_75_78_81_84_87_90_93_96_100_104_108_112_116_120_1' + str(randint(9000000, 9999999)),
        languages=sorted(set([str(4)])),
        allow_record=False,
        icon={"user_file": None, "server_file": None},
        narrow_banner={"user_file": None, "server_file": None},
        wide_banner={"user_file": None, "server_file": None})
])

channels_negative = [

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

write_generated_data(channels_file, channels)
write_generated_data(channels_edited_file, channels_edited)
