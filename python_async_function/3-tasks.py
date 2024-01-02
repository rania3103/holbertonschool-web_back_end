#!/usr/bin/env python3
"""Import wait_random from the previous python file
that you’ve written and write an async routine
called wait_n that takes in 2 int arguments
(in this order): n and max_delay. You will spawn
wait_random n times with the specified max_delay."""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ waits for a random delay between 0 and max_delay
    seconds and eventually returns it."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Write a function (do not create an async function,
    use the regular function syntax to do this)
    task_wait_random that takes an integer max_delay
    and returns a asyncio.Task."""
    return asyncio.create_task(wait_random(max_delay))
