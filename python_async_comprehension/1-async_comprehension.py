#!/usr/bin/env python3
"""Module containing the async_comprehension coroutine."""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collect 10 random floats via an async comprehension
        over async_generator.

    Iterates asynchronously over async_generator using an async comprehension,
    gathering all 10 yielded random floats into a list and returning it.

    Returns:
        A list of 10 random floats between 0 and 10.
    """
    return [value async for value in async_generator()]
