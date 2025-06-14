import sys
from pathlib import Path

if len(sys.argv) != 2:
    sys.exit("Usage: python count_lines.py <file_to_file.py>")

file_path = Path(sys.argv[1])

if not file_path.exists() or not file_path.is_file():
    sys.exit("Entered path doesn't exist or does not a file!")


with file_path.open("r", encoding="utf-8") as f:
    lines = f.readlines()


total_lines = len(lines)

non_empty_lines = [line for line in lines if line.strip()]
count_non_empty = len(non_empty_lines)

code_lines = [line for line in non_empty_lines if not line.strip().startswith("#")]
count_code_lines = len(code_lines)

print(f"A. Amount of all lines: {total_lines}")
print(f"B. Amount of all lines without empty lines: {count_non_empty}")
print(f"C. Amount of all lines without empty lines and comments: {count_code_lines}")
