def filter_odd_numbers(num: list[int]) -> list[int]:
    """
    Returns a list of odd numbers from a list.

    :param num: List of integer numbers.
    :type num: list[int]
    :return: List of odd numbers.
    :rtype: list[int]
    :raises TypeError: If `num` is not a list of integer numbers or if `num` is not a list.
    """
    if not isinstance(num, list):
        raise TypeError('Input must be a list')
    if not all(isinstance(item, int) for item in num):
        raise TypeError('All elements in the list must be integers')

    return [item for item in num if item & 1]
