#! usr/bin/env python3
""" python file contained sum_mixed_list """

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ return sum of mixed list """
    return sum(mxd_lst)
