from functools import reduce


def title(text):
    return text.title()


def reverse(text):
    return text[::-1]


def add_dot(text):
    return text + '.'


sentence = 'ala ma kota i wszy'

result = reduce(lambda acc, cb: cb(acc), (title, reverse, title, add_dot), sentence)
print(result)