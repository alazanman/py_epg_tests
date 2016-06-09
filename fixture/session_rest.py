# # -*- coding: utf-8 -*-
#
#
# class RestSessionHelper:
#
#     def __init__(self, rest):
#         self.rest = rest
#         # self.session = session
#
#     def auth(self, username, password):
#         global base_url
#         session = self.rest.session
#         url = self.rest.base_url + 'auth/login/?next=/epg/'   #???????????????????????????????????????????????????????????????????????????????????????
#         print url
#         r = session.get(url)
#         for line in r.text.splitlines():
#             if 'csrfmiddlewaretoken' in line:
#                 token = line.split("'")[-2]
#                 break
#
#         data = {'csrfmiddlewaretoken': token,
#                 'username': username,
#                 'password': password}
#         r = session.post(url, data=data, cookies=session.cookies)
#
#         url = self.base_url + 'epg/'
#         r = session.get(url, cookies=session.cookies)
#         print r.text[-290:-260]
#         return session
#
#     # def ensure_auth(self, username, password):
#     #     if not (self.is_logged_in() > 0):
#     #         self.login(username, password)
#     #
#     # def is_logged_in(self):
#     #     wd = self.app.wd
#     #     return len(wd.find_elements_by_xpath("//*[@id='drop1']"))