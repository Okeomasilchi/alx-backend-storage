#!/usr/bin/env python3
"""
Module that holds the class Cache to handle
caching using radis
"""
import redis
from typing import Union, Callable
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

    def store(self, data: Union[str, bytes, int, float]) -> str:
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

    def get(
        self,
        key: str,
        fn: Callable[[bytes], str] = None
    ) -> str:
        """
        Retrieves the value associated with the given key from
        Redis.

        Args:
            key (str): The key to retrieve the value for.
            fn (Callable[[bytes], str], optional): A function to
                apply to the retrieved value. Defaults to None.

        Returns:
            str: The retrieved value, optionally transformed by the
                provided function.
        """
        ret = self._redis.get(key)
        return fn(ret) if ret and fn else ret

    def get_str(self, key: str) -> Union[str, None]:
        """
        Retrieves the value associated with the given key as a
        string.

        Args:
            key (str): The key to retrieve the value for.

        Returns:
            Union[str, None]: The value associated with the key
            as a string, or None if the key does not exist.
        """
        data = self.get(key)
        return str(data) if data else data

    def get_int(self, key: str) -> Union[int, None]:
        """
        Retrieves the value associated with the given key and
        converts it to an integer.

        Args:
            key (str): The key to retrieve the value for.

        Returns:
            Union[int, None]: The integer value associated
                with the key, or None if the key does not exist or
                the value is not convertible to an integer.
        """
        data = self.get(key)
        return int(data) if data else data
