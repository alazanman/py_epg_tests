# -*- coding: utf-8 -*-
__author__ = 'Aleksey Tanana'

from selenium.webdriver.firefox.webdriver import WebDriver

class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("root").click()
        wd.find_element_by_link_text("Выйти").click()

    def login(self, username, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_id("id_username").click()
        wd.find_element_by_id("id_username").clear()
        wd.find_element_by_id("id_username").send_keys(username)
        wd.find_element_by_id("id_password").click()
        wd.find_element_by_id("id_password").clear()
        wd.find_element_by_id("id_password").send_keys(password)
        wd.find_element_by_id("send_data").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://10.130.8.116/epg/")

    def destroy(self):
        self.wd.quit()