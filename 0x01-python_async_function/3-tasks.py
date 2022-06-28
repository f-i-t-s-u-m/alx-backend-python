#!/usr/bin/env python3
""" python file with tasks function """

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ task wait random time function """
    return asyncio.create_task(wait_random(max_delay))
