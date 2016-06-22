# -*- coding: utf-8 -*-
# from model.channel import Channel
from random import choice
from utils.file_util import encode_base64


class RestChannelHelper:

    def __init__(self, rest):
        self.rest = rest

    def validate_banners(self, channel, channels_list):
        # banners validation
        for ch in channels_list:
            if ch == channel:
                assert self.rest.compare_files_CRC(channel.icon["user_file"], ch.icon["server_file"])
                assert self.rest.compare_files_CRC(channel.narrow_banner["user_file"], ch.narrow_banner["server_file"])
                assert self.rest.compare_files_CRC(channel.wide_banner["user_file"], ch.wide_banner["server_file"])
                break

    def create(self, channel):
        session = self.rest.session
        url = self.rest.base_url + "epg/channel/add/"
        data = {
                'csrfmiddlewaretoken': session.cookies['csrftoken'],
                'name': channel.name,
                'service_id': channel.service_id,
                'epg_name': channel.epg_name,
                'offset': channel.offset,
                'provider': channel.provider,
                'languages': channel.languages  # takes only one value!
                }
        for l in channel.languages:
            data.update({'languages': l})
        if channel.allow_record:
            data.update({'allow_record': 'on'})
        pics = {'icon': channel.icon["user_file"],
                    'narrow_banner': channel.narrow_banner["user_file"],
                    'wide_banner': channel.wide_banner["user_file"]
                }
        # print pics
        for key in pics:
            # print key, pics[key]
            if pics[key] > 0:
                data.update({key: r"data:image/jpeg;base64," + encode_base64(pics[key])})
                # print "added", key
                # print data[key]
        r = session.post(url, data=data, cookies=session.cookies)
        print "Channel created via rest:", channel

    def delete(self, channel):
        session = self.rest.session
        url = "%sepg/channel/%s/delete/" % (self.rest.base_url, channel.id)
        data = {
                'csrfmiddlewaretoken': session.cookies['csrftoken']
        }
        print url
        r = session.post(url, data=data, cookies=session.cookies)
        # print "Channel deleted via rest:", channel

    def delete_channels(self, channels, count_to_retain=0):
        while len(channels) > count_to_retain:
            # some_channel = choice(channels)
            self.delete(channels[0])
            channels.remove(channels[0])