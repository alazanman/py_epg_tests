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
                            provider=provider, languages=self.get_channel_languages(id), allow_record=bool(allow_record),
                            icon={"server_file": icon, "user_file": None}, narrow_banner={"server_file": narrow_banner, "user_file": None},
                            wide_banner={"server_file": wide_banner, "user_file": None}))
                            # provider=provider, languages=self.get_channel_languages(id), allow_record=bool(allow_record),
                            # icon={"server_file": self.full_path_if_exists(icon), "user_file": None}, narrow_banner=self.full_path_if_exists(narrow_banner),
                            # wide_banner=self.full_path_if_exists(wide_banner)))
            self.db.connection.commit()
        finally:
            cursor.close()
            # self.connection.close()
        # print channels
        return channels


    def get_channel_languages(self, channel_id):
        languages = []
        cursor = self.db.connection.cursor()
        try:
            cursor.execute(
                "select language_id from epg_channel_languages where channel_id=" + str(channel_id))
            for row in cursor:
                languages.append(str(row[0]))
            self.db.connection.commit()
        finally:
            cursor.close()
        return languages

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

    # def full_path_if_exists(self, relative_path):
    #     # base_media_url = nose_config.load_config()['web']['baseUrl'] + "media/"
    #     global base_media_url
    #     if relative_path:
    #         return base_media_url + relative_path