import multiprocessing
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

if __name__ == "__main__":
    processes = [
        multiprocessing.Process(target=print_ala),
        multiprocessing.Process(target=print_ma),
        multiprocessing.Process(target=print_kota),
    ]

    for p in processes:
        p.start()

    for p in processes:
        p.join()
