#!/usr/bin/python3
"""Import async_generator from the previous
task and then write a coroutine called
async_comprehension that takes no arguments."""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """The coroutine will loop 10 times,
    each time asynchronously wait 1 second, then yield
    a random number between 0 and 10. Use the random module."""
    for i in range(10):
        await asyncio.sleep(1)
        random_numb = random.uniform(0, 10)
        yield random_numb


async def async_comprehension():
    """The coroutine will collect 10 random
    numbers using an async comprehensing
    over async_generator, then return
    the 10 random numbers."""
    return [number async for number in async_generator()]
