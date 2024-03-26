#!/usr/bin/env python3

"""
Python function that lists all documents in a collection
"""


def list_all(mongo_collection):
    """
    Retrieve all documents from the given
    MongoDB collection.

    Args:
      mongo_collection (pymongo.collection.Collection):
      The MongoDB collection to retrieve documents from.

    Returns:
      pymongo.cursor.Cursor: A cursor object containing
      all the retrieved documents.
    """
    documents = mongo_collection.find()
    result = []

    # Iterate over the documents and append them to the result list
    for document in documents:
        result.append(document)

    return documents
