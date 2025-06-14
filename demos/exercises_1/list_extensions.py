import os
from typing import Set

path = "/home/lipov/projects/Python_practice_sessions_05/demos"
extensions: Set[str] = set()

for dirpath, dirnames, filenames in os.walk(path):
    for filename in filenames:
        _, ext = os.path.splitext(filename)
        if ext:
            extensions.add(ext)

for ext in sorted(extensions):
    print(ext)

with open("output_extensions.txt", "w") as f:
    for ext in sorted(extensions):
        f.write(ext + "\n")
