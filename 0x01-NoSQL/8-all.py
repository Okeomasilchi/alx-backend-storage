#!/usr/bin/env python3

"""
Python function that lists all documents in a collection
"""

from pymongo.collection import Collection
from pymongo.cursor import Cursor


def list_all(mongo_collection: Collection) -> Cursor:
    """
    Retrieve all documents from the given MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection):
            The MongoDB collection to retrieve documents from.

    Returns:
        pymongo.cursor.Cursor: A cursor object containing
        all the retrieved documents.
    """

    return mongo_collection.find()
