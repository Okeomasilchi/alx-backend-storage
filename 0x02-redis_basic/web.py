#!/usr/bin/env python3
"""
Implementing an expiring web cache and tracker
"""
import requests
import redis
import time
from functools import wraps

r = redis.Redis(host='localhost', port=6379, db=0)


def cache_result(func):
    """
    Decorator function that caches the result of a
    given function based on the URL.

    Args:
        func (function): The function to be decorated.

    Returns:
        function: The decorated function.

    """
    @wraps(func)
    def wrapper(url):
        key = f"count:{url}"
        count = r.get(key)
        if count:
            r.incr(key)
        else:
            r.set(key, 1)
            r.expire(key, 10)
        return func(url)
    return wrapper


@cache_result
def get_page(url: str) -> str:
    """
    Retrieve the content of a web page.

    Args:
        url (str): The URL of the web page to retrieve.

    Returns:
        str: The content of the web page as a string.
    """
    response = requests.get(url)
    return response.text
