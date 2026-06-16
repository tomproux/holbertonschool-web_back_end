#!/usr/bin/env python3
"""Module containing the measure_runtime coroutine."""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure the total runtime of four parallel async_comprehension calls.

    Executes async_comprehension four times concurrently using asyncio.gather
    and returns the total elapsed time in seconds.

    Returns:
        Total elapsed time in seconds as a float.
    """
    start = time.perf_counter()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    return time.perf_counter() - start
