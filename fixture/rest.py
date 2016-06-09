# -*- coding: utf-8 -*-
import requests
# from fixture.session_rest import RestSessionHelper


class RestApi:

    def __init__(self, base_url):
        # self.session = requests.Session()
        # self.rest_session = RestSessionHelper(self)
        self.session = requests.session()
        self.base_url = base_url

    def auth(self, username, password):
        # global base_url
        session = self.session
        url = self.base_url + 'auth/login/?next=/epg/'  # ???????????????????????????????????????????????????????????????????????????????????????
        print url
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
        print r.text[-290:-260]
        return session


    # def open_home_page(self):
    #     # session = self.session
    #     url = self.base_url + 'epg/'
    #     # url = self.base_url + 'auth/login/?next=/epg/'
    #     r = self.session.get(url, cookies=self.session.cookies)

    # def compare_user_and_server_files(self, user_file_path, server_file_path):
        # session = self.auth()


    # def auth(self, username, password):
    #     session = self.session
    #     url = self.base_url + 'auth/login/?next=/epg/'
    #     r = session.get(url)
    #     for line in r.text.splitlines():
    #         if 'csrfmiddlewaretoken' in line:
    #             token = line.split("'")[-2]
    #             break
    #
    #     data = {'csrfmiddlewaretoken': token,
    #             'username': username,
    #             'password': password}
    #     r = session.post(url, data=data, cookies=session.cookies)
    #
    #     url = self.base_url + 'epg/'
    #     r = session.get(url, cookies=session.cookies)
    #     print r.text[-290:-260]
    #     return session

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