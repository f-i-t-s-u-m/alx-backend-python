#! /usr/bin/env python3
""" python file contained to kv function"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ function to_kv and return float """
    return (f'{k}', v**2)
