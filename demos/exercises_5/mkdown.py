with open('ex.md', 'r', encoding='utf-8') as f:
    md = f.read()

# def heading(level, ln):
#     ln = ln[level:].strip()
#     return (f'<h{level}>{ln}</h{level}>')

def escape(text):
    text = text.replace('&', '&amp;')
    text = text.replace('<', '&lt;')
    return text

def heading(ln):
    level = 0
    while level < len(ln):
        if ln[level] == '#':
            level += 1
            continue
        break
    ln = ln[level:].strip()
    return (f'<h{level}>{escape(ln)}</h{level}>')

lines = md.splitlines()
for ln in lines:

    if ln.startswith('#'):
        print(heading(ln))
        continue


    print('not handled:', ln)