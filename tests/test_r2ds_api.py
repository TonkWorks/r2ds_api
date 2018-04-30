#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `r2ds_api` package."""

import pytest


import r2ds_api

TEST_AUTH_TOKEN = "TEST_AUTH_TOKEN"
def test_get():
    """API get request."""
    response = r2ds_api.get(TEST_AUTH_TOKEN, params={
        "score__gt": 100
    })
    assert response.status_code == 200

def test_topic():
    """API topic request."""
    response = r2ds_api.topic(TEST_AUTH_TOKEN, topic_id=2, params={
        "score__gt": 100
    })
    assert response.status_code == 200
