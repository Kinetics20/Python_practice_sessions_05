import os
import time

DIR_TO_SCAN = '/home/lipov/projects/Python_practice_sessions_05/demos/random-stuff'

def get_stats(stats):
    for path, dirs, files in os.walk(DIR_TO_SCAN):
        print(files)


def show_stats(stats):
    pass

def main():
    stats = {
        'totalLoC': None,
        'langs': {
            # Python
        }
    }

    while True:
        get_stats(stats)
        show_stats(stats)
        time.sleep(1.5) # Seconds.




if __name__ == '__main__':
    main()