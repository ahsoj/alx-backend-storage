#!/usr/bin/env python3
"""Class Module"""
import redis
from uuid import uuid4
from typing import Union


class Cache(object):
    '''represent Cache class'''
    def __init__(self) -> None:
        '''Initialize instance'''
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data: Union[str, bytes, int, float])-> str:
        '''
        class method takesa `data` arguments
        rType: str
        '''
        key = str(uuid4())
        self._redis.set(key, data)
        return key
