#!/usr/bin/env python3
"""
This script defines a Cache class for storing data in Redis.
"""


import redis
import uuid


class Cache:
    """
    A class for caching data in Redis.
    """

    def __init__(self):
        """
        Initializes a Redis client and flushes the instance using flushdb.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    
    def store(self, data) -> str:
        """
        Stores the input data in Redis using a randomly generated key and returns the key.

        Args:
            data: The data to be stored in Redis. Can be a str, bytes, int or float.

        Returns:
            The randomly generated key used to store the data in Redis.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
