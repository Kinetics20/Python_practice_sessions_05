from markdown import markdown

with open('ex.md', 'r', encoding='utf-8') as f:
    md = f.read()

html = markdown(md)
print(html)