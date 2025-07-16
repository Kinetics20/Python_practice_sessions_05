import socket
import threading

TIMEOUT = 1
HOST = '127.0.0.1'
# HOST = '192.168.2.253'

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




for port in range(1, 65536):
    r = scan(port)
    if r is not None:
        print(port, 'is open')