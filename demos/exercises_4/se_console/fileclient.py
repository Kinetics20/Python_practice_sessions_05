import socket
import struct
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

        if total == size:
            return b''.join(data)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.0.172', 1234))

print("CONNECTED:")

frag_number = -1
with open('bigfile', 'r+b') as f:
    while True:
        frag_number += 1
        fdata = f.read(FRAG_SZ)
        if not fdata:
            break

        h_our = hashlib.sha256(fdata).digest()

        h_serv = recvall(s, 32)

        if h_serv is None:
            print('Server disconnected. Done')
            break

        if h_our == h_serv:
            print(f'Frag {frag_number} is good')
            s.sendall(b'OK')
            continue

        print(f'Frag {frag_number} is BAD: ',
              end='', flush=True)
        s.sendall(b'UP')

        frag_len = struct.unpack('<I', recvall(s, 4))[0]
        print(f'{frag_len // 1024} KB...',
              end='', flush=True)
        sdata = recvall(s, FRAG_SZ)

        print(f'{len(sdata) // 1024} KB downloaded... ',
              end='', flush=True)

        offset = f.tell()
        f.seek(offset - FRAG_SZ)
        f.write(sdata)
        print('patched!')

s.close()
