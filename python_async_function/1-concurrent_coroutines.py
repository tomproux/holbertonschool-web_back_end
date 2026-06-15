#!/usr/bin/env python3
"""Module containing the wait_n coroutine."""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times with max_delay and return sorted delays.

    Args:
        n: Number of times to spawn wait_random.
        max_delay: Maximum delay value to pass to wait_random.

    Returns:
        List of delays in ascending order.
    """
    delays: List[float] = []

    async def collect(delay_coro):
        delay = await delay_coro
        # Insert in sorted order as each coroutine completes
        inserted = False
        for i, d in enumerate(delays):
            if delay < d:
                delays.insert(i, delay)
                inserted = True
                break
        if not inserted:
            delays.append(delay)

    await asyncio.gather(*[collect(wait_random(max_delay)) for _ in range(n)])

    return delays
