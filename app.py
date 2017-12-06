""" github REST API v3 - https://developer.github.com/v3/ """
import pandas as pd
import requests

# Using basic auth for ease of use right now
USER_NAME = '<user' # CHANGE ME!
USER_PWD = '<password>' # CHANGE ME!

# Get all org repos for lodash
org_repos = requests.get('https://api.github.com/orgs/lodash/repos', auth=(USER_NAME, USER_PWD))
# Store in memory data store of repo names
df_repos = pd.DataFrame(org_repos.json(), columns=['name'])

# Get pull requests for a repository regarless of pull request state
def get_repo_prs(repo):
    response = requests.get('https://api.github.com/repos/lodash/' + repo + '/pulls?state=all', auth=(USER_NAME, USER_PWD))
    return pd.DataFrame(response.json())

# Concat each repos list of pull requests into a single data store for further analysis
all_prs = pd.concat([get_repo_prs(df_repos.iloc[i]['name']) for i in range(df_repos.size)], ignore_index=True)

# Print test output as json - records
print (all_prs.to_json(orient='records'))
