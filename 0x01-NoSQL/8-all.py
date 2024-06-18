#!/usr/bin/env python3
"""All.py"""


def list_all(mongo_collection):
    """
    Lists all documents in a collection.
    
    :param mongo_collection: pymongo collection object
    :return: List of documents in the collection or an empty list if no documents are found
    """
    documents = mongo_collection.find()
    return documents
