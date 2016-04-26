# -*- coding: utf-8 -*-
import random, string
from model.channel import Channel


def random_string(prefix, maxlen):
    spec_symbols = r'“[|]’~<!--@/*$%^&#*/()?>,.*/\№_={":' + r"';`}"
    symbols = string.ascii_letters + string.digits + " "*10 + string.punctuation + spec_symbols
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
# print random_string("test", 1000)


# pairwise
testdata2 = [
    Channel(name=name, service_id=service_id, epg_name=epg_name, offset=offset, provider=provider)
    for name in ["", random_string("name", 10)]
    for service_id in ["", random_string("service_id", 10)]
    for epg_name in ["", random_string("epg_name", 10)]
    for offset in ["", random.randint(0, 10)]
    for provider in ["", random_string("provider", 10)]
]
# print testdata2
