#!/usr/bin/env python3

"""
script that provides some stats
about Nginx logs stored in MongoDB:
"""

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient()
    logs = client.logs.nginx
    print(f"{logs.count_documents({})} logs")
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = logs.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")
    filter_path = {"method": "GET", "path": "/status"}
    print(f"{logs.count_documents(filter_path)} status check")
