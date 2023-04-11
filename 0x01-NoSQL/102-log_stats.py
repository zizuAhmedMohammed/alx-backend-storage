#!/usr/bin/env python3
"""
A function that improves 12-log_stats.py by adding the top 10 of the most present IPs in the collection nginx of the database logs
"""
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx
    count = logs_collection.count_documents({})
    print("{} logs".format(count))
    print("Methods:")
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        meth_count = logs_collection.count_documents(
            {"method": {
                "$eq": method
            }})
        print("\tmethod {}: {}".format(method, meth_count))

    status_checks = logs_collection.count_documents(
        {"$and": [{
            "method": {
                "$eq": 'GET'
            }
        }, {
            "path": "/status"
        }]})
    print("{} status check".format(status_checks))

    top_ips = logs_collection.aggregate([{
        "$group": {
            "_id": "$ip",
            "count": {
                "$sum": 1
            }
        }
    }, {
        '$sort': {
            "count": -1
        }
    }, {
        "$limit": 10
    }])

    print("IPs:")
    for doc in top_ips:
        print("\t{}: {}".format(doc.get("_id"), doc.get("count")))
