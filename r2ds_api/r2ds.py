# -*- coding: utf-8 -*-

import requests
import time
"""Main module."""

BASE_URL = "https://r2ds.tonkworks.com/api/"

def get(token, params):
    if params == None:
        params = {}
    params["format"] = "json"

    r = requests.get(
        BASE_URL + "documents/",
        params=params,
        headers={
            'Authorization': token
        }
    )
    return r

def topic(token, topic_id, params):
    if params == None:
            params = {}
    params["format"] = "json"

    r = requests.get(
        BASE_URL + "documents/",
        params=params,
        headers={
            'Authorization': token
        }
    )
    return r

def stream(token, params):
    if params == None:
            params = {}
    params["format"] = "json"

    wait_period = 1
    last_request = time.gmtime()
    while time.gmtime() > last_request + wait_period:
        last_request = time.gmtime()
        r = requests.get(
            BASE_URL + "documents/",
            params=params,
            headers={
                'Authorization': token
            }
        )
        for d in r.json():
            yield d
        time.sleep(.2)