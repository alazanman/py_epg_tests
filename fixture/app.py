# -*- coding: utf-8 -*-
import binascii
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from fixture.session import SessionHelper
from fixture.channel import ChannelHelper
from selenium.common.exceptions import NoAlertPresentException
from time import sleep

class Application:

    def __init__(self, browser, base_url):
        if browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognised browser %s" % browser)
        # self.wd.implicitly_wait(10)
        self.session = SessionHelper(self)
        self.channel = ChannelHelper(self)
        self.base_url = base_url

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    # def wait(self):
    #     return WebDriverWait(self.wd, 10)

    def wait_for_element_by_xpath(self, xpath, secs):
        return WebDriverWait(self.wd, secs).until(
            lambda x: x.find_element_by_xpath(xpath))

    def ctrl_click(self, element):
        ActionChains(self.wd) \
            .key_down(Keys.CONTROL) \
            .click(element) \
            .key_up(Keys.CONTROL) \
            .perform()

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    # def current_url(self):
    #     wd = self.wd
    #     return wd.current_url()

    def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException:
            return False
        return True

    def close_alert(self):
        if self.is_alert_present():
            # sleep(3)
            try:
                alert = self.wd.switch_to_alert()
            except:
                print "Unable to locate alert message!"
            alert.accept()
            # return alert.text
            return True

    def destroy(self):
        self.wd.quit()