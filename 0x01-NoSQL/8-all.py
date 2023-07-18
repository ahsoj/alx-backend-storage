#!/usr/bin/env python3
"""list all documents in a collection"""


def list_al(mongo_collection):
    """return list of collection"""
    return [docs for docs in mongo_collection.find()]

