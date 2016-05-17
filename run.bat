::py.test --browser=firefox tests\test_del_channel.py
py.test --browser=chrome --check_ui tests\test_create_channel.py tests\test_edit_channel.py tests\test_del_channel.py
::py.test --browser=chrome --check_ui tests\test_create_channel.py
::py.test --browser=chrome --check_ui tests\test_edit_channel.py
::py.test --browser=chrome --check_ui tests\test_del_channel.py
::@pause