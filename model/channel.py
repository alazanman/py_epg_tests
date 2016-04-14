# -*- coding: utf-8 -*-


class Channel:
    def __init__(self, name=None, service_id=None, epg_name=None, offset=None, provider=None, allow_record=None):
        self.name = name
        self.service_id = service_id
        self.epg_name = epg_name
        self.offset = offset
        self.provider = provider
        #self.allow_record = allow_record