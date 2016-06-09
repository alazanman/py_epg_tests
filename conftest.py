# -*- coding: utf-8 -*-
import pytest
import json
import os.path
import importlib
import jsonpickle
from time import sleep
from fixture.app import Application
from fixture.db import DbFixture
from fixture.rest import RestApi


fixture = None
target = None
dbfixture = None
restfixture = None

def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target


@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--target"))['web']
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=web_config['baseUrl'])
    fixture.session.ensure_login(web_config['username'], web_config['password'])
    # def fin():
    #     sleep(1)
    #     fixture.session.ensure_logout()
    #     fixture.destroy()
    # request.addfinalizer(fin)
    return fixture

@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        sleep(1)
        if app:
            app.session.ensure_logout()
            app.destroy()
    request.addfinalizer(fin)
    return app

@pytest.fixture(scope="session")
def db(request):
    global dbfixture
    db_config = load_config(request.config.getoption("--target"))['db']
    if dbfixture is None or not dbfixture.is_valid():
        dbfixture = DbFixture(database=db_config['database'], user=db_config['user'], password=db_config['password'], host=db_config['host'], port=db_config['port'])
    def fin():
        dbfixture.destroy()
    request.addfinalizer(fin)
    return dbfixture

@pytest.fixture(scope="session")
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

@pytest.fixture
def check_ui(request):
    return request.config.getoption("--check_ui")

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--target", action="store", default="target.json")
    parser.addoption("--check_ui", action="store_true")

def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        # print fixture
        if fixture.startswith("data_"):
            testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
        elif fixture.startswith("json_"):
            testdata = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])


def load_from_module(module):
    return importlib.import_module("data.%s" % module).testdata

def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file)) as f:
        return jsonpickle.decode(f.read())