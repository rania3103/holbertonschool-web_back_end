#!/usr/bin/env python3
"""Annotate a function’s parameters
and return values with the appropriate types"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns a list of tuples of elements and their lengths"""
    return [(i, len(i)) for i in lst]
