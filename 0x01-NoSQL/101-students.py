#!/usr/bin/env python3
"""
A function that returns all students sorted by average score
"""


def top_students(mongo_collection):
    """
    A function function that returns all students sorted by average score
    mongo_collection will be the pymongo collection object
    The top must be ordered
    The average score must be part of each item returns with key = averageScore
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
