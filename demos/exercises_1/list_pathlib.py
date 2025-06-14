from pathlib import Path

path = Path("/home/lipov/projects/Python_practice_sessions_05/demos")

all_files = [str(p) for p in path.rglob('*')]

for i in sorted(all_files):
    print(i)

with open("output_B.txt", "w") as f:
    for line in sorted(all_files):
        f.write(line + "\n")
