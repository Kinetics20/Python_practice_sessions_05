import hashlib
import time

user = 'pete'
passhash = 'd7c929f4207e3b5201e3f719c5822daf1ee85cc8ea5da2ef46d2b0c24a99b090'.lower()

i = 0
last_i = 0
start = time.time()
while True:
    h = hashlib.sha256(str(i).encode()).hexdigest()
    if h == passhash:
        print(f'found pass: {i}')
        break

    now = time.time()
    diff = now - start
    if diff >= 1.0:
        start = now
        print(f'Tried {i - last_i}')
        last_i = i

    i += 1


"""users = {'pete': '63b347973bb99fed9277b33cb4646b205e9a31331acfa574add3d2351f445e43'}

sent_username = 'pete'
sent_password = '1234567'
h = hashlib.sha256(sent_password.encode()).hexdigest()

if hashlib.sha256(sent_password.encode()).hexdigest() == users[sent_username]:
    print('successful logging')
else:
    print('failed logging')"""

