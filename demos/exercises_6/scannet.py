import socket
from multiprocessing.pool import ThreadPool
import threading
import time

TIMEOUT = 1
THREAD_COUNT = 100
PORT = 80

NET_MASK = 24
NET_ADDR = (192, 168, 0, 172)

the_end = threading.Event()
counter = 0
counter_guard = threading.Lock()



def scan(host):
    global counter

    with counter_guard:
        counter += 1



    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.settimeout(TIMEOUT)
            s.connect((host, PORT))
        except ConnectionRefusedError:
            return None
        except OSError:
            return None
        s.shutdown(socket.SHUT_RDWR)
    return port

def show_progress(p):
    w = int(p * 60)
    print('=' * w, end='\r', flush=True)

def show_progress_worker():
    while not the_end.is_set():
        show_progress(counter / 65535)
        time.sleep(1 / 3)
    print(' ' * 60)

th_progress = threading.Thread(target=show_progress_worker)
th_progress.start()

with ThreadPool(100) as pool:
    results = pool.map(scan, range(1, 65536))

the_end.set()
th_progress.join()

for r in results:
    if r is not None:
        print(r, 'port is open')
