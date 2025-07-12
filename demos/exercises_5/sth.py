import re

tmpl = 'John has a {animal} and the cat has a {name}. {xyz}'

replacements = {
    'animal': 'cat',
    'name': 'John'
}

# txt = tmpl.replace('{animal}', 'cat').replace('{name}', 'John')
# print(txt)

# txt = tmpl
# for k, v in replacements.items():
#     txt = txt.replace('{' + k + '}', v)
#
# print(txt)

def get_from_repl(matchobj):
    k = matchobj.group(1)
    return replacements.get(k, '?unknown?')

# print(re.sub(r'{([a-z]+)}', get_from_repl, tmpl))

# output = []
# segments = tmpl.split('{')
# for segment in segments:
#     print('No } in segment:', segment)
#     if '}' not in segment:
#         output.append(segment)
#         continue
#     k, text = segment.split('}', 1)
#     print(f'key: {k}, text: {text}')
#     output.append(replacements.get(k, '?unknown?'))
#     output.append(text)

# print(''.join(output))

ST_START = 'start'
ST_TEXT = 'text'
ST_TAG = 'tag'


st = ST_START
i = 0
output = ''


while i < len(tmpl):
    ch = tmpl[i]
    i += 1
    print(st, ch)

    if st == ST_START:
        if ch == '{':
            st = ST_TAG
            k = ''
            continue
        output += ch
        st = ST_TEXT
        continue

    if st == ST_TEXT:
        if ch == '{':
            st = ST_TAG
            k = ''
            continue
        output += ch
        continue

    if st == ST_TEXT:
        if ch == '}':
            v = replacements.get(k, '?unknown?')
            output += v
            st = ST_TEXT
            continue
        k += ch
        continue
    print(output)




