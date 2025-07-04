import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 1234))
s.listen(10)

c, addr = s.accept()
print("CONNECTED:", addr)

start = time.time()
total = 0
while True:
    data = c.recv(1024)
    if not data:
        print('disconnected')
        break
    print(f"Received: {len(data)} bytes")

    total += len(data)

    now = time.time()
    interval = now - start
    if interval >= 1.0:
        speed = total / interval
        print(f'Speed: {speed / 1024} KB/s')

        total = 0
        start = now


# c.shutdown(socket.SHUT_RDWR)
c.close()

s.close()

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#     s.bind((HOST, PORT))
#     s.listen(1)
#     conn, addr = s.accept()
#     with conn:
#         print('Connected by', addr)
#         while True:
#             data = conn.recv(1024)
#             if not data:
#                 break
#                 conn.sendall(data)