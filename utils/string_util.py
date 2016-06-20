# -*- coding: utf-8 -*-
import random, string
from model.channel import Channel


def random_string(prefix, maxlen, spec=False):
    # spec_symbols = r'“[|]’~<!--@/*$%^&#*/()?>,.*/\№_={":' + r"';`}"
    # channel_name, Provider = '[|]~<!--@/*$%^&#*/()?>,.*/\№_={":' + r"';`}"
    # symbols = string.ascii_letters + string.digits + " "*10 + string.punctuation + spec_symbols
    spec_symbols = r'[|]~<!--@/*$%^&#*/()?>,.*/\№_={":' + r"';`}"
    symbols = string.ascii_letters + string.digits
    if spec:
        symbols = symbols + spec_symbols
    if maxlen > len(prefix):
        random_len = maxlen - len(prefix)
    else:
        random_len = 0
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(1, random_len + 1))])

def random_string_fixed_len(prefix, maxlen):
    # spec_symbols = r'“[|]’~<!--@/*$%^&#*/()?>,.*/\№_={":' + r"';`}"
    # symbols = string.ascii_letters + string.digits + " "*10 + string.punctuation + spec_symbols
    symbols = string.ascii_letters + string.digits
    if maxlen > len(prefix):
        random_len = maxlen - len(prefix)
    else:
        print "Prefix is longer than whole string!"
        random_len = 0
    return prefix + "".join([random.choice(symbols) for i in range(random_len)])

# # pairwise
# testdata2 = [
#     Channel(name=name, service_id=service_id, epg_name=epg_name, offset=offset, provider=provider)
#     for name in ["", random_string("name", 10)]
#     for service_id in ["", random_string("service_id", 10)]
#     for epg_name in ["", random_string("epg_name", 10)]
#     for offset in ["", random.randint(0, 10)]
#     for provider in ["", random_string("provider", 10)]
# ]
# # print testdata2