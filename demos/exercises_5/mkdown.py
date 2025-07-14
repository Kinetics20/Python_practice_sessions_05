import re

with open('ex.md', 'r', encoding='utf-8') as f:
    md = f.read()


def escape(text):
    text = text.replace('&', '&amp;')
    text = text.replace('<', '&lt;')
    return text


def escape_attr(text):
    text = text.replace('&', '&amp;')
    text = text.replace('<', '&lt;')
    text = text.replace('>', '&gt;')
    text = text.replace('\'', '&quot;')
    text = text.replace("'", '&#39;')
    return text


def escape_a(match_obj):
    url = match_obj.group(2)
    text = match_obj.group(1)
    return f"<a href='{escape_attr(url)}'>{text}</a>"


def heading(ln):
    level = 0
    while level < len(ln):
        if ln[level] == '#':
            level += 1
            continue
        break
    ln = ln[level:].strip()
    return (f'<h{level}>{escape(ln)}</h{level}>')


def end_list():
    print('</ul>')


def end_p():
    print('</p>')


def change_state(new_st, new_st_exit=None):
    global st
    global st_exit
    if st_exit is not None:
        st_exit()
    st = new_st
    st_exit = new_st_exit


def split_replace(text, marker, start_tag, end_tag):
    output = []
    for i, segment in enumerate(text.split(marker)):
        if i % 2 == 0:
            output.append(segment)
        else:
            output.append(start_tag + segment + end_tag)
    return ''.join(output)


def format(text):
    text = split_replace(text, '**', '<b>', '</b>')
    text = split_replace(text, '*', '<i>', '</i>')
    text = split_replace(text, '~~', '<del>', '</del>')

    text = re.sub(r'\[([^]]+)\]\(([^)]*)\)', escape_a, text)

    return text


ST_NONE = 'none'
ST_PARAGRAPH = 'p'
ST_LIST = 'list'
st = ST_NONE
st_exit = None

lines = md.splitlines()
for ln in lines:

    if ln.startswith('#'):
        change_state(ST_NONE)
        print(heading(ln))
        continue

    if ln.startswith('  *'):
        if st != ST_LIST:
            change_state(ST_LIST, end_list)
            print('<ul>')

        ln = ln[3:].strip()
        print(f'<li>{format(ln)}</li>')
        continue

    if ln.strip() == '':
        change_state(ST_PARAGRAPH, end_p)
        print('<p>')
        continue

    print(format(ln))

change_state(ST_NONE)
