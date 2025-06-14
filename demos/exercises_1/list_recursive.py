import os

def list_files_recursively(directory):
    entries = []
    for entry in os.listdir(directory):
        full_path = os.path.join(directory, entry)
        entries.append(full_path)
        if os.path.isdir(full_path):
            entries.extend(list_files_recursively(full_path))
    return entries

path = "/home/lipov/projects/Python_practice_sessions_05/demos"

all_files = list_files_recursively(path)

for i in sorted(all_files):
    print(i)

with open("output_C.txt", "w") as f:
    for line in sorted(all_files):
        f.write(line + "\n")
