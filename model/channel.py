# -*- coding: utf-8 -*-
from sys import maxsize
# from random import randint
import os.path
from random import randint, choice
from utils.file_util import abs_path_to_file
import hashlib
import binascii
# from fixture.rest import RestApi
# from tests import *


class Channel:
    def __init__(self, id=None, name=None, service_id=None, epg_name=None, offset="0", provider='', languages=None, allow_record=False, icon={"user_file": None, "server_file": None}, narrow_banner={"user_file": '', "server_file": ''}, wide_banner={"user_file": '', "server_file": ''}):
        self.id = id
        self.name = name
        self.service_id = service_id
        self.epg_name = epg_name
        self.offset = offset
        self.provider = provider
        self.languages = languages
        self.allow_record = allow_record
        self.icon = icon
        self.narrow_banner = narrow_banner
        self.wide_banner = wide_banner

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

    def __repr__(self):
        # return "%s, %s" % (self.id, self.name)
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.id, self.name, self.service_id, self.epg_name, self.provider, self.languages, self.allow_record, self.icon, self.narrow_banner, self.wide_banner)
        # return "%s, %s, %s, %s" % (self.id, unicode(self.name, 'utf-8').encode('utf-8'), self.service_id, self.epg_name)

    def __eq__(self, other):
        return self.name == other.name and \
               (self.id is None or other.id is None or self.id == other.id) and \
               (self.service_id == other.service_id) and \
               (self.epg_name == other.epg_name) and \
               (self.offset == other.offset) and \
               ((self.provider == other.provider) or ((self.provider is None or self.provider is '') and (other.provider is None or other.provider is ''))) and \
               (self.languages == other.languages) and \
               (self.allow_record == other.allow_record) and \
               ((self.icon["server_file"] == other.icon["server_file"]) or \
                (self.icon["server_file"] is None or self.icon["server_file"] is '') or \
                 (other.icon["server_file"] is None or other.icon["server_file"] is '')) and \
                ((self.narrow_banner["server_file"] == other.narrow_banner["server_file"]) or \
                 (self.narrow_banner["server_file"] is None or self.narrow_banner["server_file"] is '') or \
                  (other.narrow_banner["server_file"] is None or other.narrow_banner["server_file"] is '')) and \
                 ((self.wide_banner["server_file"] == other.wide_banner["server_file"]) or \
                  (self.wide_banner["server_file"] is None or self.wide_banner["server_file"] is '') or \
                   (other.wide_banner["server_file"] is None or other.wide_banner["server_file"] is ''))

def random_channel():
    return Channel(name='Channel_random_' + str(randint(0, 9999999)), service_id=str(randint(0, 65535)),
            epg_name='Epg_name_' + str(randint(0, 9999999)), offset=str(randint(-23, 23)),
            provider='Provider_' + str(randint(0, 9999999)),
            # languages=sorted(set([str(randint(1,4)) for l in range(randint(1,4))])),
            languages=str(randint(1,4)),
            allow_record=choice([bool(True), bool(False)]),
            icon={"user_file": abs_path_to_file(r"data/banners/icon_valid.jpg"), "server_file": None},
            narrow_banner={"user_file": abs_path_to_file(r"data/banners/narrow_valid.jpg"), "server_file": None},
            wide_banner={"user_file": abs_path_to_file(r"data/banners/wide_valid.jpg"), "server_file": None})