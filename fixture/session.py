# -*- coding: utf-8 -*-


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_id("id_username").click()
        wd.find_element_by_id("id_username").clear()
        wd.find_element_by_id("id_username").send_keys(username)
        wd.find_element_by_id("id_password").click()
        wd.find_element_by_id("id_password").clear()
        wd.find_element_by_id("id_password").send_keys(password)
        wd.find_element_by_id("send_data").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//*[@id='drop1']").click()
        wd.find_element_by_xpath("//*[@id='appRoot']/div[1]/div/div[2]/ul[2]/li[1]/ul/li[1]/a").click()

    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in() > 0:
            self.logout()

    def ensure_login(self, username, password):
        wd = self.app.wd
        if not (self.is_logged_in() > 0):
            self.login(username, password)

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_xpath("//*[@id='drop1']"))