import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            print(f"Modified: {event.src_path}")

    def on_created(self, event):
        if not event.is_directory:
            print(f"Created: {event.src_path}")

    def on_deleted(self, event):
        if not event.is_directory:
            print(f"Deleted: {event.src_path}")


def start_watchdog(path: str):
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=path, recursive=True)
    observer.start()
    print(f"Watching directory: {path}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    folder_to_watch = "/home/lipov/projects/Python_practice_sessions_05/demos"
    start_watchdog(folder_to_watch)
