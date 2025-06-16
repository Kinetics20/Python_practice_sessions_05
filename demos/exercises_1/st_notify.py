import os
from inotify_simple import INotify, flags

def start_inotify_watch(path: str):
    inotify = INotify()
    watch_flags = flags.CREATE | flags.MODIFY | flags.DELETE
    inotify.add_watch(path, watch_flags)

    print(f"Watching directory: {path}")

    try:
        while True:
            for event in inotify.read():
                name = event.name
                full_path = os.path.join(path, name)

                if event.mask & flags.CREATE:
                    print(f"Created: {full_path}")
                if event.mask & flags.MODIFY:
                    print(f"Modified: {full_path}")
                if event.mask & flags.DELETE:
                    print(f"Deleted: {full_path}")
    except KeyboardInterrupt:
        print("\nStopped watching.")

if __name__ == "__main__":
    folder_to_watch = "/home/lipov/projects/Python_practice_sessions_05/demos/exercises_1"
    start_inotify_watch(folder_to_watch)
