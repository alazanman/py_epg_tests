# -*- coding: utf-8 -*-


class Channel:
    def __init__(self, name, service_id, epg_name, offset, provider):
        self.name = name
        self.service_id = service_id
        self.epg_name = epg_name
        self.offset = offset
        self.provider = provider
