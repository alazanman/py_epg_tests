# -*- coding: utf-8 -*-
# from nose.tools import *
# import nose
# from nose import *
# import pytest
import nose
import json
import os.path
import importlib
import jsonpickle
from time import sleep
from fixture.app import Application
from fixture.db import DbFixture
from fixture.rest import RestApi


# print nose.config.Config().options
# # nose.config.Config().options = {"--browser":"chrome"}
# print nose.config.Config().options
# parser = nose.config.Config().getParser()
# # parser.add_option("--browser")
# parser.add_option("--browser", action="store", default="chrome")
# parser.add_option("--config_file", action="store", default="config_file.json")
# parser.add_option("--check_ui", action="store_true", default=True)
# print nose.config.Config().options

# web_config = {
#            "baseUrl": "http://10.130.8.159/",
#            "username": "root",
#            "password": "123"
#        }
#
# db_config = {
#     "database": "epg",
#     "user": "epg",
#     "password": "123",
#     "host": "10.130.8.159",
#     "port": "5432"
#   }
#
# rest_config = {
#     "baseUrl": "http://10.130.8.159/",
#     "username": "root",
#     "password": "123"
# }

config_file = None
config_file_name = "config_file.json"
app = None
db = None
rest = None


def load_config(file_name='config_file.json'):
    global config_file
    if config_file is None:
        config_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
        with open(config_file_path) as f:
            config_file = json.load(f)
    return config_file

base_media_url = load_config()['web']['baseUrl'] + "media/"

def set_app():
    global app
    # browser = request.config_file.getoption("--browser")
    # web_config = load_config(request.config.getoption("--config_file"))['web']
    web_config = load_config(config_file_name)['web']
    other_config = load_config(config_file_name)['other']
    if app is None or not app.is_valid():
        app = Application(browser=other_config['browser'], base_url=web_config['baseUrl'])
        print 'SET_APP', app
    app.session.ensure_login(web_config['username'], web_config['password'])
    return app

def stop_app():
    sleep(1)
    if app:
        app.session.ensure_logout()
        app.destroy()
    print 'STOP_APP', app
    return app

def set_db():
    global db
    # db_config = load_config(request.config.getoption("--config"))['db']
    db_config = load_config(config_file_name)['db']
    if db is None or not db.is_valid():
        db = DbFixture(database=db_config['database'], user=db_config['user'], password=db_config['password'], host=db_config['host'], port=db_config['port'])
        print 'SET_DB', db
    return db

def stop_db():
    if db:
        db.destroy()
    print 'STOP_DB', db
    return db

def set_rest():
    global rest
    # rest_config = load_config(request.config.getoption("--config"))['web']
    web_config = load_config(config_file_name)['web']
    # if restfixture is None or not restfixture.is_valid():
    if rest is None:
        rest = RestApi(base_url=web_config['baseUrl'])
        print 'SET_REST', rest
    rest.auth(web_config['username'], web_config['password'])
    return rest

def stop_rest():
    if rest:
        rest.destroy()
    print 'STOP_REST', rest
    return rest


def check_ui():
    # global config_file
    return load_config(config_file_name)['other']['check_ui'] == 'True'

# def nosetests_addoption(parser):
#     parser.add_option("--browser", action="store", default="chrome")
#     parser.add_option("--target", action="store", default="target.json")
#     parser.add_option("--check_ui", action="store_true")

def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s" % file)) as f:
        return jsonpickle.decode(f.read())