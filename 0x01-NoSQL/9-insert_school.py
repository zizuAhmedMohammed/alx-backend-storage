#!/usr/bin/env python3
"""
A function that inserts a new document in a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
    A function that inserts a new document in a collection based on kwargs
    Returns the new _id, mongo_collection will be the pymongo collection object
    """
    return mongo_collection.insert_one(kwargs).inserted_id
