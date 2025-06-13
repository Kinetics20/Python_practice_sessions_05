import os
import time
import json
from pprint import pprint


# DIR_TO_SCAN = '/home/lipov/projects/Python_practice_sessions_05/demos/random-stuff'
DIR_TO_SCAN = '/home/lipov/projects'

EXT_TO_LANG = {
    '.c': 'C/C++',
    '.cc': 'C/C++',
    '.h': 'C/C++',
    '.hpp': 'C/C++',
    '.cpp': 'C/C++',
    '.ino': 'C/C++',
    '.py': 'Python',
    '.pyw': 'Python',
    '.html': 'HTML',
    '.md': 'Markdown',
    '.htm': 'HTML',
    '.css': 'CSS',
    '.js': 'JavaScript',
    '.bat': 'Batch',
    '.pl': 'Perl',
    '.php': 'PHP',
    '.sh': 'Bash',
    '.ipynb': 'Jupyter Notebook',

}

def count_lines(fname):
    with open(fname, 'rb') as f:
        counter = 0
        for ln in f.readlines():
            if not ln.strip():
                continue
            counter += 1
        return counter


def get_stats(stats):
    langs = {}

    total_loc = 0
    total_file_count = 0

    for path, dirs, files in os.walk(DIR_TO_SCAN):
        path_elements = path.split(os.path.sep)

        if any([x.startswith('.') for x in path_elements]):
            continue


        for file in files:
            full_fname = f'{path}/{file}'
            _, ext = os.path.splitext(file)

            ext = ext.lower()

            lang = EXT_TO_LANG.get(ext)
            if lang is None:
                continue

            total_file_count += 1

            loc = count_lines(full_fname)
            total_loc += loc

            if lang in langs:
                langs[lang] += loc
            else:
                langs[lang] = loc


    stats['langs'] = langs
    stats['totalLOC'] = total_loc
    stats['totalFiles'] = total_file_count

BAR_WIDTH = 40
def show_stats_for(label, locs):
    max_loc = max(locs)

    i = 1
    while i < max_loc:
        i *= 2

    print(f'\x1b[1;37m{label}\x1b[m (scale: 1/{i})')

    for j, loc in enumerate(locs):
        if len(locs) ==1:
            g = 255
        else:
            g = 55 + int((j / (len(locs) - 1)) * 200)
        color = f'\x1b[38;2;0;{g};0m'

        bar_size = int((loc / i) * BAR_WIDTH)
        bar = '\u2593' * bar_size
        print(f'\x1b[1;31m{loc:5}\x1b[m {color}{bar}\x1b[m')
    print()

def show_stats(stats_in_time):
    print('\x1b[1;1H\x1b[2J', end='')

    for lang in ['Bash', 'Python', 'HTML', 'Jupyter Notebook', 'JavaScript']:
        locs = []
        for stats in stats_in_time:
            locs.append(stats['langs'].get(lang, 0))

        show_stats_for(lang, locs)


    pass



def main():
    stats_in_time = []

    # try:
    #     with open('stats.json') as f:
    #         stats_in_time = json.load(f)
    # except FileNotFoundError:
    #     pass

    try:
        while True:
            stats = {
                'totalLoC': None,
                'langs': {
                    # Python
                }
            }

            get_stats(stats)
            stats_in_time.append(stats)

            show_stats(stats_in_time[-6:])
            time.sleep(1)  # Seconds.
    except KeyboardInterrupt:
        pass

    with open('stats.json', 'w') as f:
        json.dump(stats_in_time, f)


if __name__ == '__main__':
    main()
