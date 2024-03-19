#!/usr/bin/env python3
"""
Asynchronous coroutine that spawns wait_random n times with the
specified max_delay.
"""

import asyncio
import random
from typing import List, Callable

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawns wait_random n times with the
    specified max_delay.

    Args:
        n (int): Number of times to call wait_random.
        max_delay (int): The maximum delay in seconds.

    Returns:
        List[float]: List of all the delays in ascending order.
    """
    delays: List[float] = await asyncio.gather(
        *(wait_random(max_delay) for _ in range(n))
        )
    return sorted(delays)
