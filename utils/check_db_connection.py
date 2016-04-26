# -*- coding: utf-8 -*-
import psycopg2


connection = psycopg2.connect(database='epg', user='epg', password='123', host='10.130.8.159', port='5432')

try:
    cursor = connection.cursor()
    cursor.execute("select * from epg_channel")
    for row in cursor.fetchall():
        print row
finally:
    connection.close()