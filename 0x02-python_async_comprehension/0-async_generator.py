#!/usr/bin/env python3
""" python file with one function """

import random
import asyncio
from typing import Iterator


async def async_generator() -> Iterator[float]:
    """ async_generator function """
    for _ in range(10):
        await asyncio.sleep(1)
        yield 10 * random.random()
