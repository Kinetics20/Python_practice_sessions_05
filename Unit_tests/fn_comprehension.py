def create_lst_(num: int) -> list[int]:
    if not isinstance(num, int) or isinstance(num, bool):
        raise TypeError(f'Expected int but got {type(num)}')
    return [item for item in range(num)]


if __name__ == "__main__":
    print(create_lst_('Home'))
