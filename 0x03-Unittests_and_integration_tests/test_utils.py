#!/usr/bin/env python3

"""
Utils Module
"""

from parameterized import parameterized
import unittest
from typing import Any, Dict, Tuple


def access_nested_map(nested_map: Dict[str, Any], path: Tuple[str]) -> Any:
    """
    Access nested values in a dictionary using a path of keys.

    Args:
        nested_map: The nested dictionary.
        path: A tuple representing the path to the desired value.

    Returns:
        The value at the specified path.

    Raises:
        KeyError: If the path is not found in the nested map.
    """
    try:
        for key in path:
            nested_map = nested_map[key]
        return nested_map
    except KeyError:
        raise KeyError("Path not found in nested map")


class TestAccessNestedMap(unittest.TestCase):
    """
    TestAccessNestedMap class to test access_nested_map function.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test access_nested_map function with various inputs.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(
            self, nested_map, path):
        """
        Test access_nested_map function raises KeyError with expected message.
        """
        self.assertRaises(KeyError)


if __name__ == "__main__":
    unittest.main()
