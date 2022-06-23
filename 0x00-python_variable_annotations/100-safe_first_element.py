#!/usr/bin/env python3
""" python file """

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, type(None)]:
    """ safe first element """
    if lst:
        return lst[0]
    else:
        return None

