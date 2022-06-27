#!/usr/bin/env python3
""" python basic function """

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ return random wait """

    rn = random.uniform(0, max_delay)
    await asyncio.sleep(rn)
    return rn
