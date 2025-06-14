import os
import re

REGEX_PATTERNS = {
    "Python": [
        r"^def\s+\w+\(.*\):",
        r"^import\s+\w+",
        r"^from\s+\w+\s+import"
    ],
    "C/C++": [
        r"^#include\s+<\w+\.h>",
        r"^#define\s+\w+",
        r"int\s+main\s*\(.*\)"
    ],
    "HTML": [
        r"<html.*?>",
        r"<body.*?>",
        r"<div.*?>"
    ],
    "PHP": [
        r"<\?php",
        r"echo\s+.*?;",
        r"\$[a-zA-Z_]\w*"
    ]
}

base_path = "/home/lipov/projects/Python_practice_sessions_05/demos"


def detect_languages_in_file(filepath: str) -> list[str]:
    found_languages = set()

    try:
        with open(filepath, "r", encoding="utf-8") as file:
            for line in file:
                stripped = line.strip()
                for lang, patterns in REGEX_PATTERNS.items():
                    if lang in found_languages:
                        continue

                    for pattern in patterns:
                        if re.search(pattern, stripped):
                            found_languages.add(lang)
                            break
    except (UnicodeDecodeError, FileNotFoundError):
        pass

    return list(found_languages)


detected = {}

for dirpath, _, filenames in os.walk(base_path):
    for fname in filenames:
        full_path = os.path.join(dirpath, fname)
        langs = detect_languages_in_file(full_path)
        if langs:
            detected[full_path] = langs

for path, langs in detected.items():
    print(f"{path}: {', '.join(sorted(langs))}")
