#!/usr/bin/env python3
"""Write a function named index_range
that takes two integer arguments page and page_size"""


def index_range(page, page_size):
    """ return in a list for those
    particular pagination parameters."""
    start_index = (page - 1) * page_size
    return (start_index, start_index + page_size)
