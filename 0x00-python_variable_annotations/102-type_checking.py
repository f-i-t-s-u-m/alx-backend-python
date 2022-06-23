#!/usr/bin/env python3
""" python file with one function"""

from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """ zoom array function """
    zoomed_in: List = [
            item for item in lst
            for i in range(factor)
            ]

    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(tuple(array))

zoom_3x = zoom_array(tuple(array), 3)
