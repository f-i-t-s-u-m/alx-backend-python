#!/usr/bin/env python3
""" python file with tasks function """

import asyncio
import time
from typing import Awaitable
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> type(asyncio.Task):
    """ task wait random time function """
    return asyncio.Task(wait_random(max_delay))
