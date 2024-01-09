#!/usr/bin/env python3
"""Write a Python function that inserts
a new document in a collection based on kwargs"""


def list_all(mongo_collection):
    """Return an empty list if no document in the collection"""
    req = mongo_collection.find()
    return list(req)
