from collections.abc import Callable


def get_user_name() -> str:
    user_name = input("Enter your name: ")
    if len(user_name.strip()) == 0:
        raise ValueError("Name cannot be empty")

    return user_name

def handle_user_input(cb: Callable[[], str]) ->str:
    while True:
        try:
            return cb()
        except ValueError as e:
            print(e)
            continue

if __name__ == '__main__':
    user: str = handle_user_input(get_user_name)
    print(f"Hello, {user}")