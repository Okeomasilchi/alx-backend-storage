#!/usr/bin/env python3
"""
Module that holds the class Cache to handle
caching using radis
"""
import redis
from typing import Union
from uuid import uuid4


class Cache:
    """
    A class representing a cache.

    This class provides methods to interact with a Redis
    database for caching purposes.

    Attributes:
        _redis (radis.Radis): The Redis instance used for caching.
    """

    def __init__(self) -> None:
        """
        Initializes an instance of the Cache class.

        This method initializes the Cache object and sets up
        the Redis database by creating a Radis instance and
        flushing the database.

        Parameters:
            None

        Returns:
            None
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, int, bytes, float]) -> str:
        """
        Stores the given data in Redis and returns the
        generated ID.

        Args:
            data: The data to be stored. It can be a string,
            integer, bytes, or float.

        Returns:
            The generated ID for the stored data.
        """
        id = self.gen_id()
        self._redis.set(id, data)
        return id

    def gen_id(self) -> str:
        """
        Generate a unique identifier using UUID.

        Returns:
            str: A string representation of the generated UUID.
        """
        return str(uuid4())
