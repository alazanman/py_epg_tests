# -*- coding: utf-8 -*-
from tests import *
from utils.file_util import encode_base64

def test_rest():
    print 'rest started'
    # rest.auth('root', '123')
    # rest.channel.create(Channel(name='Channel' + str(randint(0, 9999999)), service_id=str(randint(0, 65535)),
    #                             epg_name='Epg_name_' + str(randint(0, 9999999)), offset=str(randint(-23, 23)),
    #                             provider='Provider_' + str(randint(0, 9999999))))
    print "111", abs_path_to_file(r"data/banners/icon_valid.jpg"), '222'
    print "111", abs_path_to_file(r"data/banners/narrow_valid.jpg"), '222'
    print "111", abs_path_to_file(r"data/banners/wide_valid.jpg"), '222'
    rest.channel.create(Channel(name='Channel_random_' + str(randint(0, 9999999)), service_id=str(randint(0, 65535)),
            epg_name='Epg_name_' + str(randint(0, 9999999)), offset=str(randint(-23, 23)),
            provider='Provider_' + str(randint(0, 9999999)),
            # languages=sorted(set([str(randint(1,4)) for l in range(randint(1,4))])),
            languages=str(randint(1,4)),
            allow_record=choice([bool(True), bool(False)]),
            icon={"user_file": abs_path_to_file(r"data/banners/icon_valid.jpg"), "server_file": None},
            narrow_banner={"user_file": abs_path_to_file(r"data/banners/narrow_valid.jpg"), "server_file": None},
            wide_banner={"user_file": abs_path_to_file(r"data/banners/wide_valid.jpg"), "server_file": None}))





    # print encode_base64(r'C:\Users\Alexey.Tanana\Documents\workspace\satprof\py_epg_tests\data\banners\icon_valid.jpg')

    print 'rest done'
    # assert rest.compare_files_CRC("C:\\Users\\Alexey.Tanana\\Documents\\workspace\\satprof\\py_epg_tests\\data\\banners\\wide_valid.jpg", "banners/444/wide_banner.jpeg")


def setup_module():
    global rest
    rest = set_rest()
    # print rest
    # return rest