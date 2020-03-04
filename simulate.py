# -*- coding: utf-8 -*-
from __future__ import print_function

import config
import lib.oauth2 as credentials
from lib.listmanager import create_list
from lib.contacts import create_contact

credentials.get_access_token()

new_list = create_list("Lista de prueba python")
assert isinstance(result, dict), 'Could not create a list'

new_contact = create_contact(
    'new.contact@example.org',
    new_list['id'],
    {
        'firstname': 'name',
        'lastname': 'example'}
)
assert isinstance(result, dict), 'Could not create a contact'
print('List data:', new_list)
print('Contact data:', new_contact)
