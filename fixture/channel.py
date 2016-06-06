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
        # sleep(1)
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
        # if not wd.find_element_by_xpath("//select[@id='id_languages']/option[@value='2']").is_selected():
        #     wd.find_element_by_xpath("//select[@id='id_languages']/option[@value='2']").click()
        # if not wd.find_element_by_xpath("//select[@id='id_languages']/option[@value='3']").is_selected():
        #     wd.find_element_by_xpath("//select[@id='id_languages']/option[@value='3']").click()
        for language in channel.languages:
            if not wd.find_element_by_xpath("//select[@id='id_languages']/option[@value='" + language + "']").is_selected():
                wd.find_element_by_xpath("//select[@id='id_languages']/option[@value='" + language + "']").click()
        # if not wd.find_element_by_xpath("//select[@id='id_languages']/option[@value='4']").is_selected():
        #     wd.find_element_by_xpath("//select[@id='id_languages']/option[@value='4']").click()
        # if not wd.find_element_by_id("id_allow_record").is_selected():
        #     wd.find_element_by_id("id_allow_record").click()
        wd.execute_script("window.scrollBy(0, 1000)")
        wd.find_element_by_xpath("//*[@id='content']/form/fieldset/div[9]/div/img").click()
        sleep(1)
        pyautogui.typewrite(os.path.abspath(os.path.join(os.getcwd(), channel.icon)))
        # pyautogui.typewrite('C:\\icon_valid.jpg')
        pyautogui.press('enter')
        wd.find_element_by_xpath("//*[@id='content']/form/fieldset/div[10]/div/img").click()
        sleep(1)
        # narrow_banner_input = os.path.abspath(os.path.join(os.getcwd(), "../data/banners/narrow_valid.jpg"))
        pyautogui.typewrite(os.path.abspath(os.path.join(os.getcwd(), channel.narrow_banner)))
        pyautogui.press('enter')
        wd.find_element_by_xpath("//*[@id='content']/form/fieldset/div[11]/div/img").click()
        sleep(1)
        pyautogui.typewrite(os.path.abspath(os.path.join(os.getcwd(), channel.wide_banner)))
        # pyautogui.typewrite('C:\\wide_valid.jpg')
        pyautogui.press('enter')
        # sleep(3)

        # "icons/channel_416.jpeg"
        # "banners/416/narrow_banner.jpeg"
        # "banners/416/wide_banner.jpeg"

        # # narrow_banner_input = wd.find_element_by_id("id_narrow_banner")
        # # narrow_banner_input = wd.find_element_by_css_selector("#id_narrow_banner")
        # # narrow_banner_input = wd.find_element_by_xpath("//*[@id='content']/form/fieldset/div[10]/div/input")
        # narrow_banner_input = wd.find_element_by_xpath("//*[@id='id_narrow_banner']")
        # narrow_banner_img = wd.find_element_by_xpath("//*[@id='content']/form/fieldset/div[10]/div/img")
        # wd.execute_script('arguments[0].style = ""; arguments[0].style.display = "block"; arguments[0].style.visibility = "visible";', narrow_banner_input)
        # # "file.removeAttribute('class')"
        #
        # # wd.execute_script("file.removeAttribute('class')")
        #
        # # narrow_banner_input.click()
        # # narrow_banner_input.send_keys("C:\\narrow_valid.jpg")
        #
        # # wd.execute_script("$('#id_narrow_banner').focus(function() {('#id_narrow_banner').siblings()[0].trigger('unload')});")
        # # wd.execute_script("alert('here');$('#id_narrow_banner').focus(function() {alert('here');('#id_narrow_banner').siblings()[0].load(function() {alert('here')}).attr('src', 'C:\\narrow_valid.jpg')});")
        # # wd.find_element_by_xpath("//*[@id='content']/form/fieldset/div[10]/div/img").click()
        # # narrow_banner_input.send_keys("C:\\narrow_valid.jpg")
        # # sleep(3)
        # wd.execute_script("placeChooser('C:\\narrow_valid.jpg');")
        # wd.execute_script("$('#id_narrow_banner').each(function() {$(this).trigger('onload');alert('here');});")
        #
        # # onclick = "showImageModal(this); return false;"
        # # wd.execute_script(
        # #     "$('#id_narrow_banner').siblings()[0]').click(function() {('#id_narrow_banner').focus()});")
        # # wd.execute_script("return jQuery(\"" + '.ws-item-toolbar' + "\");")
        # # wd.execute_script("$('#id_narrow_banner').siblings()[0].focus(function() {trigger('click');});")
        #
        #
        # # print os.getcwd()
        # # narrow_banner_input.send_keys(os.getcwd() + "/data/banners/narrow_valid.jpg")
        #
        # sleep(5)
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
        # sleep(1)
        self.app.wait_for_element_by_xpath("//*[@href='/epg/channel/add/']", 10)        # ensure that 'add channel' button appeared

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

