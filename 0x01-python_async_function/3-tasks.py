#!/usr/bin/env python3
""" python file with tasks function """

import asyncio
import time
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int):
    """ task wait random time function """
    return asyncio.Task(wait_random(max_delay))
