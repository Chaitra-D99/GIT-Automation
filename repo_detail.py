import requests


GITHUB_API_URL = "https://api.github.com/repos/{owner}/{repo}"


OWNER = ''
REPO = ''

GITHUB_TOKEN = 'your_github_token_here'


headers = {
    'Authorization': f'token {GITHUB_TOKEN}'
}


def fetch_repo_details(owner, repo):

    url = GITHUB_API_URL.format(owner=owner, repo=repo)

    try:

        response = requests.get(url, headers=headers)


        if response.status_code == 200:
            repo_data = response.json()


            details = {
                'name': repo_data['name'],
                'full_name': repo_data['full_name'],
                'owner': repo_data['owner']['login'],
                'description': repo_data['description'],
                'url': repo_data['html_url'],
                'stars': repo_data['stargazers_count'],
                'forks': repo_data['forks_count'],
                'open_issues': repo_data['open_issues_count'],
                'language': repo_data['language'],
                'created_at': repo_data['created_at'],
                'updated_at': repo_data['updated_at'],
                'pushed_at': repo_data['pushed_at']
            }

            return details
        else:
            print(f"Error: {response.status_code}, {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None



repo_details = fetch_repo_details(OWNER, REPO)

if repo_details:
    print("Repository Details:")
    for key, value in repo_details.items():
        print(f"{key}: {value}")
