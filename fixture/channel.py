# -*- coding: utf-8 -*-


class ChannelHelper:


    def __init__(self, app):
        self.app = app

    def create(self, channel):
        wd = self.app.wd
        self.open_channels_page()
        wd.find_element_by_link_text("Добавить").click()
        wd.find_element_by_id("id_name").click()
        wd.find_element_by_id("id_name").clear()
        wd.find_element_by_id("id_name").send_keys(channel.name)
        wd.find_element_by_id("id_service_id").click()
        wd.find_element_by_id("id_service_id").clear()
        wd.find_element_by_id("id_service_id").send_keys(channel.service_id)
        wd.find_element_by_id("id_epg_name").click()
        wd.find_element_by_id("id_epg_name").clear()
        wd.find_element_by_id("id_epg_name").send_keys(channel.epg_name)
        wd.find_element_by_id("id_offset").click()
        wd.find_element_by_id("id_offset").clear()
        wd.find_element_by_id("id_offset").send_keys(channel.offset)
        wd.find_element_by_id("id_provider").click()
        wd.find_element_by_id("id_provider").clear()
        wd.find_element_by_id("id_provider").send_keys(channel.provider)
        if not wd.find_element_by_xpath("//select[@id='id_languages']/option[@value='2']").is_selected():
            wd.find_element_by_xpath("//select[@id='id_languages']/option[@value='2']").click()
        if not wd.find_element_by_xpath("//select[@id='id_languages']/option[@value='3']").is_selected():
            wd.find_element_by_xpath("//select[@id='id_languages']/option[@value='3']").click()
        if not wd.find_element_by_xpath("//select[@id='id_languages']/option[@value='1']").is_selected():
            wd.find_element_by_xpath("//select[@id='id_languages']/option[@value='1']").click()
        if not wd.find_element_by_xpath("//select[@id='id_languages']/option[@value='4']").is_selected():
            wd.find_element_by_xpath("//select[@id='id_languages']/option[@value='4']").click()
        # if not wd.find_element_by_id("id_allow_record").is_selected():
        #            wd.find_element_by_id("id_allow_record").click()
        #        wd.find_element_by_id("banner-drag").click()
        #        wd.find_element_by_id("drop-select-input").click()
        #        wd.find_element_by_xpath("//form[@class='epg-channel-form']/fieldset/div[11]/div/img").click()
        #        wd.find_element_by_id("drop-select-input").click()
        wd.find_element_by_css_selector("button.btn.btn-success").click()

    def delete_first_channel(self):
        wd = self.app.wd
        self.open_channels_page()
        wd.find_element_by_xpath("//*[@id='content']/div[2]/table/tbody/tr[1]/td[2]/a").click()
        wd.find_element_by_id("del").click()
        wd.find_element_by_xpath("//*[@id='content']/div/div/div/div[2]/form/div/button").click()

    def open_channels_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Каналы").click()