# -*- coding: utf-8 -*-
from sys import maxsize


class Channel:
    def __init__(self, id=None, name=None, service_id=None, epg_name=None, offset=None, provider=None, icon=None, allow_record=None, narrow_banner=None, wide_banner=None):
        self.id = id
        self.name = name
        self.service_id = service_id
        self.epg_name = epg_name
        self.offset = offset
        self.provider = provider
        self.icon = icon
        self.allow_record = allow_record
        self.narrow_banner = narrow_banner
        self.wide_banner = wide_banner

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

    def __repr__(self):
        return "%s, %s, %s, %s" % (self.id, self.name, self.service_id, self.epg_name)
        # return "%s, %s, %s, %s" % (self.id, unicode(self.name, 'utf-8').encode('utf-8'), self.service_id, self.epg_name)

    def __eq__(self, other):
        # return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name
        # print "self.id, self.name, other.id, other.name: %s, %s, %s, %s" % (self.id, other.id, self.name, other.name)
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name
