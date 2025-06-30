import threading
import time

def print_ala():
    while True:
        print("ALA")
        time.sleep(0.1)

def print_ma():
    while True:
        print("MA")
        time.sleep(0.35)

def print_kota():
    while True:
        print("KOTA")
        time.sleep(0.66)


threads = [
    threading.Thread(target=print_ala),
    threading.Thread(target=print_ma),
    threading.Thread(target=print_kota),
]

for t in threads:
    t.daemon = True
    t.start()


while True:
    time.sleep(1)
