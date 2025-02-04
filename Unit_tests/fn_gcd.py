def gcd(a: int, b: int) -> int:
    """
    The function returns the greatest common divisor (GCD) of two integers.
    :param a: First integer number.
    :type a: int
    :param b: Second integer number.
    :type b: int
    :return: The greatest common divisor (GCD)
    :rtype: int
    :raises TyperError: If a or b is not an integer numbers.
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("a and b must be integers")

    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a
