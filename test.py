import requests
from pprint import pprint

data = requests.request('GET', 'http://127.0.0.1:8000/api/ukraineApi/')

pprint(data.json())