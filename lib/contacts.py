#-*- coding: utf-8 -*-

import requests

import config

def create_contact(email, list_id, fields={}):
    """
    Create a contact for an specific list in Fidelizador
    """
    headers = {
        'X-Client-Slug' : config.config.get('slug'),
        'Authorization': "Bearer {}".format(config.TOKEN),
        'Content-Type': 'application/json' }
    data = {
        'email': email,
        'list_id': list_id,
        'fields': fields
    }

    response = requests.post(
        "https://api.fidelizador.com/1.1/contact.json",
        data=data,
        headers=headers)
    assert response.status_code < 400, 'Could not create a new contact'
    return response.json()
