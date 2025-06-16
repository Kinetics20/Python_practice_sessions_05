import os
from pathlib import Path

LANGUAGES = {
    ".py": "Python",
    ".js": "JavaScript",
    ".html": "HTML",
    ".css": "CSS",
    ".java": "Java",
    ".cpp": "C++",
    ".c": "C",
    ".sh": "Shell",
    ".rb": "Ruby",
}

SOURCE_DIR = Path("/home/lipov/projects/Python_practice_sessions_05/demos")

report_data = []

for file_path in SOURCE_DIR.rglob("*.*"):
    ext = file_path.suffix
    language = LANGUAGES.get(ext.lower(), "Unknown")

    if language == "Unknown":
        continue

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            non_empty_lines = [line for line in lines if line.strip()]
            line_count = len(non_empty_lines)
    except Exception as e:
        print(f"Skipping {file_path} due to error: {e}")
        continue

    report_data.append((file_path.relative_to(SOURCE_DIR), language, line_count))

html_content = """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Source Code Report</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; }}
        table {{ border-collapse: collapse; width: 80%; }}
        th, td {{ border: 1px solid #ccc; padding: 8px; text-align: left; }}
        th {{ background-color: #f4f4f4; }}
    </style>
</head>
<body>
    <h1>Source Code Report</h1>
    <p>Scanned directory: <code>{directory}</code></p>
    <table>
        <tr><th>File Name</th><th>Language</th><th>Lines of Code</th></tr>
""".format(directory=SOURCE_DIR)

for file_name, language, line_count in sorted(report_data):
    html_content += f"<tr><td>{file_name}</td><td>{language}</td><td>{line_count}</td></tr>\n"

html_content += """
    </table>
</body>
</html>
"""

output_file = "source_report.html"
with open(output_file, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"HTML report saved as '{output_file}'")
