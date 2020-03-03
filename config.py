#-*- coding: utf-8 -*-

import os
import sys

if sys.version_info < (3, 0):
    from ConfigParser import ConfigParser
else:
    from configparser import ConfigParser

TOKEN = None
REFRESH_TOKEN = None

config = ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), 'settings.cfg'))
