import requests
import json


GITHUB_USERNAME = 'your_username'
GITHUB_TOKEN = 'your_personal_access_token'

API_URL = 'https://api.github.com/user/repos'


repo_data = {
    "name": "my-new-repository",
    "description": "This is a description for my new repository.",
    "private": False,
    "auto_init": True,
    "gitignore_template": "Python"
}


auth = (GITHUB_USERNAME, GITHUB_TOKEN)

response = requests.post(API_URL, auth=auth, json=repo_data)


if response.status_code == 201:
    print(f"Repository '{repo_data['name']}' created successfully!")
    print(f"URL: {response.json()['html_url']}")
else:
    print(f"Failed to create repository: {response.status_code}")
    print(f"Response: {response.text}")
