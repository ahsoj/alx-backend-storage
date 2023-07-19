#!/usr/bin/env python3
"""Class Module"""
import redis
from uuid import uuid4
from typing import Union, Callable
from functools import wraps


def count_calls(method:Callable) -> Callable:
    '''define decorator'''
    @wraps(method)
    def wrapper(self, *args, **kwds):
        '''method wrapper'''
        if isinstance(self._redis, redis.Redis):
            self._redis.incr(method.__qualname__)
        return method(self, *args, **kwds)
    return wrapper


class Cache(object):
    '''represent Cache class'''
    def __init__(self) -> None:
        '''Initialize instance'''
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    @count_calls
    def store(self, data: Union[str, bytes, int, float])-> str:
        '''
        class method takesa `data` arguments
        rType: str
        '''
        key = str(uuid4())
        self._redis.set(key, data)
        return key
    
    def get(self,key:str,fn:Callable = None) -> Union[str,int,float,bytes]:
        '''create get method'''
        value = self._redis.get(key)
        return fn(value) if fn is not None else value

    def get_str(self,key:str) -> str:
        '''return string format'''
        return self.get(key, lambda d: d.decode('utf-8'))

    def get_int(self,key:str) -> int:
        '''return integer format'''
        return self.get(key,lambda d: int(d))

