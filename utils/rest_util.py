# -*- coding: utf-8 -*-
import requests
from random import randint


# url = 'http://ES_search_demo.com/document/record/_search?pretty=true'
# data = '{"query":{"bool":{"must":[{"text":{"record.document":"SOME_JOURNAL"}},{"text":{"record.articleTitle":"farmers"}}],"must_not":[],"should":[]}},"from":0,"size":50,"sort":[],"facets":{}}'
# response = requests.get(url, data=data)

global token

url = 'http://10.130.8.159/epg/'
response = requests.get(url)
for line in response.text.splitlines():
    if 'csrfmiddlewaretoken' in line:
        token = line.split("'")[-2]
        print token

# <input type='hidden' name='csrfmiddlewaretoken' value='X5LMyCIDzEhzgdyOaftNZUjtSdKfgwyS' />

url = 'http://10.130.8.159/auth/login/'
data = '{"csrfmiddlewaretoken": "' + token + '", ' \
        '"username": "root", ' \
        '"password": "123" }'
        # "username": "' + token + '", ' \
        # "password": "' + token + '", ' \
response = requests.get(url, data=data)
print response.text



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