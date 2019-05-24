# GHView

Welcome to GHView, a CLI for GitHub Organizations.

## Getting Started

*Note: This has been tested on Python 3.7 though 3.x should be fine.*

1. Clone this repo
1. `python setup.py install`
1. `ghview --help`

### Authenticating

1. Go to your [GitHub Settings](https://github.com/settings/tokens)
1. Create a Personal Access Token (PAT). No permissions are required.
1. `export GHVIEW_USERNAME=[github username]`
1. `export GHVIEW_PAT=[PAT]`
1. `ghview amazon 15`

## Developing

### Requirements

* [Pipenv](https://pipenv.readthedocs.io/en/latest/)

### Getting Started

1. `pipenv install`
1. make changes
1. `pipenv run test`

or

1. `python setup.py develop` - creates symlinks back to the code
1. make changes
1. `ghview` in your shell will be synced with your local *GHview* code
1. `pipenv run test` still works

## TODO

1. CI/CD
1. Serialize GitHub responses