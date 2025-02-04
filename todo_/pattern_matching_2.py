# Pattern matching

# TODO 1// simple match

def ex_1():
    while True:
        command = input('Enter command: \n')
        match command:
            case 'add todo':
                print(f'ToDo added!')
            case 'show todo':
                print('Yours todos')
            case 'bye':
                print('Bye!')
                break
            # TODO case _ - when the user enter invalid input not matched to the case
            # wild card !!!!
            case _:
                print('unknown command')


# ex_1()


# TODO 2// match on different types


def ex_2():
    for x in 1, 'two', 3.14, Exception('home'), lambda data: data + 42:
        match x:
            case int():
                print(f'int: {x}')
            case str():
                print(f'str: {x}')
            case float():
                print(f'float: {x}')
            case Exception():
                print(f'Exception: {x}')
            case y:
                print(f'y: {y}')


# ex_2()


# TODO 3// guarded matching


def ex_3():
    for i in range(6):
        match i:
            # guard - condition - if i < 4
            case 1 | 3 | 5 if i < 4:
                print(f'{i} is odd and less than 4')
            case 1 | 3 | 5 if i > 4:
                print(f'{i} is odd and greater than 4')
            case 2 | 4:
                print(f'{i} is even')


# ex_3()


# TODO first true condition ends the match i.e :

# z = 42
#
# match z:
#     case 42:
#         print('z is : 42')
#     case 42:
#         print('z is : 43')
#     case _:
#         print('z is not 42 or 44')


# TODO 4// aliased matching


def ex_4():
    for calls in [1, 2, 3], (4, 5, 6, 7, 8, 9, 8), {'a': 42}:
        match calls:
            case [1, 2, 3] as my_list:
                print(f'list: {my_list}')
            case (_, 5 as my_int, _, *i) as my_tuple if len(calls) > 5:
                print(f'tuple: {my_tuple} with {my_int}')
            case {'a': 42} as my_dict:
                print(f'dict: {my_dict}')
            case _:
                print('unknown')


# ex_4()


# TODO 5// matching with walrus operator


def ex_5():
    match the_answer := 2 * 1 * 3 * 7:
        case _:
            print(f'The answer is {the_answer}')

ex_5()
