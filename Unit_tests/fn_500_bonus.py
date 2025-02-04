def factorial(n: int) -> int:
    """
    Returns the factorial of n.

    :param n: the integer.
    :type n: int
    :return: int number of factorial of n.
    :rtype: int
    :raises: ValueError if n is negative.
             RecursionError if n is higher than 999.
    """
    if n < 0:
        raise ValueError("n must be positive")
    if n > 998:
        raise RecursionError("n must be smaller than 999")

    return 1 if n == 0 else n * factorial(n - 1)


def factorial_iterative(n: int) -> int:
    """
    Returns the factorial of n, using iterative method.
    :param n: the integer.
    :type n: int
    :return: int number of factorial of n.
    :rtype: int
    :raises: ValueError if n is negative.
    """
    if n < 0:
        raise ValueError("n must be positive")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def count_vowels(text: str) -> int:
    """
    Counts vowels in text.
    :param text: the text.
    :type text: str
    :return: int number of vowels in text.
    :rtype: int
    """
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)
