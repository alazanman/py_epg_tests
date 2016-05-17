# -*- coding: utf-8 -*-
import requests
from random import randint


global token, session

# def rest_auth()
session = requests.Session()

url = 'http://10.130.8.159/auth/login/?next=/epg/'
r = session.get(url)
for line in r.text.splitlines():
    if 'csrfmiddlewaretoken' in line:
        token = line.split("'")[-2]

data = {'csrfmiddlewaretoken': token,
        'username': 'root',
        'password': '123' }
r = session.post(url, data=data, cookies=session.cookies)

url = 'http://10.130.8.159/epg/'
r = session.get(url, cookies=session.cookies)
print r.text
print session.cookies
print data


# url = 'http://10.130.8.159/epg/channel/add/'
# data = '{"csrfmiddlewaretoken":"FeXQq2VLq47v8n0tHPHVvMMVbsk3tJY3", ' \
#         '"name"="Channel_name_' + str(randint(0, 9999999)) + '", '\
#         '"service_id"="' + str(randint(0, 65535)) + '", '\
#         '"epg_name"="Epg_name_' + str(randint(0, 9999999)) + '", ' \
#         '"offset"="' + str(randint(-23, 23)) + '", '\
#         '"provider"="Provider_' + str(randint(0, 9999999)) + '", ' \
#         '"languages"="' + str(randint(1, 4)) + '", ' \
#         '"allow_record"="on" }'
#
# response = requests.get(url, data=data)
# print response.text