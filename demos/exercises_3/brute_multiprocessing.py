import hashlib
import time
import multiprocessing

user = 'pete'
passhash = '394628d6ba9d6a9db0492a8be9fc81534a558392618bc078d9440ff412ba7801'.lower()

PROCESS_COUNT = 2


def brute(passhash, p_nr, total_count, the_end, v_start):
    i = p_nr
    print(f'Process {p_nr} started...')
    while not the_end.value:
        h = hashlib.sha256(str(i).encode()).hexdigest()
        if h == passhash:
            print(f'found pass: {i} in {time.time() - v_start} sec.')

            with the_end.get_lock():
                the_end.value += 1

            break
        i += total_count
    print(f'Process {i} ended.')


def main():
    v_start = time.time()
    the_end = multiprocessing.Value('i', 0)
    pool = []

    for i in range(PROCESS_COUNT):
        p = multiprocessing.Process(target=brute, args=(passhash, i, PROCESS_COUNT, the_end, v_start))
        pool.append(p)
        p.start()
    print('All processes have started')

    for p in pool:
        p.join()

    print('Ending main process')


if __name__ == '__main__':
    main()
