import re
import random


def get_user_numbers(quantity: int = 5) -> list[int]:
    user_digits_txt: str = input(f'Enter {quantity} digits separated by comma:\n ')
    user_digits_lst: list[str] = re.findall(r'\d+', user_digits_txt)

    if len(user_digits_lst) != quantity:
        raise ValueError(f'Your amount of digits: {len(user_digits_lst)} is not equal to {quantity}')

    return [int(num) for num in user_digits_lst]


def is_in_range(num: int) -> bool:
    return 1 <= num <= 49


def is_not_redundant(numbers: list[int]) -> bool:
    return len(set(numbers)) == len(numbers)


def validate(digits: list[int]) -> None:
    for num in digits:
        if not is_in_range(num):
            raise ValueError(f'Number {num} is not in range 1-49')

    if not is_not_redundant(digits):
        raise ValueError(f'Redundant numbers are not allowed')


def draw_digits(quantity: int) -> list[int]:
    num_list: list[int] = []
    while len(num_list) < quantity:
        drawn_num: int = random.randint(1, 49)
        if drawn_num not in num_list:
            num_list.append(drawn_num)
    return num_list


def check_hits(user_digits: list[int], drawn_digits: list[int]) -> set[int]:
    return set(user_digits) & set(drawn_digits)


def show_results(hits: set[int]) -> None:
    if len(hits) == 0:
        print('Try again!')
    else:
        print(f'Hits: {len(hits)}. Your digits: {", ".join(str(hit) for hit in hits)}.')


def play(quantity: int = 5) -> None:
    while True:
        try:
            user_digits = get_user_numbers(quantity)
        except ValueError as e:
            print(e)
            continue

        try:
            validate(user_digits)
        except ValueError as e:
            print(e)
            continue

        break

    digits: list[int] = draw_digits(quantity)
    hits: set[int] = check_hits(user_digits, digits)
    show_results(hits)


# TODO write a function that shows in the results how much money you won
if __name__ == '__main__':
    game_type = int(input('choose game type [5-Mini Lotto draw, 6-Lotto draw]'))
    play(game_type)
