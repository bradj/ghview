import json
import pytest


@pytest.fixture(scope="module")
def new_obj():
    return lambda dictionary: type('obj', (object,), dictionary)

@pytest.fixture(scope="module")
def link_header_first():
    return '<https://api.github.com/organizations/913567/repos?per_page=100&page=2>; rel="next", <https://api.github.com/organizations/913567/repos?per_page=100&page=2>; rel="last"'


@pytest.fixture(scope="module")
def link_header_middle():
    return '<https://api.github.com/organizations/913567/repos?per_page=10&page=4>; rel="prev", <https://api.github.com/organizations/913567/repos?per_page=10&page=6>; rel="next", <https://api.github.com/organizations/913567/repos?per_page=10&page=16>; rel="last", <https://api.github.com/organizations/913567/repos?per_page=10&page=1>; rel="first"'


@pytest.fixture(scope="module")
def link_header_last():
    return '<https://api.github.com/organizations/913567/repos?per_page=10&page=15>; rel="prev", <https://api.github.com/organizations/913567/repos?per_page=10&page=1>; rel="first"'


@pytest.fixture(scope="module")
def raw_repo():
    raw_repo = '''
{
        "id": 2044029,
        "node_id": "MDEwOlJlcG9zaXRvcnkyMDQ0MDI5",
        "name": "astyanax",
        "full_name": "Netflix/astyanax",
        "private": false,
        "owner": {
            "login": "Netflix",
            "id": 913567,
            "node_id": "MDEyOk9yZ2FuaXphdGlvbjkxMzU2Nw==",
            "avatar_url": "https://avatars3.githubusercontent.com/u/913567?v=4",
            "gravatar_id": "",
            "url": "https://api.github.com/users/Netflix",
            "html_url": "https://github.com/Netflix",
            "followers_url": "https://api.github.com/users/Netflix/followers",
            "following_url": "https://api.github.com/users/Netflix/following{/other_user}",
            "gists_url": "https://api.github.com/users/Netflix/gists{/gist_id}",
            "starred_url": "https://api.github.com/users/Netflix/starred{/owner}{/repo}",
            "subscriptions_url": "https://api.github.com/users/Netflix/subscriptions",
            "organizations_url": "https://api.github.com/users/Netflix/orgs",
            "repos_url": "https://api.github.com/users/Netflix/repos",
            "events_url": "https://api.github.com/users/Netflix/events{/privacy}",
            "received_events_url": "https://api.github.com/users/Netflix/received_events",
            "type": "Organization",
            "site_admin": false
        },
        "html_url": "https://github.com/Netflix/astyanax",
        "description": "Cassandra Java Client",
        "fork": false,
        "url": "https://api.github.com/repos/Netflix/astyanax",
        "forks_url": "https://api.github.com/repos/Netflix/astyanax/forks",
        "keys_url": "https://api.github.com/repos/Netflix/astyanax/keys{/key_id}",
        "collaborators_url": "https://api.github.com/repos/Netflix/astyanax/collaborators{/collaborator}",
        "teams_url": "https://api.github.com/repos/Netflix/astyanax/teams",
        "hooks_url": "https://api.github.com/repos/Netflix/astyanax/hooks",
        "issue_events_url": "https://api.github.com/repos/Netflix/astyanax/issues/events{/number}",
        "events_url": "https://api.github.com/repos/Netflix/astyanax/events",
        "assignees_url": "https://api.github.com/repos/Netflix/astyanax/assignees{/user}",
        "branches_url": "https://api.github.com/repos/Netflix/astyanax/branches{/branch}",
        "tags_url": "https://api.github.com/repos/Netflix/astyanax/tags",
        "blobs_url": "https://api.github.com/repos/Netflix/astyanax/git/blobs{/sha}",
        "git_tags_url": "https://api.github.com/repos/Netflix/astyanax/git/tags{/sha}",
        "git_refs_url": "https://api.github.com/repos/Netflix/astyanax/git/refs{/sha}",
        "trees_url": "https://api.github.com/repos/Netflix/astyanax/git/trees{/sha}",
        "statuses_url": "https://api.github.com/repos/Netflix/astyanax/statuses/{sha}",
        "languages_url": "https://api.github.com/repos/Netflix/astyanax/languages",
        "stargazers_url": "https://api.github.com/repos/Netflix/astyanax/stargazers",
        "contributors_url": "https://api.github.com/repos/Netflix/astyanax/contributors",
        "subscribers_url": "https://api.github.com/repos/Netflix/astyanax/subscribers",
        "subscription_url": "https://api.github.com/repos/Netflix/astyanax/subscription",
        "commits_url": "https://api.github.com/repos/Netflix/astyanax/commits{/sha}",
        "git_commits_url": "https://api.github.com/repos/Netflix/astyanax/git/commits{/sha}",
        "comments_url": "https://api.github.com/repos/Netflix/astyanax/comments{/number}",
        "issue_comment_url": "https://api.github.com/repos/Netflix/astyanax/issues/comments{/number}",
        "contents_url": "https://api.github.com/repos/Netflix/astyanax/contents/{+path}",
        "compare_url": "https://api.github.com/repos/Netflix/astyanax/compare/{base}...{head}",
        "merges_url": "https://api.github.com/repos/Netflix/astyanax/merges",
        "archive_url": "https://api.github.com/repos/Netflix/astyanax/{archive_format}{/ref}",
        "downloads_url": "https://api.github.com/repos/Netflix/astyanax/downloads",
        "issues_url": "https://api.github.com/repos/Netflix/astyanax/issues{/number}",
        "pulls_url": "https://api.github.com/repos/Netflix/astyanax/pulls{/number}",
        "milestones_url": "https://api.github.com/repos/Netflix/astyanax/milestones{/number}",
        "notifications_url": "https://api.github.com/repos/Netflix/astyanax/notifications{?since,all,participating}",
        "labels_url": "https://api.github.com/repos/Netflix/astyanax/labels{/name}",
        "releases_url": "https://api.github.com/repos/Netflix/astyanax/releases{/id}",
        "deployments_url": "https://api.github.com/repos/Netflix/astyanax/deployments",
        "created_at": "2011-07-13T20:24:30Z",
        "updated_at": "2019-05-23T01:58:41Z",
        "pushed_at": "2018-10-04T03:01:43Z",
        "git_url": "git://github.com/Netflix/astyanax.git",
        "ssh_url": "git@github.com:Netflix/astyanax.git",
        "clone_url": "https://github.com/Netflix/astyanax.git",
        "svn_url": "https://github.com/Netflix/astyanax",
        "homepage": "",
        "size": 6990,
        "stargazers_count": 1007,
        "watchers_count": 1007,
        "language": "Java",
        "has_issues": true,
        "has_projects": true,
        "has_downloads": true,
        "has_wiki": true,
        "has_pages": true,
        "forks_count": 372,
        "mirror_url": null,
        "archived": false,
        "disabled": false,
        "open_issues_count": 161,
        "license": {
            "key": "apache-2.0",
            "name": "Apache License 2.0",
            "spdx_id": "Apache-2.0",
            "url": "https://api.github.com/licenses/apache-2.0",
            "node_id": "MDc6TGljZW5zZTI="
        },
        "forks": 372,
        "open_issues": 161,
        "watchers": 1007,
        "default_branch": "master",
        "permissions": {
            "admin": false,
            "push": false,
            "pull": true
        }
    }
'''

    return json.loads(raw_repo)
