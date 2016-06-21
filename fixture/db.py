# -*- coding: utf-8 -*-
import psycopg2
# from model.channel import Channel
from fixture.channel_db import DbChannelHelper
# import nose_config

# global base_media_url
# base_media_url = nose_config.load_config()['web']['baseUrl'] + "media/"

class DbFixture:

    def __init__(self, database, user, password, host, port):
        self.database = database
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connection = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
        self.connection.autocommit = True
        self.channel = DbChannelHelper(self)
        psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
        psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)

    def is_valid(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("select now()")
            cursor.close()
            return True
        except:
            return False

    def destroy(self):
        self.connection.close()


# print DbFixture(database='epg', user='epg', password='123', host='10.130.8.159', port='5432').get_channels_count()