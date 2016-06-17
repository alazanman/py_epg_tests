# -*- coding: utf-8 -*-
import requests
import binascii
from fixture.channel_rest import RestChannelHelper


class RestApi:

    def __init__(self, base_url):
        self.session = requests.session()
        self.base_url = base_url
        self.base_media_url = self.base_url + "media/"
        self.channel = RestChannelHelper(self)

    def auth(self, username, password):
        session = self.session
        r = session.get(self.base_url + "epg/")
        # print 'csrftoken:', session.cookies['csrftoken']
        data = {'csrfmiddlewaretoken': session.cookies['csrftoken'],
                'username': username,
                'password': password}
        session.post(self.base_url + "auth/login/?next=/epg/", data=data, cookies=session.cookies)
        print session.get(self.base_url + "epg/", cookies=session.cookies).text[-290:-260]
        return session

    def download_file(self, url):
        session = self.session
        r = session.get(url)
        return r.content

    def compare_files_CRC(self, file_path1, file_path2):
        if (file_path1 == None or file_path1 == '') and (file_path2 == None or file_path2 == ''):
            # print "1:", file_path1, file_path2
            return True
        elif file_path1 == None or file_path2 == None:
            # print "2:", file_path1, file_path2
            return False
        else:
            try:
                file1 = open(file_path1, 'rb').read()
                # print "1", (binascii.crc32(file1) & 0xFFFFFFFF)
            except:
                try:
                    file1 = self.download_file(self.base_media_url + file_path1)
                    # print "2", (binascii.crc32(file1) & 0xFFFFFFFF)
                except:
                    print "Something went wrong while trying to read file_1!"
                    # raise "5"
                    return
            file1_crc = (binascii.crc32(file1) & 0xFFFFFFFF)
            try:
                file2 = open(file_path2, 'rb').read()
                # print "3", (binascii.crc32(file2) & 0xFFFFFFFF)
            except:
                try:
                    file2 = self.download_file(self.base_media_url + file_path2)
                    # print "4", (binascii.crc32(file2) & 0xFFFFFFFF)
                except:
                    print "Something went wrong while trying to read file_2!"
                    # raise "6"
                    return
            file2_crc = (binascii.crc32(file2) & 0xFFFFFFFF)
            return file1_crc == file2_crc


        # def open_home_page(self):
    #     # session = self.session
    #     url = self.base_url + 'epg/'
    #     # url = self.base_url + 'auth/login/?next=/epg/'
    #     r = self.session.get(url, cookies=self.session.cookies)

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