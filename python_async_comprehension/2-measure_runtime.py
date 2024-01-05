#!/usr/bin/env python3
"""Import async_generator from the previous
task and then write a coroutine called
async_comprehension that takes no arguments."""
import asyncio
import random
from typing import Generator, List
from time import time


async def async_generator() -> Generator[float, None, None]:
    """The coroutine will loop 10 times,
    each time asynchronously wait 1 second, then yield
    a random number between 0 and 10. Use the random module."""
    for i in range(10):
        await asyncio.sleep(1)
        random_numb = random.uniform(0, 10)
        yield random_numb


async def async_comprehension() -> List[float]:
    """The coroutine will collect 10 random
    numbers using an async comprehensing
    over async_generator, then return
    the 10 random numbers."""
    return [number async for number in async_generator()]


async def measure_runtime() -> float:
    """import async_comprehension from the previous
    file and write a measure_runtime coroutine that
    will execute async_comprehension four times
    in parallel using asyncio.gather"""
    start = time()
    for i in range(4):
        task = asyncio.create_task(async_comprehension())
        await asyncio.gather(task)
    end = time()
    return end - start
