""" github REST API v3 - https://developer.github.com/v3/ """
import pandas as pd
import re
import requests

class OrgPullRequestInfo:
    page_pattern = re.compile('(?<=&page=)(.*?)(?=\>)')

    # Using basic auth for ease of use right now
    def __init__(self, org):
        self.orgname = org
        self.USER_NAME = '<user>' # CHANGE ME!
        self.USER_PWD = '<password>' # CHANGE ME!

    # Get all org repos for lodash
    def get_org_repos(self, org):
        org_repos = requests.get(f'https://api.github.com/orgs/{org}/repos', auth=(self.USER_NAME, self.USER_PWD))
        # Store in memory data store of repo names
        return pd.DataFrame(org_repos.json(), columns=['name'])

    # Get pull requests for a repository regarless of pull request state
    def get_repo_prs(self, repo):
        response = requests.get(f'https://api.github.com/repos/lodash/{repo}/pulls?state=all&per_page=100', auth=(self.USER_NAME, self.USER_PWD))
        page_max = self.page_pattern.findall(str(response.headers))
        df = pd.DataFrame()
        # Check if there is pagination to this response
        if page_max:
            for i in range(1, int(page_max[-1])+1):
                response = requests.get(f'https://api.github.com/repos/lodash/{repo}/pulls?state=all&page={i}&per_page=100', auth=(self.USER_NAME, self.USER_PWD))
                df = pd.concat([df, pd.DataFrame(response.json())], ignore_index=True)
        else:
            df = pd.DataFrame(response.json())
        return df

    # Get pull request info for org
    def get_pr_info(self):
        org_repos = self.get_org_repos(self.orgname)
        # Concat each repos list of pull requests into a single data store for further analysis
        return pd.concat([self.get_repo_prs(org_repos.iloc[i]['name']) for i in range(org_repos.size)], ignore_index=True)

if __name__ == '__main__':
    pr = OrgPullRequestInfo('lodash')
    pr_output = pr.get_pr_info()
    # Print test output as number of pull requests
    print (pr_output.count()['id'])
