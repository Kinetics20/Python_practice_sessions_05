from collections.abc import Sequence
from typing import Any, TypeVar, Iterable

T = TypeVar('T')

def get_first_element(elements: Sequence[T]) -> T | None:
    if not elements:
        return None
    return elements[0]


C = TypeVar('C')


def get_elements_by_type(elements: Iterable[Any], kind: type[C]) -> list[C]:
    lst: list[C] = []

    for element in elements:
        if isinstance(element, kind):
            lst.append(element)
    return lst