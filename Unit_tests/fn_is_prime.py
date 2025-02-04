import math


def is_prime(num: int) -> bool:
    """
    Function takes number and returns true if it is a prime number
    :param num: The num must be an integer number
    :type num: int
    :return: bool value, True if it is a prime number, False otherwise
    :rtype: bool
    """
    if not isinstance(num, int) or isinstance(num, bool):
        raise TypeError(f'Expected int but got {type(num)}')
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
