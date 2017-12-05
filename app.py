import json
import numpy as np
import pandas as pd
import requests

# Get all org repos for lodash
org_repos = requests.get('https://api.github.com/orgs/lodash/repos')
df_repos = pd.DataFrame(org_repos.json(), columns=['name'])
df_prs = pd.DataFrame()

def get_repo_prs(repo):
    r = requests.get('https://api.github.com/repos/lodash/' + repo + '/pulls?state=all')
    df_tmp = pd.DataFrame(r.json(), columns=['user'])
    print (df_tmp)
    df_prs.append(df_tmp)

for r in range(0, df_repos.size):
    get_repo_prs(df_repos.iloc[r]['name'])

print (df_prs)
