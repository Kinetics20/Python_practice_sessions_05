import socket
import time
import hashlib

FRAG_SZ = 1024 * 1024 # 1MB

def recvall(s, size):
    total = 0
    data = []

    while True:
        part_data = s.recv(size - total)
        if not part_data:
            return None

        total += len(part_data)
        data.append(part_data)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 1234))
s.listen(10)

c, addr = s.accept()
print("CONNECTED:", addr)

with open('bigfile', 'rb') as f:
    while True:
        fdata = f.read(FRAG_SZ)
        h = hashlib.sha256(fdata).digest()

        c.sendall(h)


c.close()

s.close()
