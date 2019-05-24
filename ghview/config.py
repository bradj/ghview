_api_url = 'https://api.github.com/'


def repos_url(org, limit=100):
    return f'{_api_url}orgs/{org}/repos?per_page={limit}'


def org_url(org):
    return f'{_api_url}orgs/{org}'
