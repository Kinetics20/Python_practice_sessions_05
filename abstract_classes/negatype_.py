from abc import ABC, abstractmethod
from collections.abc import Iterable, Generator
from typing import TypeVar, Any

data: list[Any] = [(1, 2), [3, 4, [1, 2], [2, 3, 4, 5]], [1, 2]]
data1: list[Any] = [1, 2, 3]
data2: list[Any] = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                    'November', 'December']

class NonStringIterable(ABC):
    @abstractmethod
    def __iter__(self):
        raise NotImplementedError

    @classmethod
    def __subclasshook__(cls, subclass):
        if cls is NonStringIterable:
            if issubclass(subclass, str):
                return False
            if hasattr(subclass, '__iter__') and callable(subclass.__iter__):
                return True
        return NotImplemented


T = TypeVar("T")


def flatten(items: Iterable[T]) -> Generator[T]:
    for item in items:
        if isinstance(item, NonStringIterable):
            yield from flatten(item)
        else:
            yield item


# def flatten(items):
#     result = []
#
#     for item in items:
#         result.extend(item)
#     return result

# def flatten(items):
#     return [x for y in items for x in y]

# def flatten(items):
#     result_ = []
#
#     for item in items:
#         for element in item:
#             result_.append(element)
#     return result_

if __name__ == '__main__':
    result = list(flatten(data2))

    print(result)

    # assert result == ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
    #                 'November', 'December']
