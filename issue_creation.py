import requests
import json


GITHUB_USERNAME = 'your_username'
GITHUB_TOKEN = 'your_personal_access_token'


API_URL = 'https://api.github.com/repos/your_username/your_repo/issues'

# Issue details
issue_data = {
    "title": "Bug: Example Issue",
    "body": "This is a description of the issue.",
    "labels": ["bug"],
}


auth = (GITHUB_USERNAME, GITHUB_TOKEN)


response = requests.post(API_URL, auth=auth, json=issue_data)


if response.status_code == 201:
    issue = response.json()
    print(f"Issue created successfully! Title: {issue['title']}")
    print(f"URL: {issue['html_url']}")
else:
    print(f"Failed to create issue: {response.status_code}")
    print(f"Response: {response.text}")
