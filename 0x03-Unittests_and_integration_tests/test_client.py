#!/usr/bin/env python3

"""
Test Client Module
"""

import unittest
from unittest.mock import patch
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """
    TestGithubOrgClient class to test GithubOrgClient class.
    """

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.GithubOrgClient.get_json')
    def test_org(self, org_name, mock_get_json):
        """
        Test org method of GithubOrgClient class.
        """
        test_payload = {"name": org_name}
        mock_get_json.return_value = test_payload

        github_client = GithubOrgClient(org_name)
        result = github_client.org

        mock_get_json.assert_called_once_with(
            'https://api.github.com/orgs/' + org_name
        )
        self.assertEqual(result, test_payload)

    def test_public_repos_url(self):
        """
        Test _public_repos_url method of GithubOrgClient class.
        """
        # Mock the org method to return a known payload
        known_payload = {
            "repos_url": "https://api.github.com/orgs/testorg/repos"
        }
        with patch.object(GithubOrgClient, 'org', return_value=known_payload):
            github_client = GithubOrgClient("testorg")
            result = github_client._public_repos_url

        expected_url = "https://api.github.com/orgs/testorg/repos"
        self.assertEqual(result, expected_url)


if __name__ == "__main__":
    unittest.main()
