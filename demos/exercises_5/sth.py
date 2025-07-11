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

print(re.sub(r'{([a-z]+)}', get_from_repl, tmpl))