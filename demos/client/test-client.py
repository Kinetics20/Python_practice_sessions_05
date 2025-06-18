import requests
import json
from pprint import pprint


def add_numbers(numbers):
    x = json.dumps(numbers)
    r = requests.post(
        'http://127.0.0.1:8000/api/add-numbers?api_key=pass', data=x)


    res = r.json()
    return res['result']

print(add_numbers([1, 2, 3]))
print(add_numbers([40, 2]))