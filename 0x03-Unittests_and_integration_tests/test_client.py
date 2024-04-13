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


@patch('client.get_json')
@patch.object(GithubOrgClient, '_public_repos_url',
              return_value="https://api.github.com/orgs/testorg/repos")
def test_public_repos(self, mock_public_repos_url, mock_get_json):
    """
        Test public_repos method of GithubOrgClient class.
        """
    # Mock get_json to return a payload of your choice
    mock_get_json.return_value = [
        {"name": "repo1"},
        {"name": "repo2"},
        {"name": "repo3"}
    ]

    github_client = GithubOrgClient("testorg")
    result = github_client.public_repos()

    expected_repos = ["repo1", "repo2", "repo3"]
    self.assertEqual(result, expected_repos)

    # Assert that mocked property and get_json were called once
    mock_public_repos_url.assert_called_once()
    mock_get_json.assert_called_once_with(
        "https://api.github.com/orgs/testorg/repos"
    )


@parameterized.expand([
    ({"license": {"key": "my_license"}}, "my_license", True),
    ({"license": {"key": "other_license"}}, "my_license", False)
])
def test_has_license(self, repo, license_key, expected_result):
    """
        Test has_license method of GithubOrgClient class.
        """
    github_client = GithubOrgClient("testorg")
    result = github_client.has_license(repo, license_key)
    self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
