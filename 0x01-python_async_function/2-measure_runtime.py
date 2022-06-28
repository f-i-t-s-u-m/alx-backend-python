#!/usr/bin/env python3
""" python file with one function inside """

import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ measure time taken to complete the function """

    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    return time.perf_counter() - start