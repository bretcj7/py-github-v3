""" github REST API v3 - https://developer.github.com/v3/ """
import pandas as pd
import requests

class OrgPullRequestInfo:

    # Using basic auth for ease of use right now
    def __init__(self, org):
        self.orgname = org
        self.USER_NAME = '<user>' # CHANGE ME!
        self.USER_PWD = '<password>' # CHANGE ME!

    # Get all org repos for lodash
    def __get_org_repos(self, org):
        org_repos = requests.get(f'https://api.github.com/orgs/{org}/repos', auth=(self.USER_NAME, self.USER_PWD))
        # Store in memory data store of repo names
        return pd.DataFrame(org_repos.json(), columns=['name'])

    # Get pull requests for a repository regarless of pull request state
    def __get_repo_prs(self, repo):
        response = requests.get(f'https://api.github.com/repos/lodash/{repo}/pulls?state=all', auth=(self.USER_NAME, self.USER_PWD))
        return pd.DataFrame(response.json())

    # Get pull request info for org
    def get_pr_info(self):
        org_repos = self.__get_org_repos(self.orgname)
        # Concat each repos list of pull requests into a single data store for further analysis
        return pd.concat([self.__get_repo_prs(org_repos.iloc[i]['name']) for i in range(org_repos.size)], ignore_index=True)

pr = OrgPullRequestInfo('lodash')
pr_output = pr.get_pr_info()
# Print test output as json - records
print (pr_output.to_json(orient='records'))
