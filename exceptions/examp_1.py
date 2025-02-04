def divide(a: float, b: float) -> float | str:
    return a / b

try:
    result = divide(20, 0)
except ValueError as e:
    '???'

# result = divide(20, 0)
# if isinstance(result, float):
#     result2 = result - 10
#     print(result2)
# else:
#