#!/usr/bin/env python3
"""
Module for element_length function.
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples containing each element of lst along with
    its length.

    Args:
        lst: An iterable of sequences.

    Returns:
        A list of tuples where each tuple contains an element of lst
        and its length.
    """
    return [(i, len(i)) for i in lst]
