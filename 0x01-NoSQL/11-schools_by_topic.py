#!/usr/bin/env python3
"""Python function"""


def schools_by_topic(mongo_collection, topic):
    """return the list of school having a specific topic"""
    specific_topic = {'topics': {
            '$elemMatch': {
                    '$eq': topic,
                },
        }}
    return [docs for docs in mongo_collection.find(specific_topic)]
