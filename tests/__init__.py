# -*- coding: utf-8 -*-
__author__ = 'Aleksey Tanana'
from nose_config import *


# from nose.tools import with_setup
# from fixture.nose import nose_print as nose_print
# from fixture.nose import nose_print2 as nose_print2


# def setup_package():
#     global db, app
#     print(__name__, '__init__.py : setup_package() ========================================')
#     db = set_db()
#     app = set_app()
#     return db, app


# def setup_package():
#     global json_channels
#     json_channels = test_generator('json_channels')
#     print json_channels

def teardown_package():
    global db, app
    print(__name__, '__init__.py : teardown_package() =====================================')
    db = stop_db()
    app = stop_app()
    return db, app