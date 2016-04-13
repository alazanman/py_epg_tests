# -*- coding: utf-8 -*-


def test_delete_first_channel(app):
    app.session.login("root", "123")
    app.channel.delete_first_channel()
    app.session.logout()