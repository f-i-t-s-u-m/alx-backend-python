#!/usr/bin/env python3
""" python basic function """

import random


async def wait_random(max_delay: int = 10) -> float:
    """ return random wait """
    return random.uniform(0, max_delay)
