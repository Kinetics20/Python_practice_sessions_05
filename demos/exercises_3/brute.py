import hashlib
import time

user = 'pete'
passhash = '150a6354c2e1d1d9fd16d050707b0427c9689f3c1b10e98777eee09a8872064b'.lower()

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

