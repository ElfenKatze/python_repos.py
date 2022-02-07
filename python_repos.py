import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Aceppt': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"status code: {r.status_code}")

# store API response in a variable.
response_dict = r.json()

# process results.
print(response_dict.keys())

print(f"total repositories: {response_dict['total_count']}")

# explore information about the repositories
repo_dict = response_dict['items']
print(f"repositories returned: {len(repo_dict)}")

print("\nSelected information about each repository:")
for repo_dict in repo_dict:
 print(f"\nName: {repo_dict['name']}")
 print(f"Owner: {repo_dict['owner']['login']}")
 print(f"Stars: {repo_dict['stargazers_count']}")
 print(f"Repository: {repo_dict['html_url']}")
 print(f"Description: {repo_dict['description']}")