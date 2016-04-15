# -*- coding: utf-8 -*-
from time import sleep


def test_delete_first_channel(app):
    sleep(1)
    app.channel.delete_first_channel()