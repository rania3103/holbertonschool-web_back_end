#!/usr/bin/env python3
"""Import wait_random from the previous python file
that you’ve written and write an async routine
called wait_n that takes in 2 int arguments
(in this order): n and max_delay. You will spawn
wait_random n times with the specified max_delay."""
import random
import asyncio
from typing import List


async def wait_random(max_delay: int = 10) -> float:
    """ waits for a random delay between 0 and max_delay
    seconds and eventually returns it."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ wait_n should return the list of all the delays
    (float values). The list of the delays should
    be in ascending order without using sort()
    because of concurrency."""
    l: list = []
    for i in range(n):
        delay = wait_random(max_delay)
        l.append(delay)
    return sorted(await asyncio.gather(*l))


def measure_time(n: int, max_delay: int) -> float:
    """ Create a measure_time function with integers n
    and max_delay as arguments that measures the
    total execution time for wait_n(n, max_delay),
    and returns total_time / n. Your function
    should return a float."""
    delays = asyncio.run(wait_n(n, max_delay))
    return sum(delays) / n
