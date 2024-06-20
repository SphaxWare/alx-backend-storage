#!/usr/bin/env python3
"""web.py"""
import redis
import requests
from typing import Callable
from functools import wraps

# Initialize the Redis client
redis_client = redis.Redis()


def count_requests(method: Callable) -> Callable:
    """Decorator to count requests to a particular URL."""
    @wraps(method)
    def wrapper(url: str) -> str:
        """Wrapper function to count the request and call the method."""
        count_key = f"count:{url}"
        redis_client.incr(count_key)
        return method(url)
    return wrapper


def cache_page(method: Callable) -> Callable:
    """Decorator to cache the HTML content of a URL."""
    @wraps(method)
    def wrapper(url: str) -> str:
        """Wrapper function to cache the page content."""
        cache_key = f"cache:{url}"
        cached_content = redis_client.get(cache_key)
        if cached_content:
            return cached_content.decode('utf-8')

        # Call the original method to get the HTML content
        content = method(url)
        # Cache the content with an expiration time of 10 seconds
        redis_client.setex(cache_key, 10, content)
        return content
    return wrapper


@count_requests
@cache_page
def get_page(url: str) -> str:
    """Get the HTML content of a particular URL and cache it."""
    response = requests.get(url)
    return response.text
