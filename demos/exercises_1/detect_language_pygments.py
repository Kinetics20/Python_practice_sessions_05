import os
import sys
from typing import Optional
from pygments.lexers import guess_lexer
from pygments.util import ClassNotFound
from multiprocessing import Process, Queue
from multiprocessing.queues import Queue as QueueType
from tqdm import tqdm

base_path = "/home/lipov/projects/Python_practice_sessions_05/demos"


def detect_in_process(content: str, queue: QueueType):
    try:
        lexer = guess_lexer(content)
        queue.put(lexer.__class__.__name__)
    except ClassNotFound:
        queue.put(None)
    except (ValueError, TypeError):
        queue.put(None)


def detect_language_with_pygments(filepath: str, timeout: int = 2) -> Optional[str]:
    try:
        if os.path.getsize(filepath) > 1_000_000:
            return None

        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()

        if not content.strip():
            return None

        queue: QueueType = Queue()
        process = Process(target=detect_in_process, args=(content, queue))
        process.start()
        process.join(timeout)

        if process.is_alive():
            process.terminate()
            process.join()
            return None

        return queue.get()

    except (UnicodeDecodeError, FileNotFoundError):
        return None
    except Exception as e:
        print(f"Error during file {filepath}: {e}", file=sys.stderr)
        return None


results = {}
all_files = []

for dirpath, _, filenames in os.walk(base_path):
    for fname in filenames:
        full_path = os.path.join(dirpath, fname)
        all_files.append(full_path)

for full_path in tqdm(all_files, desc="Processing files"):
    lang = detect_language_with_pygments(full_path)
    if lang:
        results[full_path] = lang

for path, lang in results.items():
    print(f"{path}: {lang}")
