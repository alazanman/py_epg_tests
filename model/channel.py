# -*- coding: utf-8 -*-
from sys import maxsize
import hashlib
import binascii
# from fixture.rest import RestApi
# from tests import *


class Channel:
    def __init__(self, id=None, name=None, service_id=None, epg_name=None, offset="0", provider=None, languages=None, allow_record=False, icon={"user_file": None, "server_file": None}, narrow_banner=None, wide_banner=None):
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
        return "%s, %s, %s, %s, %s, %s, %s, %s" % (self.id, self.name, self.service_id, self.epg_name, self.languages, self.icon, self.narrow_banner, self.wide_banner)
        # return "%s, %s, %s, %s" % (self.id, unicode(self.name, 'utf-8').encode('utf-8'), self.service_id, self.epg_name)

    def __eq__(self, other):
        # return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name
        # print "self.id, self.name, other.id, other.name: %s, %s, %s, %s" % (self.id, other.id, self.name, other.name)
        # from nose_config import set_rest
        # global rest
        # rest = set_rest()
        # print "self.icon, other.icon: %s, %s" % (self.icon, other.icon)
        # print self.icon["server_file"], self.icon["server_file"]
        return self.name == other.name and \
               (self.id is None or other.id is None or self.id == other.id) and \
               (self.service_id == other.service_id) and \
               (self.epg_name == other.epg_name) and \
               (self.offset == other.offset) and \
               (self.provider == other.provider) or ((self.provider is None or self.provider is '') and (other.provider is None or other.provider is '')) and \
               (self.languages == other.languages) and \
               (self.allow_record == other.allow_record) and \
               (self.icon["server_file"] is None or self.icon["server_file"] is '' or
                 other.icon["server_file"] is None or other.icon["server_file"] is '' or
                self.icon["server_file"] == other.icon["server_file"]) and \
                (self.narrow_banner["server_file"] is None or self.narrow_banner["server_file"] is '' or
                other.narrow_banner["server_file"] is None or other.narrow_banner["server_file"] is '' or
                self.narrow_banner["server_file"] == other.narrow_banner["server_file"]) and \
                (self.wide_banner["server_file"] is None or self.wide_banner["server_file"] is '' or
                other.wide_banner["server_file"] is None or other.wide_banner["server_file"] is '' or
                 self.narrow_banner["server_file"] == other.narrow_banner["server_file"])
                # rest.compare_files_CRC(self.icon["server_file"], other.icon["server_file"]) and \
                # rest.compare_files_CRC(self.narrow_banner["server_file"], other.narrow_banner["server_file"])) and \
                # rest.compare_files_CRC(self.wide_banner["server_file"], other.wide_banner["server_file"])))


# ((self.icon["server_file"] is None or self.icon["server_file"] is '') and
#  (other.icon["server_file"] is None or other.icon["server_file"] is '') or
#  self.icon["server_file"] == other.icon["server_file"]) and \
# ((self.narrow_banner["server_file"] is None or self.narrow_banner["server_file"] is '') and
#  (other.narrow_banner["server_file"] is None or other.narrow_banner["server_file"] is '') or
#  self.narrow_banner["server_file"] == other.narrow_banner["server_file"]) and \
# ((self.wide_banner["server_file"] is None or self.wide_banner["server_file"] is '') and
#  (other.wide_banner["server_file"] is None or other.wide_banner["server_file"] is '') or
#  self.narrow_banner["server_file"] == other.narrow_banner["server_file"])

        # (self.id is None or other.id is None or self.id == other.id) and \
# (self.service_id is None or other.service_id is None or self.service_id == other.service_id) and \
# (self.epg_name is None or other.epg_name is None or self.epg_name == other.epg_name) and \
# (self.offset is None or other.offset is None or self.offset == other.offset) and \
# (self.provider is None or other.provider is None or self.provider == other.provider) and \
# (self.languages is None or other.languages is None or self.languages == other.languages) and \
# (self.allow_record is None or other.allow_record is None or self.allow_record == other.allow_record) and \
# (self.icon["server_file"] is None or self.icon["server_file"] is '' or
#  other.icon["server_file"] is None or other.icon["server_file"] is '' or
#  self.icon["server_file"] == other.icon["server_file"]) and \
# (self.narrow_banner["server_file"] is None or self.narrow_banner["server_file"] is '' or
#  other.narrow_banner["server_file"] is None or other.narrow_banner["server_file"] is '' or
#  self.narrow_banner["server_file"] == other.narrow_banner["server_file"]) and \
# (self.wide_banner["server_file"] is None or self.wide_banner["server_file"] is '' or
#  other.wide_banner["server_file"] is None or other.wide_banner["server_file"] is '' or
#  self.narrow_banner["server_file"] == other.narrow_banner["server_file"])
# # rest.compare_files_CRC(self.icon["server_file"], other.icon["server_file"]) and \
# # rest.compare_files_CRC(self.narrow_banner["server_file"], other.narrow_banner["server_file"])) and \
# # rest.compare_files_CRC(self.wide_banner["server_file"], other.wide_banner["server_file"])))