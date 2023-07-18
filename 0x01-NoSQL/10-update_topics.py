#!/usr/bin/env python3
"""changes all topcis of a school document based on the name"""


def update_topics(mongo_collection, name, topics):
    """change all topics"""
    mongo_collection.update_mny(
            {'name': name},
            {'$set': {'topics': topics}}
            )
