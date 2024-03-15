#!/usr/bin/env python3
"""
Module for safe_first_element function.
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of lst if it exists, otherwise returns None.

    Args:
        lst: A sequence of elements.

    Returns:
        The first element of lst if it exists, otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
