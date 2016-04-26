# -*- coding: utf-8 -*-
import psycopg2


class DbFixture:

    def __init__(self, database, user, password, host, port):
        self.database = database
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connection = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)

    def destroy(self):
        self.connection.close()