#!/usr/bin/env python3
"""Module containing the measure_time function."""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the average execution time per coroutine for wait_n.

    Args:
        n: Number of times to spawn wait_random.
        max_delay: Maximum delay value to pass to wait_n.

    Returns:
        Average elapsed time per coroutine (total_time / n).
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = time.perf_counter() - start

    return elapsed / n
