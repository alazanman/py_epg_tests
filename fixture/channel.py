# -*- coding: utf-8 -*-
from time import sleep
from model.channel import Channel


class ChannelHelper:


    def __init__(self, app):
        self.app = app

    def create(self, channel):
        wd = self.app.wd
        self.open_channels_page()
        self.click_add_channel()
        self.fill_channel_form(channel)
        self.submit_channel_form()
        sleep(1)
        self.channel_cache = None

    def delete_first_channel(self):
        self.delete_channel_by_index(0)

    def delete_channel_by_index(self, index):
        wd = self.app.wd
        self.open_channels_page()
        self.click_channel_in_list(index)
        self.click_delete_button()
        self.confirm_delete_button()
        self.channel_cache = None

    def delete_channel_by_id(self, id):
        wd = self.app.wd
        self.open_channels_page()
        self.click_channel_in_list_by_id(id)
        self.click_delete_button()
        self.confirm_delete_button()
        self.channel_cache = None

    def edit_channel_by_id(self, id, new_channel):
        wd = self.app.wd
        self.open_channels_page()
        self.click_channel_in_list_by_id(id)
        self.fill_channel_form(new_channel)
        self.submit_channel_form()
        self.channel_cache = None

    def edit_channel_by_index(self, index, new_channel):
        wd = self.app.wd
        self.open_channels_page()
        self.click_channel_in_list(index)
        self.fill_channel_form(new_channel)
        self.submit_channel_form()
        self.channel_cache = None

    def edit_first_channel(self, new_channel):
        self.edit_channel_by_index(0, new_channel)

    def click_add_channel(self):
        wd = self.app.wd
        # wd.find_element_by_link_text("Добавить").click()
        wd.find_element_by_xpath("//*[@href='/epg/channel/add/']").click()

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

    def click_channel_in_list(self, index):
        wd = self.app.wd
        wd.find_element_by_xpath("//*[@id='content']/div[2]/table/tbody/tr[" + str(index+1) + "]/td[2]/a").click()

    def click_channel_in_list_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_xpath("//*[@href='/epg/channel/" + str(id) + "/']").click()

    def submit_channel_form(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("button.btn.btn-success").click()
        # wd.find_element_by_xpath("//*[@id='content']/form/fieldset/div[12]/div[2]/button").click()

    def click_delete_button(self):
        wd = self.app.wd
        wd.find_element_by_id("del").click()

    def confirm_delete_button(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//*[@id='content']/div/div/div/div[2]/form/div/button").click()

    def open_channels_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith('/epg/channel/'):            # MOVE TO EPG CONSTANTS, PARAMETRISE URL
            wd.execute_script("window.scrollTo(0, 0)")
            wd.find_element_by_xpath("//*[@id='menu']/div[1]/div[2]/a[1]").click()
        #wd.find_element_by_link_text("Каналы").click()

    def count(self):
        wd = self.app.wd
        self.open_channels_page()
        return len(wd.find_elements_by_xpath("//*[@id='content']/div[2]/table/tbody/tr[.]/td[2]/a"))

    channel_cache = None

    def get_channels(self):
        if self.channel_cache is None:
            wd = self.app.wd
            self.open_channels_page()
            self.channel_cache = []
            for element in wd.find_elements_by_xpath("//*[@id='content']/div[2]/table/tbody/tr[.]/td[2]/a"):
                text = element.text
                id = element.get_attribute("href").split('/')[-2]
                # print "id =", id
                self.channel_cache.append(Channel(name=text, id=id))
        return list(self.channel_cache)

    # def get_channel_list(self):
    #     wd = self.app.wd
    #     self.open_channels_page()
    #     channels = []
    #     for element in wd.find_elements_by_xpath("//*[@id='content']/div[2]/table/tbody/tr[.]/td[2]/a"):
    #         text = element.text
    #         id = element.get_attribute("href").split('/')[-2]
    #         #print "id =", id
    #         channels.append(Channel(name=text, id=id))
    #     return channels

