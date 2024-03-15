#!/usr/bin/env python3
"""
Module for sum_list function.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Function that takes a list of floats and returns their sum.

    Args:
        input_list: The list of floats.

    Returns:
        The sum of the input list as a float.
    """
    return sum(input_list)
