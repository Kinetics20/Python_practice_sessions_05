def dogs_age(age: int | float) -> int | float | str:
    return age * 10.5 if 0 < age <= 2 else 21 + (age - 2) * 4 if age > 2 else f'age must be greater than 0'


def dogs_age_2(age: int | float) -> int | float:
    if not isinstance(age, (int, float)) or type(age) is bool:
        raise TypeError(f'Expected int or float but got {type(age)}')
    if age == float('inf') or age == -float('inf'):
        raise ValueError(f'age must be a finite number')
    if age <= 0:
        raise ValueError('age must be greater than 0')
    return age * 10.5 if age <= 2 else 21 + (age - 2) * 4


if __name__ == '__main__':
    test_cases = [2, 3.5, -1, "pies", True, None]

    for case in test_cases:
        if isinstance(case, (int, float)) and not isinstance(case, bool):
            try:
                print(f"Input: {case}, Dog's age: {dogs_age_2(case)}")
            except ValueError as e:
                print(f"Input: {case}, Error: {e}")
        else:
            print(f"Input: {case}, Error: Expected int or float but got {type(case).__name__}")
