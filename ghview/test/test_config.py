from ghview import config
import json


def test_repos_url():
    org = 'testorg'
    url = config.repos_url(org)

    assert(url == f'https://api.github.com/orgs/{org}/repos?per_page=100')


def test_repos_url_limit():
    limit = 50
    org = 'testorg'
    url = config.repos_url(org, limit=limit)

    assert(url == f'https://api.github.com/orgs/{org}/repos?per_page={limit}')


def test_org_url():
    org = 'testorg'
    url = config.org_url(org)

    assert(url == f'https://api.github.com/orgs/{org}')
