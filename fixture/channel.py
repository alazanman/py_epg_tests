# -*- coding: utf-8 -*-
from time import sleep
import os
import pyautogui
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
        self.channel_cache = None

    # def delete_first_channel(self):
    #     self.delete_channel_by_index(0)

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

    def edit_channel_by_id(self, channel_edited):
        wd = self.app.wd
        self.open_channels_page()
        self.click_channel_in_list_by_id(channel_edited.id)
        self.fill_channel_form(channel_edited)
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
        # deselect languages
        for element in wd.find_elements_by_xpath("//select[@id='id_languages']/option"):
            if element.is_selected():
                element.click()
        # select languages
        for language in channel.languages:
            wd.find_element_by_xpath("//select[@id='id_languages']/option[@value='" + language + "']").click()
        # select/deselect allow_record if needed
        if channel.allow_record != wd.find_element_by_id("id_allow_record").is_selected():
            wd.find_element_by_id("id_allow_record").click()
        wd.execute_script("window.scrollBy(0, 1000)")

        # icon, narrow_banner, wide_banner elements in series
        pictures = [channel.icon["user_file"],
                    channel.narrow_banner["user_file"],
                    channel.wide_banner["user_file"]]
        drop_field_new = ["//*[@id='content']/form/fieldset/div[9]/div/img",
                          "//*[@id='content']/form/fieldset/div[10]/div/img",
                          "//*[@id='content']/form/fieldset/div[11]/div/img"]
        picture_delete_buttons = ["//*/label[@for='icon-clear_id']",
                               "//*/label[@for='narrow_banner-clear_id']",
                               "//*/label[@for='wide_banner-clear_id']"]
        drop_field_after_delete_pic = ["//*[@id='content']/form/fieldset/div[9]/div[2]/div[1]/div[1]/img[2]",
                                       "//*[@id='content']/form/fieldset/div[10]/div[2]/div[1]/div[1]/img[2]",
                                       "//*[@id='content']/form/fieldset/div[11]/div[2]/div[1]/div[1]/img[2]"]
        for i in range(0, 3):
            if pictures[i]:
                if wd.find_elements_by_xpath(drop_field_new[i]):
                    self.add_file_pyautogui(drop_field_new[i], pictures[i])
                elif wd.find_elements_by_xpath(picture_delete_buttons[i]):
                    wd.find_element_by_xpath(picture_delete_buttons[i]).click()
                    self.add_file_pyautogui(drop_field_after_delete_pic[i], pictures[i])
            else:
                if wd.find_elements_by_xpath(picture_delete_buttons[i]):
                    wd.find_element_by_xpath(picture_delete_buttons[i]).click()

    def add_file_pyautogui(self, xpath, file_path):
        if file_path:
            self.app.wd.find_element_by_xpath(xpath).click()
            sleep(1)
            pyautogui.typewrite(os.path.abspath(os.path.join(os.getcwd(), file_path)))
            pyautogui.press('enter')

    def enter_text(self, field_id, text):
        wd = self.app.wd
        wd.find_element_by_id(field_id).click()
        wd.find_element_by_id(field_id).clear()
        if text is not None:
            wd.find_element_by_id(field_id).send_keys(text)

    def click_channel_in_list(self, index):
        wd = self.app.wd
        wd.find_element_by_xpath("//*[@id='content']/div[2]/table/tbody/tr[" + str(index+1) + "]/td[2]/a").click()

    def click_channel_in_list_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_xpath("//*[@href='/epg/channel/" + str(id) + "/']").click()

    def submit_channel_form(self):
        wd = self.app.wd
        sleep(1)
        wd.find_element_by_css_selector("button.btn.btn-success").click()
        self.app.wait_for_element_by_xpath("//*[@href='/epg/channel/add/']", 3)        # ensure that 'add channel' button appeared

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

    def create_random_channel(self):
        # TO IMPLEMENT VIA REST
        self.create(
            Channel(name='Channel' + str(randint(0, 9999999)), service_id=str(randint(0, 65535)),
                    epg_name='Epg_name_' + str(randint(0, 9999999)), offset=str(randint(-23, 23)),
                    provider='Provider_' + str(randint(0, 9999999))))

    def is_submit_button_present(self):
        # print "SUBMIT:", self.app.wd.find_elements_by_xpath("//*[@id='content']/form/fieldset/div[12]/div[2]/button")
        return self.app.wd.find_elements_by_xpath("//*[@id='content']/form/fieldset/div[12]/div[2]/button")


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

