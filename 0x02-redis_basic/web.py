#!/usr/bin/env python3
"""implementing an expiring web cache and tracker"""

import redis
import requests
from functools import wraps
from typing import Callable

_redis = redis.Redis()


def data_cacher(method: Callable) -> Callable:
    """implement wrapper"""
    @wraps(method)
    def wrapper(url) -> str:
        _redis.incr("count:{}".format(url))
        result = _redis.get("result:{}".format(url)) or None
        if result is not None:
            return result.decode('utf-8')
        result = method(url)
        _redis.set("count:{}".format(url), 0)
        _redis.setex("result:{}".format(url), 10, result)
        return result
    return wrapper


@data_cacher
def get_page(url:str) -> str:
    """obtin the HTML content of\
        a particular URL and returns it"""
    response = requests.get(url)
    return response.text

