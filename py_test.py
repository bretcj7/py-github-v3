import pytest
import pandas as pd
import requests

# Test basic get request of org's repos
def test_http_get_repos():
    r = requests.get('https://api.github.com/orgs/lodash/repos')
    assert r.status_code == 200
    assert r.json()

# Test basic get request of pull requests for an org/repo
def test_http_get_pr():
    r = requests.get('https://api.github.com/repos/lodash/lodash/pulls?state=all')
    assert r.status_code == 200
    assert r.json()

# Test basic data store of json to dataframe
def test_pandas_load():
    json_string = [{'id': 3955647, 'name': 'lodash', 'full_name': 'lodash/lodash'}]
    df = pd.DataFrame(json_string,  columns=['name','full_name'])
    assert df.size == 2
