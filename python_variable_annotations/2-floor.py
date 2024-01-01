#!/usr/bin/env python3
"""Write a type-annotated function floor
which takes a float n as argument
and returns the floor of the float."""

from math import floor as fl


def floor(n: float) -> int:
    """returns the floor of the float."""
    return fl(n)
