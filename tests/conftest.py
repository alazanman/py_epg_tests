# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from time import sleep

fixture = None

@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--baseUrl")
    if fixture is None:
        fixture = Application(browser=browser, base_url=base_url)
    elif not fixture.is_valid():
        fixture = Application(browser=browser, base_url=base_url)
    fixture.session.ensure_login("root", "123")
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        sleep(1)
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--baseUrl", action="store", default="http://10.130.8.159/epg/")