#!/usr/bin/env python3
"""
Module for zoom_array function.
"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zooms in on the array lst by repeating each element factor times.

    Args:
        lst: The input array to be zoomed in.
        factor: The zooming factor, specifying how many times each element
        should be repeated.

    Returns:
        List[int]: The zoomed-in array.
    """
    zoomed_in: List = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in


if __name__ == "__main__":
    zoom_array = __import__('102-type_checking').zoom_array
    print(zoom_array.__annotations__)
