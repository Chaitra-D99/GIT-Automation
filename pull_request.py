import requests


from dotenv import load_dotenv
import os
load_dotenv()

GITHUB_USERNAME = os.getenv('GITHUB_USERNAME')
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')


owner = 'your_username'
repo = 'your_repo'
head_branch = 'feature-branch'
base_branch = 'main'


pr_data = {
    "title": "Add feature XYZ",
    "body": "This PR adds feature XYZ to the project.",
    "head": head_branch,
    "base": base_branch
}


api_url = f"https://api.github.com/repos/{owner}/{repo}/pulls"


auth = (GITHUB_USERNAME, GITHUB_TOKEN)


response = requests.post(api_url, json=pr_data, auth=auth)


if response.status_code == 201:
    pr = response.json()
    print(f"Pull request created successfully: {pr['html_url']}")
else:
    print(f"Failed to create pull request: {response.status_code}")
    print(response.json())
