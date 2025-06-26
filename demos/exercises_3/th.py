import threading
import time
import sys

# i = 0
# while True:
#     if i != 0:
#         time.sleep(0.1)
#
#     if i % 5 == 0:
#         print('----------')
#         sys.stdout.flush()
#
#     if i % 3 == 0:
#         print('@@@@@@@')
#         sys.stdout.flush()
#
#     i += 1

def print_ats():
    while True:
        print('@@@@@@@@')
        sys.stdout.flush()
        time.sleep(0.3)

th =threading.Thread(target=print_ats)
th.start()

while True:
    print('---------')
    sys.stdout.flush()
    time.sleep(0.5)