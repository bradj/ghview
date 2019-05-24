#!/usr/bin/env python

import click
from concurrent.futures import ThreadPoolExecutor, as_completed
from halo import Halo
import sys

import config
from github import get_repos, get_prs
from repo import Repo


def print_stars(repos, top_n):
    print(f'Top {top_n} starred repos')

    for repo in repos:
        print(' {:>5} - {}'.format(repo.stars, repo.name))


def print_forks(repos, top_n):
    print(f'Top {top_n} forked repos')

    for repo in repos:
        print(' {:>5} - {}'.format(repo.forks, repo.name))


def print_prs(repos, top_n):
    print(f"Top {top_n} repos with the most PR's")

    for repo in repos:
        print(' {:>5} - {}'.format(repo.pr_count, repo.name))


def print_contrib(repos, top_n):
    print(f"Top {top_n} repos with the highest contribution percentage (PRs / Forks)")

    for repo in repos:
        print(' {:>5d} - {}'.format(int(repo.contrib), repo.name))


@click.command()
@click.argument('organization', required=True)
@click.argument('top_n', type=click.INT, required=True)
@click.option('--username', envvar='GHVIEW_USERNAME', help='GitHub username')
@click.option('--pat', envvar='GHVIEW_PAT', help='GitHub personal access token')
@click.version_option(version='0.1.0')
def parse(organization, top_n, username, pat):
    """                                      
  Welcome to GHView, a CLI for GitHub Organizations.

  \b
  Environment Variables:  
    GHVIEW_USERNAME = GitHub Username
    GHVIEW_PAT      = GitHub personal access token

  Using GitHub credentials boosts your rate limit from 60/hr to 5000/hr.

  https://developer.github.com/v3/#rate-limiting
  """
    print()
    try:
        raw_repos = get_repos(organization, username=username, pat=pat)
    except Exception as ex:
        click.echo('Error collecting repos')
        sys.exit(1)

    repos = []

    with Halo(text='Retrieving repos...', spinner='dots'):
        for raw_repo in raw_repos:
            repos.append(Repo(raw_repo))

    if len(repos) == 0:
        print('No public repos were found')
        sys.exit(0)

    with Halo(text='Retrieving pull requests...', spinner='dots'):
        try:
            with ThreadPoolExecutor(max_workers=5) as executor:
                future_to_repo = {executor.submit(get_prs, repo.pr_url, username, pat): repo for repo in repos}
                for future in as_completed(future_to_repo):
                    repo = future_to_repo[future]

                    repo.pr_count = future.result()
        except Exception as exc:
                    print('%r generated an exception: %s' % (repo.name, exc))
                    sys.exit(1)

    top_star = sorted(repos, key=lambda repo: repo.stars, reverse=True)[:top_n]
    top_fork = sorted(repos, key=lambda repo: repo.forks, reverse=True)[:top_n]
    top_prs = sorted(repos, key=lambda repo: repo.pr_count, reverse=True)[:top_n]
    top_contrib = sorted(repos, key=lambda repo: repo.contrib, reverse=True)[:top_n]

    print_stars(top_star, top_n)
    print_forks(top_fork, top_n)
    print_prs(top_prs, top_n)
    print_contrib(top_contrib, top_n)


if __name__ == '__main__':
    parse()
