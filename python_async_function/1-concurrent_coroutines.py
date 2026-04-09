#!/usr/bin/env python3
"""Module for wait_n coroutine"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times and return delays in ascending order"""
    delays = await asyncio.gather(*[wait_random(max_delay) for _ in range(n)])
    sorted_delays = []
    for delay in delays:
        inserted = False
        for i, val in enumerate(sorted_delays):
            if delay <= val:
                sorted_delays.insert(i, delay)
                inserted = True
                break
        if not inserted:
            sorted_delays.append(delay)
    return sorted_delays
