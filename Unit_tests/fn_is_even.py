def is_even(num: int | float) -> bool:
    if not isinstance(num, (int, float)):
        raise TypeError(f"Expected int or float, but got {type(num)}")
    if isinstance(num, float) and not num.is_integer():
        raise ValueError(f"Expected an integer-like value, but got a float: {num}")
    return not int(num) % 2
