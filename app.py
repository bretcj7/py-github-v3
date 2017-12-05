import json
import numpy as np
import pandas as pd
import requests

API_KEY = 'a4d03a857807cb8fc26a3700e8f0a4daf393ba1d'

r = requests.get('https://api.github.com/orgs/lodash/repos')
print (r.json()[0])
