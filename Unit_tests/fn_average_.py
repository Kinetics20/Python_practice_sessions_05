def calc_average(l: list[int | float]) -> float:
    """
    Calculates average of list
    :param l: The list of numbers, list contains mixed types of numbers.
    :type l: list[int | float]
    :return: Average of list.
    :rtype: float
    : raises ValueError if list is empty.
    """
    if not l:
        raise ValueError("List cannot be empty")
    return sum(l) / len(l)
