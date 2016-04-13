# -*- coding: utf-8 -*-
import unittest

from fixture.application import Application
from model.channel import Channel


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class test_create_channel(unittest.TestCase):
    def setUp(self):
        self.app = Application()

    def test_create_channel(self):
        self.app.login("root", "123")
        self.app.create_channel(
            Channel(name="1234", service_id="2345", epg_name="epg_name2", offset="3", provider="Provider"))
        self.app.logout()

    def tearDown(self):
        self.app.destroy()


if __name__ == '__main__':
    unittest.main()
