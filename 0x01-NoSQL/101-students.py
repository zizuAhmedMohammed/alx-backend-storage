#!/usr/bin/env python3
"""
A function that Improve 12-log_stats.py by adding the top 10 of the most present IPs in the collection nginx of the database logs
"""


def top_students(mongo_collection):
    """
    A function that Improve 12-log_stats.py by adding the top 10 of the most
    present IPs in the collection nginx of the database logs
    returns all students sorted by average score
    """
    return mongo_collection.aggregate([{
        "$unwind": "$topics"
    }, {
        "$group": {
            "_id": {
                "_id": "$_id",
                "name": "$name"
            },
            "averageScore": {
                "$avg": "$topics.score"
            }
        }
    }, {
        "$project": {
            "_id": "$_id._id",
            "name": "$_id.name",
            "averageScore": "$averageScore"
        }
    }, {
        '$sort': {
            "averageScore": -1
        }
    }])
