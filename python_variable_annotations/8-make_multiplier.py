#!/usr/bin/env python3
"""Write a type-annotated function make_multiplier
that takes a float multiplier as argument and
returns a function that multiplies a float by multiplier."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function that multiplies a float by the multiplier."""
    def fun_to_multiply(n: float) -> float:
        """this function will multiply the float by the multiplier"""
        return n * multiplier
    return fun_to_multiply
