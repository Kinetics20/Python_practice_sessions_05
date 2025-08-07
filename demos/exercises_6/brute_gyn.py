import requests
import time

for i in range(0, 120):
    addr = f'https://gynvael.coldwind.pl/?lang=pl&id={i}'
    r = requests.get(addr)
    if '<!DOCTYPE html PUBLIC' in r.text:
        print(addr)
    time.sleep(.2)
