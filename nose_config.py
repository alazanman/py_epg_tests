# -*- coding: utf-8 -*-
# from nose.tools import *
# import nose
# from nose import *
# import pytest
import json
import os.path
import importlib
import jsonpickle
from time import sleep
from fixture.application import Application
from fixture.db import DbFixture
from fixture.rest import RestApi


browser = 'chrome'
web_config = {
           "baseUrl": "http://10.130.8.159/",
           "username": "root",
           "password": "123"
       }

db_config = {
    "database": "epg",
    "user": "epg",
    "password": "123",
    "host": "10.130.8.159",
    "port": "5432"
  }

app = None
target = None
db = None
restfixture = None

def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target

def set_app():
    global app
    # browser = request.config.getoption("--browser")
    # web_config = load_config(request.config.getoption("--target"))['web']
    if app is None or not app.is_valid():
        app = Application(browser=browser, base_url=web_config['baseUrl'])
    app.session.ensure_login(web_config['username'], web_config['password'])
    print 'SET_APP'
    return app

# @pytest.fixture(scope="session", autouse=True)
def stop_app():
    sleep(1)
    if app:
        app.session.ensure_logout()
        app.destroy()
    print 'STOP_APP'
    return app


# @pytest.fixture(scope="session")
def set_db():
    global db
    # db_config = load_config(request.config.getoption("--target"))['db']
    if db is None or not db.is_valid():
        db = DbFixture(database=db_config['database'], user=db_config['user'], password=db_config['password'], host=db_config['host'], port=db_config['port'])
        print 'SET_DB'
    print db, db.channel
    return db

def stop_db():
    db.destroy()
    print 'STOP_DB'
    return db


# @pytest.fixture(scope="session")
def rest(request):
    global restfixture
    rest_config = load_config(request.config.getoption("--target"))['web']
    # if restfixture is None or not restfixture.is_valid():
    if restfixture is None:
        restfixture = RestApi(base_url=rest_config['baseUrl'])
    def fin():
        restfixture.destroy()
    request.addfinalizer(fin)
    return restfixture

# @pytest.fixture
# def check_ui(request):
#     return request.config.getoption("--check_ui")

# def pytest_addoption(parser):
#     parser.addoption("--browser", action="store", default="chrome")
#     parser.addoption("--target", action="store", default="target.json")
#     parser.addoption("--check_ui", action="store_true")
#
# def pytest_generate_tests(metafunc):
#     for fixture in metafunc.fixturenames:
#         if fixture.startswith("data_"):
#             testdata = load_from_module(fixture[5:])
#             metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
#         elif fixture.startswith("json_"):
#             testdata = load_from_json(fixture[5:])
#             metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
#
# def test_generator(func_args):
#     for func_arg in func_args:
#         if func_arg.startswith("json_"):
#             testdata = load_from_json(func_arg[5:])
#             return list(str(x) for x in testdata)
#             # for data in testdata:
#             #     yield func_name, data
#             # metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])

def load_from_module(module):
    return importlib.import_module("data.%s" % module).testdata

def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s" % file)) as f:
        # for i in jsonpickle.decode(f.read()):
        #     print i
        # print len(jsonpickle.decode(f.read()))
        return jsonpickle.decode(f.read())