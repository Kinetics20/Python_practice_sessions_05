import socket
from multiprocessing.pool import ThreadPool
import threading
import time

TIMEOUT = 1
THREAD_COUNT = 100
PORT = 80

NET_MASK = 24
NET_ADDR = (192, 168, 0, 172)


def calc_start_end_ip(addr, mask):
    addr = (
            (addr[0] << 24) |
            (addr[1] << 16) |
            (addr[2] << 8) |
            (addr[3] << 0)
    )

    mask32 = ((1 << mask) - 1) << (32 - mask)

    start = addr & mask32
    stop = start | ((1 << (32 - mask)) - 1)

    return start, stop


host_list = []


def convert_addr32_to_str(addr32):
    a = (addr32 >> 24) & 0xff
    b = (addr32 >> 16) & 0xff
    c = (addr32 >> 8) & 0xff
    d = addr32 & 0xff

    return f'{a}:{b}:{c}:{d}'


start, stop = calc_start_end_ip(NET_ADDR, NET_MASK)
for addr32 in range(start, stop + 1):
    host_list.append(convert_addr32_to_str(addr32))

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
    return host


def show_progress(p):
    w = int(p * 60)
    print('=' * w, end='\r', flush=True)


def show_progress_worker():
    while not the_end.is_set():
        show_progress(counter / len(host_list))
        time.sleep(1 / 3)
    print(' ' * 60)


th_progress = threading.Thread(target=show_progress_worker)
th_progress.start()

with ThreadPool(100) as pool:
    results = pool.map(scan, host_list)

the_end.set()
th_progress.join()

for r in results:
    if r is not None:
        print(f'{r} has a port {PORT} open')
