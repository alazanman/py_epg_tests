# -*- coding: utf-8 -*-
from tests import *
from model.channel import random_channel


def test_rest():
    print 'rest started'
    # rest.auth('root', '123')
    rest.channel.create(random_channel())

    # print encode_base64(r'C:\Users\Alexey.Tanana\Documents\workspace\satprof\py_epg_tests\data\banners\icon_valid.jpg')
    print 'rest done'
    # assert rest.compare_files_CRC("C:\\Users\\Alexey.Tanana\\Documents\\workspace\\satprof\\py_epg_tests\\data\\banners\\wide_valid.jpg", "banners/444/wide_banner.jpeg")


def setup_module():
    global rest
    rest = set_rest()
    # print rest
    # return rest