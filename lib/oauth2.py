#-*- coding: utf-8 -*-
import requests
import simplejson

import config

urlToken = "https://api.fidelizador.com/oauth/v2/token"

def get_access_token():
    data = {
        'grant_type' : 'client_credentials',
        'client_id' : config.config.get('credentials', 'client_id'),
        'client_secret' : config.config.get('credentials', 'secret'),
    }
    response = requests.get(urlToken, data, headers={'Content-Type': 'application/json'})
    assert response.status_code == 200, 'Error getting access_token with existing credentials'
    result = response.json()
    config.TOKEN = result.get('access_token')
    config.REFRESH_TOKEN = result.get('refresh_token')
