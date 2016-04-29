# -*- coding: utf-8 -*-
import psycopg2
from model.channel import Channel
from timeit import timeit


def test_channels_db_matches_ui(app, db):
    print timeit(lambda: app.channel.get_channels(), number=1)
    ui_list = app.channel.get_channels()
    print timeit(lambda: db.get_channels(), number=1)
    db_list = db.get_channels()
    print "ui_list"
    print ui_list
    print "db_list"
    print db_list
    assert sorted(ui_list, key=Channel.id_or_max) == sorted(db_list, key=Channel.id_or_max)


# connection = psycopg2.connect(database='epg', user='epg', password='123', host='10.130.8.159', port='5432')
#
# try:
#     cursor = connection.cursor()
#     cursor.execute("select * from epg_channel")
#     for row in cursor.fetchall():
#         print row
# finally:
#     connection.close()
#
