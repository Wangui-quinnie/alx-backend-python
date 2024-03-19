#!/usr/bin/env python3
"""
Returns the list of random default values in ascending order.
"""

import asyncio
from typing import List
from random import uniform
from itertools import repeat

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Creates an asyncio.Task for the wait_random coroutine.

    Args:
        n (int): The number of times to call wait_random.
        max_delay (int): The maximum delay in seconds.

    Returns:
        List[float]: A list of delays.
    """
    delays: List[float] = await asyncio.gather(
        *(wait_random(max_delay) for _ in repeat(None, n))
        )
    return sorted(delays)
