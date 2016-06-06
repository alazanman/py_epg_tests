# -*- coding: utf-8 -*-
from sys import maxsize


class Channel:
    def __init__(self, id=None, name=None, service_id=None, epg_name=None, offset="0", provider=None, languages=None, allow_record=False, icon=None, narrow_banner=None, wide_banner=None):
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
        # print "self.offset, other.offset: %s, %s" % (self.offset, other.offset)
        return self.name == other.name and \
               (self.id is None or other.id is None or self.id == other.id) and \
               (self.service_id is None or other.service_id is None or self.service_id == other.service_id) and \
               (self.epg_name is None or other.epg_name is None or self.epg_name == other.epg_name) and \
               (self.offset is None or other.offset is None or self.offset == other.offset) and \
               (self.provider is None or other.provider is None or self.provider == other.provider) and \
               (self.languages is None or other.languages is None or self.languages == other.languages) and \
               (self.allow_record is None or other.allow_record is None or self.allow_record == other.allow_record)
        # and \
               # (self.icon is None or other.icon is None or self.icon == other.icon) and \
               # (self.narrow_banner is None or other.narrow_banner is None or self.narrow_banner == other.narrow_banner) and \
               # (self.wide_banner is None or other.wide_banner is None or self.wide_banner == other.wide_banner)