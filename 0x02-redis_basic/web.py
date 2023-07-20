#!/usr/bin/env python3
"""implementing an expiring web cache and tracker"""

import redis
import requests

_redis = redis.Redis()
counter = 0


def get_page(url:str) -> str:
    """obtin the HTML content of\
        a particular URL and returns it"""
    _redis.set("cached:{}".format(url), count)
    response = requests.get(url)
    _redis.incr("count:{}".format(url))
    _redis.setex(
        "cached:{}".format(url), 10, response.get("cached:{}").format(url))
    return response.text


if __name__ == "__main__":
    get_page('http://slowwly.robertomurray.co.uk')

