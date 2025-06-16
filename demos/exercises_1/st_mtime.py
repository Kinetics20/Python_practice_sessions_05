import os
import time


def get_all_files_with_mtime(root_dir: str) -> dict[str, float]:
    """return dictionary with a full path to file as a key and modification time as a value."""
    mtime_map = {}
    for dirpath, _, filenames in os.walk(root_dir):
        for fname in filenames:
            full_path = os.path.join(dirpath, fname)
            try:
                mtime_map[full_path] = os.stat(full_path).st_mtime
            except FileNotFoundError:
                continue
    return mtime_map


def monitor_directory(path: str, interval: int = 1) -> None:
    print(f"Monitoring changes in: {path}")
    cache = get_all_files_with_mtime(path)

    while True:
        time.sleep(interval)
        current = get_all_files_with_mtime(path)

        for file, mtime in current.items():
            if file not in cache or mtime != cache[file]:
                print(f"changed: {file}")

        cache = current


if __name__ == "__main__":
    folder_to_watch = "/home/lipov/projects/Python_practice_sessions_05/demos"
    monitor_directory(folder_to_watch)
