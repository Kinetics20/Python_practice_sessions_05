from collections import Counter
from urllib.request import urlopen
import re

# print(issubclass(Counter, dict))

# letters = 'John has a cats and dogs'

# letter_counter = Counter(letters)
# # print(letter_counter[' '])
#
# with urlopen('https://wolnelektury.pl/media/book/txt/pan-tadeusz.txt') as response:
#     text = response.read().decode('utf-8')
#     text = [word for word in re.findall(r'\b\w+\b', text) if len(word) > 5]
#     counter = Counter(text)
#     print(counter.most_common(10))

letters = ['a', 'b', 'c', 'a', 'c', 'a', 'b', 'c']
letter_counter = Counter(letters)
print(letter_counter)
letter_counter.update('aa')
letter_counter.update(['c', 'c'])

letter_counter.update({'b': 5})
letter_counter.update(a=2, b=2, c=2)

letter_counter.subtract(a=7, b=6, c=8)
letter_counter.clear()
print(letter_counter)

# -----+-----
c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2)

print(c1 + c2)
print(c1 - c2)

print(c1 & c2)
print(c1 | c2)
print(+c1)
print(-Counter(a=1, b=-1))

print(list(c1.elements()))
print(c1.most_common())
print(c1.total())