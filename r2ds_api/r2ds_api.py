# -*- coding: utf-8 -*-

import requests

"""Main module."""

def topic(token, topic_id, options,):
    r = requests.get(
        'https://api.github.com/user',
        headers={
            'Authorization': token
        }
    ))
    return r.content