# -*- coding: utf-8 -*-
from tests import *
import binascii

# @parameterized([param(rest)])
# def test_rest_func(rest):
def test_rest():
    print 'rest auth started'
    # rest.auth('root', '123')

    print rest.compare_files_CRC("C:\\Users\\Alexey.Tanana\\Documents\\workspace\\satprof\\py_epg_tests\\data\\banners\\wide_valid.jpg", "banners/444/wide_banner.jpeg")
    #
    # r = rest.session.get("C:\\Users\\Alexey.Tanana\\Documents\\workspace\\satprof\\py_epg_tests\\data\\banners\\wide_valid.jpg")
    # print r.content

    # banner = rest.download_file(rest.base_media_url + "banners/444/wide_banner.jpeg")
    # print (binascii.crc32(banner) & 0xFFFFFFFF)
    # filename = "C:\\Users\\Alexey.Tanana\\Documents\\workspace\\satprof\\py_epg_tests\\data\\banners\\wide_valid2.jpg"
    # buf = open(filename,'rb').read()
    # print (binascii.crc32(buf) & 0xFFFFFFFF)

    print 'rest auth done'
    assert rest.compare_files_CRC("C:\\Users\\Alexey.Tanana\\Documents\\workspace\\satprof\\py_epg_tests\\data\\banners\\wide_valid.jpg", "banners/444/wide_banner.jpeg")


def setup_module():
    global rest
    rest = set_rest()
    # print rest
    # return rest



# def if_user_and_server_files_equal(user_path, server_path):
#     server_file = rest.download_file(rest.base_media_url + server_path)
#     server_file_crc = (binascii.crc32(server_file) & 0xFFFFFFFF)
#     user_file = open(user_path,'rb').read()
#     user_file_crc = (binascii.crc32(user_file) & 0xFFFFFFFF)
#     return server_file_crc == user_file_crc