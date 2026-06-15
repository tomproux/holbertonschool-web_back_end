#!/usr/bin/env python3
"""Module containing the task_wait_random function."""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Create and return an asyncio Task for wait_random.

    Wraps wait_random in an asyncio.Task using the running event loop,
    allowing the coroutine to be scheduled for concurrent execution.

    Args:
        max_delay: Maximum number of seconds wait_random may delay.

    Returns:
        An asyncio.Task wrapping the wait_random coroutine.
    """
    return asyncio.get_event_loop().create_task(wait_random(max_delay))
