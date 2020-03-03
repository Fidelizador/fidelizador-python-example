# -*- coding: utf-8 -*-
from __future__ import print_function

import config
import sys
import lib.listmanager as listmanager
import lib.oauth2 as credentials

credentials.get_access_token()

if not config.TOKEN:
    print("Could not get access token")
    sys.exit(0)

result = listmanager.create_list("Lista de prueba python")
assert isinstance(result, dict), 'Could not create a list'
print(result)
