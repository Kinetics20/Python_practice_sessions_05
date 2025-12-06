import time
import os
import sys

def flash_screen(times=6, interval=0.3):
    for _ in range(times):
        sys.stdout.write('\033[?5h')
        sys.stdout.flush()
        time.sleep(interval)
        sys.stdout.write('\033[?5l')
        sys.stdout.flush()
        time.sleep(interval)

def format_time(seconds):
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return f'{h:02}:{m:02}:{s:02}'

def main():
    try:
        t = int(input('Enter alarm time in seconds: '))
        print(f'Alarm set for {t} seconds.')
        for remaining in range(t, -1, -1):
            sys.stdout.write(f'\rTime left: {format_time(remaining)}')
            sys.stdout.flush()

            if remaining == 0:
                break
            time.sleep(1)
        print()
        flash_screen()
        print('Time is up!')
    except KeyboardInterrupt:
        print('\nCanceled.')
    except ValueError:
        print('Invalid input.')

if __name__ == '__main__':
    main()