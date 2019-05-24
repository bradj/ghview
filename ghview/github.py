import click
from datetime import datetime
import requests
import sys
import traceback

from config import repos_url, org_url


def next_page(link_header):
    links = link_header.split(',')

    for link in links:
        if link.find('rel="next"') >= 0:
            start = link.find('<')
            end = link.find('>')

            return link[start + 1:end]

    return None


def check_throttle(response):
    if response.status_code == 403:
        epoch_utc = int(response.headers['X-RateLimit-Reset'])

        resume_time = datetime.fromtimestamp(epoch_utc).strftime('%c')

        click.echo(f'\nGitHub has started to throttle your requests.')
        click.echo(f'Additional requests can be made at {resume_time}.')


def request(url, username=None, pat=None):
    if username and pat:
        r = requests.get(url, auth=(username, pat))
    else:
        r = requests.get(url)

    if r.status_code != requests.codes.ok:
        check_throttle(r)
        click.echo(f'GitHub returned HTTP code {r.status_code} for {url}')
        raise Exception(f'Request {url} failed')

    return r


def get_repos(organization, page_url=None, username=None, pat=None):
    if page_url:
        url = page_url
    else:
        url = repos_url(organization)

    r = request(url, username, pat)

    try:
        repos = r.json()

        if 'Link' in r.headers:
            page_url = next_page(r.headers['Link'])

            if page_url:
                repos.extend(get_repos(organization, page_url, username, pat))

        return repos
    except Exception as ex:
        print(ex)
        click.echo('Could not parse the response from GitHub')
        click.echo(r.text[:600])


def get_prs(url, username=None, pat=None):
    r = request(url, username, pat)

    try:
        pr_list = r.json()

        if (len(pr_list) > 0):
            return pr_list[0]['number']

        return 0
    except Exception as ex:
        click.echo(f'Error parsing response for {url}')
        sys.exit(1)
