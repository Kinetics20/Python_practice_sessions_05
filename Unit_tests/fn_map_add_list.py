def add_elements_list(list_1: list[int], list_2: list) -> list[int]:
    """
    Adds numbers from list_1 to list_2 for the exact indexes, i.e. list_1[0] + list_2[0] etc.
    :param list_1: first list of integers
    :type list_1: list[int]
    :param list_2: second list of integers
    :type list_2: list[int]
    :return: new list of added numbers
    :rtype: list[int]
    """
    return list(map(lambda a, b: a + b, list_1, list_2))