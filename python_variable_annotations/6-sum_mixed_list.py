#!/usr/bin/env python3
"""Write a type-annotated function sum_mixed_list
which takes a list mxd_lst of integers
and floats and returns their sum as a float."""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """returns sum of the mxs_lst as a float."""
    sum: float = 0.0
    for numb in mxd_lst:
        sum += numb
    return sum
