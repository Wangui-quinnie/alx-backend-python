#!/usr/bin/env python3
"""
Module for make_multiplier function.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Function that takes a float multiplier as argument and returns
    a function that
    multiplies a float by multiplier.

    Args:
        multiplier: The multiplier value.

    Returns:
        A function that multiplies a float by the multiplier.
    """
    def multiplier_function(x: float) -> float:
        """
        Inner function that multiplies a float by the multiplier.

        Args:
            x: The float value to be multiplied.

        Returns:
            The result of multiplying x by the multiplier.
        """
        return x * multiplier

    return multiplier_function
