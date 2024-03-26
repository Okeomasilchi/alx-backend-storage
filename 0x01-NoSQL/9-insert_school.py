#!/usr/bin/env python3

def insert_school(mongo_collection, **kwargs):
    """
    Insert a new document in a collection based on kwargs
    """
    # print(kwargs)
    return mongo_collection.insert_one(kwargs).inserted_id
