import requests
from requests.auth import HTTPBasicAuth

import sys

BASE_URL = "https://api.github.com"


def list_repos(username, api_token):
    url = BASE_URL + f"/users/{username}/repos"
    print(f"Sending request to {url}")
    response = requests.get(url, auth=HTTPBasicAuth(username, api_token))
    print(response.json())
    return response.json()


def delete_repos(username, api_token, repos):
    for repo in repos:
        print(repo['name'])
        name = repo['name']
        if name.endswith('production') or name.endswith('staging') or name.endswith('dev'):
            delete_repo(name, username, api_token)


def delete_repo(repo, username, api_token):
    print(f"Deleting repo {repo}")
    url = BASE_URL + f"/repos/{username}/{repo}"
    print(url)
    response = requests.delete(url, auth=HTTPBasicAuth(username, api_token))
    print(response.status_code)


if __name__ == '__main__':
    username = sys.argv[1]
    api_token = sys.argv[2]
    repos = list_repos(username, api_token)
    delete_repos(username, api_token, repos)
