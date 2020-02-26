# -*- coding: utf-8 -*-
from __future__ import print_function

import settings
import sys
import lib.listmanager as listmanager
import lib.oauth2 as credentials

settings.ACCESS_TOKEN = credentials.get_access_token()

if not settings.ACCESS_TOKEN:
    print("Could not get access token")
    sys.exit(0)

response = listmanager.create_list("Lista de prueba python")

print(response)

