# -*- coding: utf-8 -*-
import requests


class RestApi:

    def __init__(self, base_url):
        self.session = requests.Session()
        self.base_url = base_url

    def auth(self, username, password):
        session = self.session
        url = self.base_url + 'auth/login/?next=/epg/'
        r = session.get(url)
        for line in r.text.splitlines():
            if 'csrfmiddlewaretoken' in line:
                token = line.split("'")[-2]
                break

        data = {'csrfmiddlewaretoken': token,
                'username': username,
                'password': password}
        r = session.post(url, data=data, cookies=session.cookies)

        url = self.base_url + 'epg/'
        r = session.get(url, cookies=session.cookies)
        print r.text
        # print session.cookies
        # print data

    def is_valid(self):
        # try:
        #     self.wd.current_url
        #     return True
        # except:
        #     return False
        pass

    def destroy(self):
        #     self.connection.close()
        pass