import pytest
import pandas as pd
import requests

def test_http_get_repos():
    r = requests.get('https://api.github.com/orgs/lodash/repos')
    assert r.status_code == 200
    assert r.json()

def test_http_get_pr():
    r = requests.get('https://api.github.com/repos/lodash/lodash/pulls?state=all')
    assert r.status_code == 200
    assert r.json()

def test_pandas_load():
    json_string = [{'id': 3955647, 'name': 'lodash', 'full_name': 'lodash/lodash'}]
    df = pd.DataFrame(json_string,  columns=['name','full_name'])
    assert df.size == 2
