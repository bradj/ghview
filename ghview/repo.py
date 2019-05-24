import requests
import click
import sys


class Repo(object):

    def __init__(self, raw_repo):
        super(Repo, self).__init__()

        self.name = raw_repo['name'].strip()
        self.stars = int(raw_repo['stargazers_count'])
        self.forks = int(raw_repo['forks'])
        self.pr_url = self._get_pr_url(raw_repo)
        self.pr_count = 0

    @property
    def contrib(self):
        if self.pr_count > self.forks:
            return 100

        if self.pr_count == 0:
            return 0

        return self.pr_count / self.forks * 100

    def _get_pr_url(self, raw_repo):
        url = raw_repo['pulls_url'].replace('{/number}', '')

        # https://developer.github.com/v3/pulls/#parameters
        # Defaults:
        #   sorts by created
        #   order by desc
        #   ie: newest first. Newest PR # will give us PR count
        #
        #   set state to all
        #   otherwise we'll only get open pr's
        return f'{url}?state=open&per_page=1'
