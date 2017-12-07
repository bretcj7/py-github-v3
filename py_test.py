import app as tc
import pytest
import pandas as pd
import requests

# Define test fixture so class will be instantiated once per module
@pytest.fixture(scope="module")
def test_class():
    return tc.OrgPullRequestInfo('lodash')

# Test new class is of instance
def test_new_pr_class_init(test_class):
    assert isinstance(test_class, tc.OrgPullRequestInfo)

# Test basic get request of org's repos
def test_get_org_repos(test_class):
    assert test_class.get_org_repos('lodash').to_json()

# Test basic get request of pull requests for an org/repo
def test_get_repo_prs(test_class):
    assert test_class.get_repo_prs('lodash').to_json()

# Test basic data store of json to dataframe
def test_pandas_load():
    json_string = [{'id': 3955647, 'name': 'lodash', 'full_name': 'lodash/lodash'}]
    json_string2 = [{'id': 908, 'name': 'test', 'full_name': 'lodash/test', 'other': 'other'}]
    df = pd.DataFrame(json_string,  columns=['name','full_name'])
    df2 = pd.DataFrame(json_string2, columns=['name','full_name'])
    assert df.size == 2
    assert pd.concat([df, df2], ignore_index=True).empty == False
