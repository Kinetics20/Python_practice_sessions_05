def create_list_compr_factorial(n: int) ->list[int]:
    if n < 0:
        raise ValueError('n must be a non-negative integer')
    return [i ** 2 for i in range(n)]
