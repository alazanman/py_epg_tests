py.test --browser=firefox tests
::nosetests --browser=chrome --check_ui tests
::py.test --browser=chrome --check_ui tests\test_create_channel.py
::py.test --browser=chrome --check_ui tests\test_edit_channel.py
::py.test --browser=chrome --check_ui tests\test_del_channel.py
::@pause