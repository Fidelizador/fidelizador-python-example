#-*- coding: utf-8 -*-

import requests

import config

def create_list(name):
    """ This method create a list in Fidelizador """
    headers = {
        'X-Client-Slug' : config.config.get('slug'),
        'Authorization': "Bearer {}".format(config.TOKEN),
        'Content-Type': 'application/json' }
    data = {
        'name' : name
    }

    response = requests.post(
        "https://api.fidelizador.com/1.0/list.json",
        data=data,
        headers=headers)
    assert response.status_code == 200, 'Could not create a new list'
    return response.json()
