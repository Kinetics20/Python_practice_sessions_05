def create_matrix(n: int) -> list[list[int]]:
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    """
    Creates 2D matrix of size n x n.
    :param n: int
    :return: 2D matrix of size n x n.
    :rtype: list[list[int]]
    """
    return [[j + i * n for j in range(1, n + 1)] for i in range(n)]
