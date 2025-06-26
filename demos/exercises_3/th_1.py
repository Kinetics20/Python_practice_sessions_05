import threading
import time
import sys

a = 1
b = 2
c = 3

def calc_10():
    global a
    global b
    global c

    a = 4
    time.sleep(0)
    b = 6
    time.sleep(0)
    c = a + b
    assert  c == 10, f'THREAD {a} {b} {c}'

def calc_10b():
    global a
    global b
    global c

    a = 3
    time.sleep(0)
    b = 7
    time.sleep(0)
    c = a + b
    assert  c == 10, f'THREAD_B {a} {b} {c}'

def calc_10c():
    global a
    global b
    global c

    a = 2
    time.sleep(0)
    b = 8
    time.sleep(0)
    c = a + b
    assert  c == 10, f'THREAD_C {a} {b} {c}'


th =threading.Thread(target=calc_10)
th.start()

th =threading.Thread(target=calc_10b)
th.start()

th =threading.Thread(target=calc_10c)
th.start()



while True:
    a = 5
    time.sleep(0)
    b = 5
    time.sleep(0)
    c = a + b
    assert  c == 10, f'MAIN {a} {b} {c}'
