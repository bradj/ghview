from ghview.repo import Repo
import json


def test_ctor(raw_repo):
    r = Repo(raw_repo)

    assert(r.name == 'astyanax')
    assert(r.stars == 1007)
    assert(r.forks == 372)
    assert(r.pr_url == 'https://api.github.com/repos/Netflix/astyanax/pulls?state=open&per_page=1')


def test_contrib_percentage(raw_repo):
    r = Repo(raw_repo)

    r.forks = 100
    r.pr_count = 50

    assert(r.contrib == 50)

    r.forks = 100
    r.pr_count = 101

    assert(r.contrib == 101)

    r.forks = 0
    r.pr_count = 101

    assert(r.contrib == 100)

    r.forks = 100
    r.pr_count = 0

    assert(r.contrib == 0)
