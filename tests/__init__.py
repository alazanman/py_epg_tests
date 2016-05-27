# -*- coding: utf-8 -*-
__author__ = 'Aleksey Tanana'
from data.channels_generator import *
from nose import with_setup
from nose_config import *
from nose_parameterized import parameterized, param


def teardown_package():
    global db, app, rest
    print(__name__, '__init__.py : teardown_package() =====================================')
    db = stop_db()
    app = stop_app()
    rest = stop_rest()

# def setup_package():
#     global check_ui
#     print(__name__, '__init__.py : setup_package() ========================================')
#     check_ui = if_check_ui()
#     # print 'check UI:', check_ui

# def setup_package():
#     global check_ui
#     print(__name__, '__init__.py : setup_package() ========================================')
#     options = cli_options()

# def setup_module():
#     global db, app, rest
#     db = set_db()
#     app = set_app()
#     rest = set_rest()
#     return app, db, rest