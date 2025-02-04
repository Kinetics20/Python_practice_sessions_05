def add_string_lengths_with_map(strings: list[str], increments: list[int]) -> list[int]:
    """
    Computes the length of each string in 'strings' and adds the corresponding value from 'increments'.
    :param strings: list of strings to calculate lengths
    :type strings: list[str]
    :param increments: list of integers to add to each string's length
    :type increments: list[int]
    :return: list of resulting integers
    :rtype: list[int]
    """
    return list(map(lambda s, inc: len(s) + inc, strings, increments))
