#!/usr/bin/env python3
"""
Creates an asyncio.Task for the wait_n coroutine.
"""

from typing import List
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_random_wrapper(max_delay: int) -> float:
    """
    Wrapper function for wait_random coroutine.

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        float: The random delay.
    """
    return await wait_random(max_delay)


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Creates an asyncio.Task for the wait_random coroutine.

    Args:
        n (int): The number of times to call wait_random.
        max_delay (int): The maximum delay in seconds.

    Returns:
        List[float]: A list of delays.
    """
    tasks = [wait_random_wrapper(max_delay) for _ in range(n)]
    return await asyncio.gather(*tasks)
