def repeat_strings_with_map(strings: list[str], counts: list[int]) -> list[str]:
    """
    Repeats each string in the 'strings' list based on the corresponding value in the 'counts' list.
    :param strings: list of strings to repeat
    :type strings: list[str]
    :param counts: list of integers indicating the number of repetitions
    :type counts: list[int]
    :return: new list with repeated strings
    :rtype: list[str]
    """
    return list(map(lambda s, c: s * c, strings, counts))
