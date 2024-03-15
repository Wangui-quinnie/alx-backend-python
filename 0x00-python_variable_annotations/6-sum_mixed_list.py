#!/usr/bin/env python3
"""
Module for sum_mixed_list function.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Function that takes a list of integers and floats and returns their sum.

    Args:
        mxd_lst: The list of integers and floats.

    Returns:
        The sum of the input list as a float.
    """
    return sum(mxd_lst)
