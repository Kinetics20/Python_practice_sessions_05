import os

KEYWORDS = {
    "C/C++": ["#include", "#define"],
    "PHP": ["<?php"],
    "Python": ["def ", "import "],
    "HTML": ["<html", "<body", "<div"]
}

base_path = "/home/lipov/projects/Python_practice_sessions_05/demos"

detected_languages = {}

for dirpath, _, filenames in os.walk(base_path):
    for filename in filenames:
        file_path = os.path.join(dirpath, filename)

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
        except (UnicodeDecodeError, FileNotFoundError):
            continue

        found_languages = set()

        for language, keywords in KEYWORDS.items():
            for kw in keywords:
                if kw in content:
                    found_languages.add(language)
                    break

        if found_languages:
            detected_languages[file_path] = found_languages

for path, langs in detected_languages.items():
    print(f"{path}: {', '.join(sorted(langs))}")
