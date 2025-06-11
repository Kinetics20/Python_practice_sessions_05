import os
import time

DIR_TO_SCAN = '/home/lipov/projects/Python_practice_sessions_05/demos/random-stuff'

EXT_TO_LANG = {
    '.c': 'C/C++',
    '.cc': 'C/C++',
    '.h': 'C/C++',
    '.hpp': 'C/C++',
    '.cpp': 'C/C++',
    '.py': 'Python',
    '.pyw': 'Python',
    '.html': 'HTML',
    '.htm': 'HTML',
    '.css': 'CSS',
    '.js': 'JavaScript',
    '.bat': 'Batch',
    '.pl': 'Perl',
    '.php': 'PHP',

}


def get_stats(stats):
    for path, dirs, files in os.walk(DIR_TO_SCAN):
        for file in files:
            full_fname = f'{path}/{file}'
        _, ext = os.path.splitext(file)

        ext = ext.lower()

        lang = EXT_TO_LANG.get(ext)
        if lang is None:
            print(ext)
            continue


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
        time.sleep(1.5)  # Seconds.


if __name__ == '__main__':
    main()
