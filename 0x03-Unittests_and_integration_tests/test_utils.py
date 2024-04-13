#!/usr/bin/env python3

"""
Utils Module
"""

from parameterized import parameterized
import unittest
from typing import Any, Dict, Tuple
import requests
from unittest.mock import patch, Mock


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


def get_json(url: str) -> dict:
    """
    Get JSON data from a URL.

    Args:
        url: The URL to fetch JSON data from.

    Returns:
        A dictionary containing the JSON data.
    """
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


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


class TestGetJson(unittest.TestCase):
    """
    TestGetJson class to test get_json function.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        Test get_json function with mocked requests.get.
        """
        mock_get.return_value = Mock()
        mock_get.return_value.json.return_value = test_payload

        result = get_json(test_url)

        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


if __name__ == "__main__":
    unittest.main()
