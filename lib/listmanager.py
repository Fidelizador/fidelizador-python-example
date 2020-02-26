#-*- coding: utf-8 -*-

import requests
import settings
import simplejson

urlCreateList = "https://api.fidelizador.com/1.0/list.json"

def create_list(name):
    """ This method create a list in Fidelizador """
    headers = { 'X-Client-Slug' : settings.SLUG, 'Authorization': "Bearer {}".format(settings.ACCESS_TOKEN) }
    data = {
        'name' : name
    }
    
    try:
        response = requests.post(urlCreateList, data=data, headers=headers)
        responseText = response.text
        responseJson = simplejson.loads(responseText)
    except Exception:
        return False   
    return responseJson


