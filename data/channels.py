# -*- coding: utf-8 -*-
from model.channel import Channel
from random import randint
from fixture.utils import random_string


testdata = [
    Channel(name='Channel' + str(randint(0, 9999)), service_id="2345", epg_name="epg_name2", offset="3", provider="Provider"),
    Channel(name='Channel' + str(randint(0, 9999)), service_id="1111", epg_name="epg_name1111", offset="1", provider="Provider"),
    # Channel(name="", service_id="", epg_name="", offset="", provider="")
]