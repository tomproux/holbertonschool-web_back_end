#!/usr/bin/env python3
"""Module containing the task_wait_n coroutine."""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn task_wait_random n times with max_delay and return sorted delays.

    Uses asyncio.Task instances created by task_wait_random to run
    concurrently, collecting each delay result in ascending order
    without using sort().

    Args:
        n: Number of times to spawn task_wait_random.
        max_delay: Maximum delay value to pass to task_wait_random.

    Returns:
        List of float delays in ascending order.
    """
    delays: List[float] = []

    async def collect(task: asyncio.Task) -> None:
        """Await a task and insert its result in sorted order.

        Args:
            task: An asyncio.Task wrapping wait_random.
        """
        delay = await task
        inserted = False
        for i, d in enumerate(delays):
            if delay < d:
                delays.insert(i, delay)
                inserted = True
                break
        if not inserted:
            delays.append(delay)

    await asyncio.gather(*[collect(task_wait_random(max_delay))
                           for _ in range(n)])

    return delays
