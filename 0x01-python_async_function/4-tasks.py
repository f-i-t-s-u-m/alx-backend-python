#!/usr/bin/env python3
""" python async task file """


import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """ run cocurrent functions """
    tasks = []
    dtask = []
    for i in range(n):
        res = task_wait_random(max_delay)
        tasks.append(res)
        res.add_done_callback(lambda x: dtask.append(x.result()))
    for task in tasks:
        await task
    return dtask
