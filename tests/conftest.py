# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from time import sleep

fixture = None

@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()
        fixture.session.login("root", "123")
    elif not fixture.is_valid():
        fixture = Application()
        fixture.session.login("root", "123")
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