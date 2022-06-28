#!/usr/bin/env python3
""" python file with one function """

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ function to comprehens data """
    return [data async for data in async_generator()]
