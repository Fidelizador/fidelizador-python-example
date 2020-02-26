#-*- coding: utf-8 -*-
import requests
import settings
import simplejson


urlToken = "https://api.fidelizador.com/oauth/v2/token"

def get_access_token():
    data = {
        'grant_type' : 'client_credentials',
        'client_id' : settings.CLIENTID,
        'client_secret' : settings.SECRET
    }
    try:
        response = requests.post(urlToken, data)
        responseText = response.text
        responseJson = simplejson.loads(responseText)
    except Exception:
        return False   
    return responseJson['access_token']