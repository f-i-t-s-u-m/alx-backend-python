#!/usr/bin/env python3
""" python async task file """


import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """ run cocurrent functions """
    tasks = []
    dtask = []
    for i in range(n):
        res = asyncio.create_task(wait_random(max_delay))
        tasks.append(res)
        res.add_done_callback(lambda x: dtask.append(x.result()))

    for task in tasks:
        await task
    return dtask
