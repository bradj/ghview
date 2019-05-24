# GHView

Welcome to GHView, a CLI for GitHub Organizations.

## Getting Started

1. Clone this repo
1. `pipenv install`
1. `pipenv run org hulu 15`

## Authenticating

1. Go to your [GitHub Settings](https://github.com/settings/tokens)
1. Create a Personal Access Token (PAT). No permissions are required.
1. `export GHVIEW_USERNAME=[github username]`
1. `export GHVIEW_PAT=[PAT]`
1. `pipenv run org amazon 15`
