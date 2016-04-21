# -*- coding: utf-8 -*-
from sys import maxsize


class Channel:
    def __init__(self, id=None, name=None, service_id=None, epg_name=None, offset=None, provider=None, allow_record=None):
        self.id = id
        self.name = name
        self.service_id = service_id
        self.epg_name = epg_name
        self.offset = offset
        self.provider = provider
        #self.allow_record = allow_record

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

    def __repr__(self):
        return "%s, %s" % (self.id, self.name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

