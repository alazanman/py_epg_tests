# -*- coding: utf-8 -*-


class ChannelHelper:


    def __init__(self, app):
        self.app = app

    def create(self, channel):
        wd = self.app.wd
        self.open_channels_page()
        wd.find_element_by_link_text("Добавить").click()
        self.fill_channel_form(channel)
        wd.find_element_by_css_selector("button.btn.btn-success").click()

    def fill_channel_form(self, channel):
        wd = self.app.wd
        self.enter_text("id_name", channel.name)
        self.enter_text("id_service_id", channel.service_id)
        self.enter_text("id_epg_name", channel.epg_name)
        self.enter_text("id_offset", channel.offset)
        self.enter_text("id_provider", channel.provider)
        # wd.find_element_by_xpath("//select[@id='id_languages']/option[@value='2']").click()
        # wd.find_element_by_xpath("//select[@id='id_languages']/option[@value='3']").click()
        # wd.find_element_by_xpath("//select[@id='id_languages']/option[@value='1']").click()
        # wd.find_element_by_xpath("//select[@id='id_languages']/option[@value='4']").click()
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


    def enter_text(self, field_id, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_id(field_id).click()
            wd.find_element_by_id(field_id).clear()
            wd.find_element_by_id(field_id).send_keys(text)

    def delete_first_channel(self):
        wd = self.app.wd
        self.open_channels_page()
        self.click_first_channel_in_list()
        wd.find_element_by_id("del").click()
        wd.find_element_by_xpath("//*[@id='content']/div/div/div/div[2]/form/div/button").click()

    def click_first_channel_in_list(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//*[@id='content']/div[2]/table/tbody/tr[1]/td[2]/a").click()

    def edit_first_channel(self, new_channel):
        wd = self.app.wd
        self.open_channels_page()
        self.click_first_channel_in_list()
        self.fill_channel_form(new_channel)
        wd.find_element_by_xpath("//*[@id='content']/form/fieldset/div[12]/div[2]/button").click()

    def open_channels_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith('/epg/channel/'):            # MOVE TO EPG CONSTANTS, PARAMETRISE URL
            wd.find_element_by_xpath("//*[@id='menu']/div[1]/div[2]/a[1]").click()
        #wd.find_element_by_link_text("Каналы").click()

    def count(self):        # MAKE IT FROM DB
        pass