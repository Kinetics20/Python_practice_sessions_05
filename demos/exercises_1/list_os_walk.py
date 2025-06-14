import os


path = "/home/lipov/projects/Python_practice_sessions_05/demos"
all_files: list[str] = []

for dirpath, dirnames, filenames in os.walk(path):
    for name in dirnames + filenames:
        full_path = os.path.join(dirpath, name)
        all_files.append(full_path)

for i in sorted(all_files):
    print(i)

with open("output_A.txt", "w") as f:
    for line in sorted(all_files):
        f.write(line + "\n")
