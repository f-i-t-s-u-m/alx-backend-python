#!/usr/bin/env python3
""" python file with one function """

import random
import asyncio
from typing import Iterator


async def async_generator() -> Iterator[float]:
    for _ in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
