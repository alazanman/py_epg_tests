# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.channel import Channel


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_create_channel(app):
    app.session.login("root", "123")
    app.channel.create(
        Channel(name="1234", service_id="2345", epg_name="epg_name2", offset="3", provider="Provider"))
    app.session.logout()