# -*- coding: utf-8 -*-
import os
import base64


def abs_path_to_file(relative_path):
    # print os.getcwd()
    return os.path.abspath(os.path.join(os.getcwd(), relative_path))

def encode_base64(abs_path):
    print "abs_path", abs_path
    with open(abs_path, 'rb') as f:
        return base64.b64encode(f.read())