#!/usr/bin/env python3
""" python file containg element length function """

from typing import Sequence, List, Tuple, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ element length function """
    return [(i, len(i)) for i in lst]
