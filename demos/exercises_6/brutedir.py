import requests
import time

HOST = 'http://127.0.0.1:8000/docs'

with open('wordlist.txt') as f:
    for line in f:
        path = line.strip()
        r = requests.get(f'{HOST}/{path}')
        if r.status_code in range(200, 400):
            print(path, r.status_code)
        time.sleep(.2)
