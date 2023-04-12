#!/usr/bin/env python3
"""
This script defines a Cache class for storing data in Redis.
"""
import uuid
from typing import Union

import redis


class Cache:
    """
    A class for caching data in Redis.
    """

    def __init__(self) -> None:
        """
        Initializes a Redis client and flushes the instance using flushdb.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    
    def store(self, data: Union[str, bytes, int, float]) -> str:
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


    def get(
        self,
        key: str,
        fn: Optional[Callable] = None,
    ) -> Union[str, bytes, int, float, None]:
        """
        returns the value stored in the redis store at the key by converting it
        to its original data type by calling the function fn. if the key is not
        found, it returns None
        """
        value = self._redis.get(key)
        if value is not None and fn is not None:
            value = fn(value)
        return value

    
    def get_int(self, key: str) -> Union[int, None]:
        """
        returns the value stored in the redis store at the key as an int
        """
        return self.get(key, int)

    
    def get_str(self, key: str) -> Union[str, None]:
        """
        returns the value stored in the reds store at the key as str
        """
        return self.get(key, str)   
