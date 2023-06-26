import requests
import pprint

data = requests.request('GET', 'http://127.0.0.1:8000/api/ukraineApi/')

pprint.pprint(data.json())