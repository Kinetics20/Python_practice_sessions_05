import hashlib
import threading
import time

user = 'pete'
passhash = '394628d6ba9d6a9db0492a8be9fc81534a558392618bc078d9440ff412ba7801'.lower()

THREAD_COUNT = 6

v_start = time.time()
the_end = threading.Event()


def brute(passhash, i, total_count):
    while not the_end.is_set():
        h = hashlib.sha256(str(i).encode()).hexdigest()
        if h == passhash:
            print(f'found pass: {i} in {time.time() - v_start} sec.')
            the_end.set()
            break
        i += total_count


threads = []
for i in range(THREAD_COUNT):
    th = threading.Thread(target=brute, args=(passhash, i, THREAD_COUNT), daemon=True)
    threads.append(th)
    th.start()

for th in threads:
    th.join()

"""users = {'pete': '63b347973bb99fed9277b33cb4646b205e9a31331acfa574add3d2351f445e43'}

sent_username = 'pete'
sent_password = '1234567'
h = hashlib.sha256(sent_password.encode()).hexdigest()

if hashlib.sha256(sent_password.encode()).hexdigest() == users[sent_username]:
    print('successful logging')
else:
    print('failed logging')"""

# echo -n '1234567' |sha256sum
# cat /proc/cpuinfo
