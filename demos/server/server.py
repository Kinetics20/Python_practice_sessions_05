import json

from fastapi import FastAPI
app = FastAPI()

@app.post('/api/add-numbers')
def add_numbers(numbers):
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