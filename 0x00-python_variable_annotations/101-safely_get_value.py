#!/usr/bin/env python3
"""
Module for safely_get_value function.
"""
from typing import Mapping, Any, TypeVar, Union

# Define a generic type variable
T = TypeVar('T')


def safely_get_value(
        dct: Mapping,
        key: Any,
        default: Union[T, None] = None
) -> Union[Any, T]:
    """
    Safely retrieves the value associated with the given key from
    the dictionary.

    Args:
        dct: A mapping (e.g., dictionary) object.
        key: The key to retrieve the value for.
        default: The default value to return if the key is not found
        (default is None).

    Returns:
        The value associated with the key if it exists, otherwise returns
        the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
