import re


def solution(full_text: str, search_text: str) -> int:
    if search_text == "":
        return len(full_text) + 1

    return sum(1 for _ in re.finditer(re.escape(search_text), full_text))


def solution_2(full_text, search_text):
    return full_text.count(search_text)


def solution_3(f, s):
    return f.count(s)


def solution_4(data, index, default):
    return data[index] if -len(data) <= index < len(data) else default


class Person:
    def __init__(self, name):
        self.name = name

    def greet(self, your_name):
        return f"Hello {your_name}, my name is {self.name}"