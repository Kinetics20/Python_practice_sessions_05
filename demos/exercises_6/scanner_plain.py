import socket
import threading
import queue

TIMEOUT = 1
THREAD_COUNT = 100
HOST = '127.0.0.1'


def scan(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.settimeout(TIMEOUT)
            s.connect((HOST, port))
        except ConnectionRefusedError:
            return None
        except OSError:
            return None
        s.shutdown(socket.SHUT_RDWR)
    return port


def thread_worker(jobs, results):
    while True:
        try:
            port = jobs.get(block=False)
        except queue.Empty:
            return
        results[port] = scan(port)


results = [None] * 65536
threads = []
jobs = queue.Queue()

for port in range(1, 65536):
    jobs.put(port)

for _ in range(THREAD_COUNT):
    th = threading.Thread(
        target=thread_worker,
        args=(jobs, results)
    )
    th.start()
    threads.append(th)

for th in threads:
    th.join()

for r in results:
    if r is not None:
        print(r, 'port is open')
