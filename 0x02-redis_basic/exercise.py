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

    
    def get(self, key: str, default=None, fn: Callable[[bytes], Union[str, int]] = None) -> Union[None,str,int]:
        """
        Retrieves the value corresponding to the given key from Redis and converts it if necessary.
        If the `key` is not found and the `default` parameter is provided, returns it instead.
        If the `key` is not found and the `default` parameter is not provided, returns None.
        Args:
            key: A string representing a Redis key.
            default: A default value to return if `key` is not found in Redis. Defaults to None.
            fn: A callable object that will be used to convert the value if necessary.
                For example, if you want to always retrieve a str from Redis,
                you can pass str as `fn`. Defaults to None.
        Returns:
            The Redis value corresponding to `key`, converted via `fn` if necessary.
            If the `key` is not found and a default value is not provided, returns None.
        """
        result = self._redis.get(key)
        if result is None:
            return default
        else:
            if fn is not None:
                return fn(result)
            else:
                return result.decode('utf-8')
    
    
    def get_str(self, key: str, default: str = None) -> str:
        """
        Convenience method that returns the string value corresponding to the given key from Redis,
        with an optional default value if the key is not found.
        Args:
            key: A string representing a Redis key.
            default: A default value to return if `key` is not found in Redis. Defaults to None.
        Returns:
             The Redis string value corresponding to `key`,
             or the default value if the `key` is not found.
             If the `key` is not found and a default is not provided, returns None.
        """
        return self.get(key, default=default, fn=str)
    def get_int(self, key: str, default: int = None) -> int:
        """
        Convenience method that returns the integer value corresponding to the given key from Redis,
        with an optional default value if the key is not found.
        Args:
            key: A string representing a Redis key.
            default: A default value to return if `key` is not found in Redis. Defaults to None.
        Returns:
             The Redis integer value corresponding to `key`,
             or the default value if the `key` is not found.
             If the `key` is not found and a default is not provided, returns None.
        """
        return self.get(key, default=default, fn=int)
