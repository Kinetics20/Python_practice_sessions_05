import time

next_ala = time.time()
next_ma = time.time()
next_kota = time.time()

while True:
    now = time.time()

    if now >= next_ala:
        print("ALA")
        next_ala += 0.1

    if now >= next_ma:
        print("MA")
        next_ma += 0.35

    if now >= next_kota:
        print("KOTA")
        next_kota += 0.66

    time.sleep(0.01)
