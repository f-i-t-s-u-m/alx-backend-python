#!/usr/bin/env python3
""" python file with safely get value function """

from typing import Union, Mapping, Any, TypeVar


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[TypeVar('T'), None] = None)\
                             -> Union[Any, TypeVar('T')]:
    """ safely_get_value function """
    if key in dct:
        return dct[key]
    else:
        return default
