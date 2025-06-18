import json

from fastapi import FastAPI
app = FastAPI()

@app.post('/api/add-numbers')
def add_numbers(api_key: str, numbers: list[int]) -> dict:
    if api_key != 'pass':
        return {
            'result': None,
            'error' : True,
            'error_msg': 'access denied'
        }
    acc = 0
    for n in numbers:
        acc += n
    return {
        'result': acc,
        'error': False,
        'error_msg': None
    }
# r = add_numbers([1, 2, 3, 4])
# r_json = json.dumps(r)
# print(r_json)