# Python github API V3

Python script to get all pull requests from the lodash organization.  This will include getting pull requests from all repositories under the lodash org.

This uses Basic Authentication for ease of use as a starter to learn the API.

### Libraries:
- pandas [http://pandas.pydata.org/]
- requests [http://docs.python-requests.org/en/master/]
- pytest [https://docs.pytest.org/en/latest/contents.html]

### Requirements:
- python v3.6
- pip3

### Sample Usage:
- Run unit tests
```python
>> pytest
py_test.py ...
=====3 Tests======
```

- Modify app.py and replace '<user>' and '<password>' with real git authenticated user/password
```python
user_name = 'johndoe' # CHANGE ME!
user_pwd = '123abc' # CHANGE ME!
```

- Run app.py
