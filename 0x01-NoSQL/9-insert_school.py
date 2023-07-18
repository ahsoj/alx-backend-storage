#!/usr/bin/env python3
"""inserts a new document in a collection  based on `kwargs`"""


def insert_school(mongo_collection, **kwargs):
    """return new `_id`"""
    return mongo_collection.insert_one(kwargs).inserted_id
