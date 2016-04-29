# -*- coding: utf-8 -*-
from model.channel import Channel


class DbChannelHelper:

    def __init__(self, db):
        self.db = db

    def get_channels(self):
        channels = []
        cursor = self.db.connection.cursor()
        try:
            cursor.execute(
                "select id, name, service_id, epg_name, epg_channel.offset, provider, icon, allow_record, narrow_banner, wide_banner from epg_channel")
            for row in cursor:
                (id, name, service_id, epg_name, offset, provider, icon, allow_record, narrow_banner, wide_banner) = row
                channels.append(
                    Channel(id=str(id), name=name, service_id=str(service_id), epg_name=epg_name, offset=str(offset),
                            provider=provider, icon=icon, allow_record=bool(allow_record), narrow_banner=narrow_banner,
                            wide_banner=wide_banner))
            self.db.connection.commit()
        finally:
            cursor.close()
            # self.connection.close()
        return channels

    def count(self):
        cursor = self.db.connection.cursor()
        try:
            cursor.execute("select count(*) from epg_channel")
            count = cursor.fetchone()[0]
            self.db.connection.commit()
        finally:
            cursor.close()
            # self.connection.close()
        # print count, type(count), int(count), type(count)
        return int(count)