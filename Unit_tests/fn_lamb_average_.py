from typing import Callable

calc_average: Callable[[list[int | float]], float] = lambda l: (
    (sum(l) / len(l)) if l else (_ for _ in ()).throw(ValueError("List cannot be empty"))
)
calc_average.__doc__ = """
Calculates average of list.

:param l: The list of numbers, list contains mixed types of numbers. (int or float).
:type l: list[int | float]
:return: Average of list as float.
:rtype: float
:raises ValueError if list is empty.
"""
