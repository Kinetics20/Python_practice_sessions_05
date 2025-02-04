# This is a set of 500 pieces python functions
from collections.abc import Sequence
from math import pi


# 001
# adding two numbers

def add_num(a, b):
    return a + b


assert add_num(2, 5) == 7


# 002
# subtracting two numbers

def subtract_num(a, b):
    return a - b


assert subtract_num(2, 5) == -3


# 003
# multiplying two numbers

def multiply_num(a, b):
    return a * b


assert multiply_num(2, 5) == 10


# 004
# dividing two numbers

def divide_num(a, b):
    return a / b


assert divide_num(2, 5) == 0.4


# 005
# subtracting two numbers without the rest

def divide_num_without_rest(a, b):
    return a // b


assert divide_num_without_rest(2, 5) == 0


# 006
# exponentiation of two numbers

def exponentiation_num(a, b):
    return a ** b


assert exponentiation_num(5, 2) == 25


# 007
# square root

def count_square_root(a):
    return a ** 0.5


assert count_square_root(4) == 2


# 008
# BMI calculator

def bmi(mass, height):
    return mass / height ** 2


assert bmi(89, 1.8) == 27.469135802469133


# 009
# check word is palindrome

def check_palindrome(word):
    return word == word[::-1]


assert check_palindrome("hello") == False


# 010
# count square area

def square_area(a):
    return a * a


assert square_area(4) == 16


# 011
# count rectangle area

def rectangle_area(a, b):
    return a * b


assert rectangle_area(2, 3) == 6


# 012
# count triangle area

def triangle_area(a, b, h):
    return 0.5 * (a + b) * h


assert triangle_area(2, 3, 4) == 10


# 013
# count perimeter of a square

def square_perimeter(a):
    return a * 4


assert square_perimeter(4) == 16


# 014
# count perimeter of a rectangle

def perimeter_rectangle(a, b):
    return 2 * (a + b)


assert perimeter_rectangle(4, 4) == 16


# 015
# count perimeter of a triangle

def perimeter_triangle(a, b, c):
    return a + b + c


# 016
# count circumference of a circle

def circumference_circle(r):
    return 2 * pi * r


assert circumference_circle(4) == 25.132741228718345


# 017
# count circle area

def circle_area(r):
    return pi * r * r


assert circle_area(2) == 12.566370614359172


# 018
# count trapezoid area

def trapezoid_area(a, b, h):
    return 0.5 * (a + b) * h


assert trapezoid_area(4, 4, 4) == 16


# 019
# count trapezoid perimeter

def trapezoid_perimeter(a, b, c, d):
    return a + b + c + d


assert trapezoid_perimeter(4, 4, 4, 4) == 16


# 020
# count cube volume

def cube_volume(a):
    return a ** 3


assert cube_volume(4) == 64


# 021
# count cube total surface area

def cube_total_surface_area(a):
    return 6 * a * a


assert cube_total_surface_area(2) == 24


# 022
# count cuboid volume

def cuboid_volume(a, b, c):
    return a * b * c


assert cuboid_volume(4, 4, 4) == 64


# 023
# count cuboid total surface area

def cuboid_total_surface_area(a, b, c):
    return 2 * (a * b + a * c + b * c)


assert cuboid_total_surface_area(4, 4, 4) == 96


# 024
# count sphere area

def sphere_area(r):
    return 4 / 3 * pi * r ** 3


assert sphere_area(4) == 268.082573106329


# 025
# count sphere volume

def sphere_volume(r):
    return 4 * pi * r ** 2


assert sphere_volume(4) == 201.06192982974676


# 026
# count cone volume

def cone_volume(r, h):
    return 1 / 3 * pi * r ** 2 * h


assert cone_volume(4, 4) == 67.02064327658225


# 027
# count cone total area

def cone_total_surface_area(r, l):
    return pi * r * (r + l)


assert cone_total_surface_area(4, 4) == 100.53096491487338


# 028
# count cylinder total area

def cylinder_area(r, h):
    return 2 * pi * r * (r + h) == 201.06192982974676


# 029
# count cylinder volume

def cylinder_volume(r, h):
    return pi * r ** 2 * h


assert cylinder_volume(4, 5) == cylinder_volume(4, 5)


# 030
# count pyramid volume square based

def pyramid_volume_square_based(a, h):
    return 1 / 3 * a ** a * h


assert pyramid_volume_square_based(4, 4) == 341.3333333333333

# 030 , 031 , 032
# using list comprehension return new list with only even numbers

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def create_new_list_even_num(array):
    return [num for num in array if not num % 2]
    # return [ num for num in array if not num & 1]


assert create_new_list_even_num(list_1) == [2, 4, 6, 8, 10]

# 033 , 034 , 035
# using list comprehension flat list of lists

list_2 = [[1, 3], [2, 4], [3, 5]]


def create_new_flat_list(array):
    return [x for y in array for x in y]


assert create_new_flat_list(list_2) == [1, 3, 2, 4, 3, 5]


# 036 , 037 , 038
# using list comprehension multiply each element list by n

def create_new_list_mul_by_n(n, array):
    return [item * n for item in array]


assert create_new_list_mul_by_n(10, list_1) == [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# 039 , 040 , 041
# using list comprehension filter list and keep only str value

list_3 = [1, 'home', 3, 'John', 5, 'funeral', 'infinity', 'compulsive', 9, 10]


def create_new_str_list(array):
    return [item for item in array if isinstance(item, str)]


assert create_new_str_list(list_3) == ['home', 'John', 'funeral', 'infinity', 'compulsive']

# 042 , 043 , 044
# using dict comprehension create dict from the list

list_4 = ['home', 'John', 'funeral', 'infinity', 'compulsive']


def create_dict_from_list(array):
    return {key: value for key, value in enumerate(array)}


assert create_dict_from_list(list_4) == {0: 'home', 1: 'John', 2: 'funeral', 3: 'infinity', 4: 'compulsive'}

# 045 , 046 , 047
# using list comprehension create list from dictionary

dict_1 = {0: 'home', 1: 'John', 2: 'funeral', 3: 'infinity', 4: 'compulsive'}


def create_list_from_dict(any_dict):
    return [item for item in any_dict.values()]


assert create_list_from_dict(dict_1) == ['home', 'John', 'funeral', 'infinity', 'compulsive']


# 048 , 049 , 050
# using list comprehension create list of tuples from dictionary

def create_list_tuples_from_dict(any_dict):
    return [(key, value) for key, value in any_dict.items()]


assert create_list_tuples_from_dict(dict_1) == [(0, 'home'), (1, 'John'), (2, 'funeral'), (3, 'infinity'),
                                                (4, 'compulsive')]

# 051 , 052 , 053
# using list comprehension create flat list from list of tuples

list_5 = [(0, 'home'), (1, 'John'), (2, 'funeral'), (3, 'infinity'), (4, 'compulsive')]


def create_flat_list_from_list_of_tuples(array):
    return [x for y in array for x in y]


assert create_flat_list_from_list_of_tuples(list_5) == [0, 'home', 1, 'John', 2, 'funeral', 3, 'infinity', 4,
                                                        'compulsive']


# 054 , 055 , 056
# using list comprehension create list from dictionary using keys

def create_list_from_dict_key(any_dict):
    return [key for key in any_dict]
    # return [key for key, value in any_dict.items()]


assert create_list_from_dict_key(dict_1) == [0, 1, 2, 3, 4]


# 057 , 058 , 059
# using list comprehension create list from dictionary using values with len condition of value

def create_list_from_dict_value_condition(any_dict):
    return [item for item in any_dict.values() if len(item) > 5]


assert create_list_from_dict_value_condition(dict_1) == ['funeral', 'infinity', 'compulsive']


# 060 , 061 , 062
# using list comprehension create list from dictionary using keys and values like a string

def create_list_from_dict_k_v_str(any_dict):
    return [f'{key}: {value}' for key, value in any_dict.items()]


assert create_list_from_dict_k_v_str(dict_1) == ['0: home', '1: John', '2: funeral', '3: infinity', '4: compulsive']


# 063 , 064 , 065
# using list comprehension create sliced list

def create_sliced_list(array):
    return [item[:3] for item in array]


assert create_sliced_list(list_4) == ['hom', 'Joh', 'fun', 'inf', 'com']


# 066 , 067 , 068
# using list comprehension create new list with item[1]

def create_list_item_one_index(array):
    return [item[1] for item in array]


assert create_list_item_one_index(list_4) == ['o', 'o', 'u', 'n', 'o']

# 069 , 070 , 071
# using list comprehension create new list if letter in item

letter = 'n'


def create_list_letter_in_item(array, n):
    return [item for item in array if n in item]


assert create_list_letter_in_item(list_4, letter) == ['John', 'funeral', 'infinity']


# 072 , 073 , 074
# using list comprehension create new list if not item % n

def create_list_from_range_modulo_n(n):
    return [item for item in range(101) if not item % n]


assert create_list_from_range_modulo_n(18) == [0, 18, 36, 54, 72, 90]


# 075 , 076 , 077
# using list comprehension create new list if not item % n and in the specific scope

def create_list_from_range_modulo_n_and_cond(n, a, b):
    return [item for item in range(101) if not item % n and a < item <= b]


assert create_list_from_range_modulo_n_and_cond(20, 40, 80) == [60, 80]

# 078 , 079 , 080
# using list comprehension create new list with dictionary's values capitalized

dict_2 = {0: 'home_AS_a_Hall', 1: ' John2    ', 2: 'funeral123   ', 3: '88infinity',
          4: 'compulsive is a bad character treat'}


def create_list_from_dict(any_dict):
    return [item.capitalize() for item in any_dict.values()]


assert create_list_from_dict(dict_2) == ['Home_as_a_hall',
                                         ' john2    ',
                                         'Funeral123   ',
                                         '88infinity',
                                         'Compulsive is a bad character treat']

# 081
# string capitalize method

sentence_1 = ' Better now than NEVER      '


def str_capitalize(any_str):
    return any_str.capitalize()


assert str_capitalize(sentence_1) == ' better now than never      '


# 082 , 083 , 084
# using list comprehension create new list with dictionary's values lowered

def create_list_from_dict_lowered(any_dict):
    return [item.lower() for item in any_dict.values()]


assert create_list_from_dict_lowered(dict_2) == ['home_as_a_hall',
                                                 ' john2    ',
                                                 'funeral123   ',
                                                 '88infinity',
                                                 'compulsive is a bad character treat']


# 085
# string lower method

def str_lower(any_str):
    return any_str.lower()


assert str_lower(sentence_1) == ' better now than never      '


# 086 , 087 , 088
# using list comprehension create new list with dictionary's values upper

def create_list_from_dict_upper(any_dict):
    return [item.upper() for item in any_dict.values()]


assert create_list_from_dict_upper(dict_2) == ['HOME_AS_A_HALL',
                                               ' JOHN2    ',
                                               'FUNERAL123   ',
                                               '88INFINITY',
                                               'COMPULSIVE IS A BAD CHARACTER TREAT']


# 089
# string lower method

def str_upper(any_str):
    return any_str.upper()


assert str_upper(sentence_1) == ' BETTER NOW THAN NEVER      '


# 090 , 091 , 092
# using list comprehension create new list with dictionary's values titled

def create_list_from_dict_titled(any_dict):
    return [item.title() for item in any_dict.values()]


assert create_list_from_dict_titled(dict_2) == create_list_from_dict_titled(dict_2)


# 093
# string lower method

def str_title(any_str):
    return any_str.title()


assert str_title(sentence_1) == ' Better Now Than Never      '


# 094
# string swapcase method

def str_swapcase(any_str):
    return any_str.swapcase()


assert str_swapcase(sentence_1) == ' bETTER NOW THAN never      '


# 095
# string strip method

def str_strip(any_str):
    return any_str.strip()


assert str_strip(sentence_1) == 'Better now than NEVER'


# 096
# string strip and title methods

def str_strip_and_title(any_str):
    return any_str.strip().title()


assert str_strip_and_title(sentence_1) == 'Better Now Than Never'


# 097
# string replace method

def str_replace(any_str):
    return any_str.replace(' ', '_$_$_')


assert str_replace(sentence_1) == '_$_$_Better_$_$_now_$_$_than_$_$_NEVER_$_$__$_$__$_$__$_$__$_$__$_$_'


# 098
# string replace method

def str_replace_and_count(any_str):
    return any_str.replace(' ', '_$_$_', 4)


assert str_replace_and_count(sentence_1) == '_$_$_Better_$_$_now_$_$_than_$_$_NEVER      '


# 099, 100, 101
# using list comprehension convert list to string

def create_list_to_str():
    return ''.join([str(item) for item in range(11)])


assert create_list_to_str() == '012345678910'


# 102, 103, 104
# using list comprehension convert list to string and next to int

def create_list_to_str_to_int():
    return int(''.join([str(item) for item in range(11)]))


assert create_list_to_str_to_int() == 12345678910


# 105, 106, 107
# using list comprehension achieve two list from dictionary

def create_lists_from_dict(any_dict):
    l_1 = [item for item in any_dict.values()]
    l_2 = [item for item in any_dict.keys()]

    return l_1, l_2


assert create_lists_from_dict(dict_2) == (
    ['home_AS_a_Hall', ' John2    ', 'funeral123   ', '88infinity', 'compulsive is a bad character treat'],
    [0, 1, 2, 3, 4])

# 108, 109, 110
# using dict comprehension create dict from tuple

my_tuple = ("home", "apple", "tower")


def create_dict_from_tuple(any_tuple):
    return {key: value for key, value in enumerate(any_tuple)}


assert create_dict_from_tuple(my_tuple) == {0: 'home', 1: 'apple', 2: 'tower'}

sentence_2 = 'New York 76st'


# 111
# string isalnum method , are there only letters and digits in the str

def str_isalnum(any_str):
    return any_str.isalnum()


assert str_isalnum(sentence_2) == False


# 112
# string isalpha method , are there only letters in the str

def str_isalpha(any_str):
    return any_str.isalpha()


assert str_isalpha(sentence_2) == False


# 113
# string isalpha method , are there only digits in the str

def str_isdigit(any_str):
    return any_str.isdigit()


assert str_isdigit('1234') == True


# 114
# string isdecimal method , are there only decimal digits in the str

def str_isdecimal(any_str):
    return any_str.isdecimal()


assert str_isdecimal('1234') == True


# 115
# string isnumeric method , are there only numbers in the str

def str_isnumeric(any_str):
    return any_str.isnumeric()


assert str_isnumeric('12 34') == False


# 116
# string islower method , are there only lower letters in the str

def str_islower(any_str):
    return any_str.islower()


assert str_islower('where is the bus stop') == True


# 117
# string isupper method , are there only upper letters in the str

def str_isupper(any_str):
    return any_str.isupper()


assert str_isupper('where is the bus stop') == False


# 118
# string isspace method , are there only white signs in the str

def str_isspace(any_str):
    return any_str.isspace()


assert str_isspace('      ') == True


# 119
# string split method , create list from str using split

def str_split(any_str):
    return any_str.split(',')


assert str_split('ab,cd,ef') == ['ab', 'cd', 'ef']


# 120
# using join method , create str from list of str

def list_join(any_list_str):
    return ', '.join(any_list_str)


assert list_join(['ab', 'cd', 'ef']) == 'ab, cd, ef'


# 121
# Write a function that given a floor in the american system returns the floor in the european system.

# Examples
#
# 1  =>  0
# 0  =>  0
# 5  =>  4
# 15  =>  13
# -3  =>  -3

def get_real_floor(n):
    return n if n < 1 else n - 1 if n < 13 else n - 2


assert get_real_floor(5) == 4

handball_elite = [
    {
        "name": "FC Barcelona",
        "country": "Spain",
        "city": "Barcelona",
        "founded": 1942,
        "arena": "Palau Blaugrana",
        "capacity": 7500,
        "colors": ["burgundy", "navy blue"],
        "successes_in_cl": {"1st": 12, "2nd": 5, "3rd": 3},
    },
    {
        "name": "SC Magdeburg",
        "country": "Germany",
        "city": "Magdeburg",
        "founded": 1955,
        "arena": "GETEC Arena",
        "capacity": 8000,
        "colors": ["green", "red"],
        "successes_in_cl": {"1st": 4, "2nd": 0, "3rd": 0},
    },
    {
        "name": "THW Kiel",
        "country": "Germany",
        "city": "Kiel",
        "founded": 1904,
        "arena": "Sparkassen",
        "capacity": 10250,
        "colors": ["white", "black"],
        "successes_in_cl": {"1st": 4, "2nd": 4, "3rd": 3},
    },
    {
        "name": "AaB Handbold",
        "country": "Denmark",
        "city": "Aalborg",
        "founded": 2000,
        "arena": "Jutlander",
        "capacity": 5020,
        "colors": ["red", "white"],
        "successes_in_cl": {"1st": 0, "2nd": 2, "3rd": 0},
    },
    {
        "name": "Paris SG Handball",
        "country": "France",
        "city": "Paris",
        "founded": 1941,
        "arena": "Stade Pierre",
        "capacity": 4500,
        "colors": ["blue", "red", "white"],
        "successes_in_cl": {"1st": 0, "2nd": 1, "3rd": 4},
    },
    {
        "name": "KS Iskra Kielce",
        "country": "Poland",
        "city": "Kielce",
        "founded": 1965,
        "arena": "Hala Legionów",
        "capacity": 4200,
        "colors": ["yellow", "blue", "white"],
        "successes_in_cl": {"1st": 1, "2nd": 2, "3rd": 2},
    },
    {
        "name": "MKB Veszprem KC",
        "country": "Hungary",
        "city": "Veszprem",
        "founded": 1977,
        "arena": "Veszprém",
        "capacity": 5096,
        "colors": ["red", "white"],
        "successes_in_cl": {"1st": 0, "2nd": 4, "3rd": 1},
    },
    {
        "name": "Fuechse Berlin",
        "country": "Germany",
        "city": "Berlin",
        "founded": 1891,
        "arena": "Max Schmeling",
        "capacity": 8500,
        "colors": ["green", "black", "white"],
        "successes_in_cl": {"1st": 0, "2nd": 0, "3rd": 0},
    },
    {
        "name": "SG Flensburg-Handewitt",
        "country": "Germany",
        "city": "Flensburg-Handewitt",
        "founded": 1990,
        "arena": "Flens Arena",
        "capacity": 6300,
        "colors": ["blue", "red", "white"],
        "successes_in_cl": {"1st": 1, "2nd": 2, "3rd": 0},
    },
    {
        "name": "Sporting Clube de Portugal",
        "country": "Portugal",
        "city": "Lisbon",
        "founded": 1932,
        "arena": "Pavilhão",
        "capacity": 3000,
        "colors": ["green", "white"],
        "successes_in_cl": {"1st": 0, "2nd": 0, "3rd": 0},
    },
    {
        "name": "Montpellier HB",
        "country": "France",
        "city": "Montpellier",
        "founded": 1982,
        "arena": "FDI Stadium",
        "capacity": 9000,
        "colors": ["blue", "white"],
        "successes_in_cl": {"1st": 2, "2nd": 0, "3rd": 0},
    },
    {
        "name": "Wisla Plock",
        "country": "Poland",
        "city": "Płock",
        "founded": 1964,
        "arena": "Orlen Arena",
        "capacity": 5492,
        "colors": ["blue", "white"],
        "successes_in_cl": {"1st": 0, "2nd": 0, "3rd": 0},
    },
    {
        "name": "SC Pick Szeged",
        "country": "Hungary",
        "city": "Szeged",
        "founded": 1961,
        "arena": "Pick Aréna",
        "capacity": 8143,
        "colors": ["blue", "white"],
        "successes_in_cl": {"1st": 0, "2nd": 0, "3rd": 0},
    },
    {
        "name": "HBC Nantes",
        "country": "France",
        "city": "Nantes",
        "founded": 1953,
        "arena": "Palais des",
        "capacity": 10750,
        "colors": ["pink", "yellow"],
        "successes_in_cl": {"1st": 0, "2nd": 1, "3rd": 0},
    },
    {
        "name": "GOG Svendborg TGI",
        "country": "Denmark",
        "city": "Gudme",
        "founded": 1973,
        "arena": "Phønix Tag",
        "capacity": 2265,
        "colors": ["yellow", "red"],
        "successes_in_cl": {"1st": 0, "2nd": 0, "3rd": 0},
    },
    {
        "name": "Dinamo Bucarest",
        "country": "Romania",
        "city": "Bucarest",
        "founded": 1953,
        "arena": "Sala Polivalentă",
        "capacity": 5300,
        "colors": ["red", "white"],
        "successes_in_cl": {"1st": 1, "2nd": 1, "3rd": 0},
    },
    {
        "name": "RK Nexe Nasice",
        "country": "Croatia",
        "city": "Nasice",
        "founded": 1959,
        "arena": "Sportska",
        "capacity": 2500,
        "colors": ["green", "black"],
        "successes_in_cl": {"1st": 0, "2nd": 0, "3rd": 0},
    },
    {
        "name": "RK Croatia Zagreb",
        "country": "Croatia",
        "city": "Zagreb",
        "founded": 1922,
        "arena": "Arena Zagreb",
        "capacity": 15200,
        "colors": ["blue", "white", "red"],
        "successes_in_cl": {"1st": 2, "2nd": 4, "3rd": 0},
    },
    {
        "name": "Rhein Neckar Löwen",
        "country": "Germany",
        "city": "Lowen",
        "founded": 2002,
        "arena": "SAP Arena",
        "capacity": 14500,
        "colors": ["yellow", "navy blue"],
        "successes_in_cl": {"1st": 0, "2nd": 0, "3rd": 1},
    },
    {
        "name": "Valur",
        "country": "Iceland",
        "city": "Reykjavík",
        "founded": 1911,
        "arena": "N höllin",
        "capacity": 1300,
        "colors": ["red", "white"],
        "successes_in_cl": {"1st": 0, "2nd": 0, "3rd": 0},
    }
]


# 122, 123, 124
# Write a function that return list of tuples and takes list of dictionaries
# question : What are the 3 oldest clubs (among those mentioned) and how many years ago were they founded ?

def three_oldest_club(data):
    sorted_clubs = sorted(data, key=lambda x: x['founded'])

    oldest_clubs = sorted_clubs[:3]

    current_year = 2024

    result = [(club['name'], current_year - club['founded']) for club in oldest_clubs]

    return result


assert three_oldest_club(handball_elite) == [('Fuechse Berlin', 133), ('THW Kiel', 120), ('Valur', 113)]


# 125, 126, 127
# Write a function that return list of dictionary
# question : Has any club from Poland achieved success in the Champions League (successes_in_cl), if so, display information about it.

def check_polish_clubs(data):
    return [club for club in data if club['country'] == 'Poland' and
            (club['successes_in_cl']['1st'] > 0 or club['successes_in_cl']['2nd'] > 0 or
             club['successes_in_cl']['3rd'] > 0)]


assert check_polish_clubs(handball_elite) == [{'name': 'KS Iskra Kielce',
                                               'country': 'Poland',
                                               'city': 'Kielce',
                                               'founded': 1965,
                                               'arena': 'Hala Legionów',
                                               'capacity': 4200,
                                               'colors': ['yellow', 'blue', 'white'],
                                               'successes_in_cl': {'1st': 1, '2nd': 2, '3rd': 2}}]


# 128, 129, 130
# Write a function that return list of tuples and takes list of dictionaries
# question : Which countries (name the top 3) are most represented by the clubs mentioned in the ranking?

def check_amount_country(data):
    country_counts = {}

    for club in data:
        country = club['country']
        if country in country_counts:
            country_counts[country] += 1
        else:
            country_counts[country] = 1

    sorted_country_counts = sorted(country_counts.items(), key=lambda x: x[1], reverse=True)

    return sorted_country_counts[:3]


assert check_amount_country(handball_elite) == [('Germany', 5), ('France', 3), ('Denmark', 2)]

d = {
    "Poland": "Warsaw",
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "United Kingdom": "London",
    "Canada": "Ottawa",
    "United States": "Washington, D.C.",
    "Japan": "Tokyo",
    "Australia": "Canberra"
}


# 131, 132, 133
# Write a function that takes dictionary and return list  key/s that starts with J letter


def keys_start_with_j(any_dict):
    return [key for key, value in any_dict.items() if key.startswith('J')]


assert keys_start_with_j(d) == ['Japan']


# 134, 135, 136
# Write a function that takes dictionary and return list of value/s that ends with n letter

def value_ends_with_n(any_dict):
    return [value for key, value in any_dict.items() if value.endswith('n')]


assert value_ends_with_n(d) == ['Berlin', 'London']


# 137, 138, 139
# Write a function that takes dictionary and return list of
# keys when value/s starts with W and ends with w letter

def value_start_w_ends_w(any_dict):
    return [key for key, value in any_dict.items()
            if value.startswith('W') and value.endswith('w')]


assert value_start_w_ends_w(d) == ["Poland"]


# 139, 140, 141
# Write a function that takes dictionary and return list of
# values when a letter or t letter exists 2 or more times

def value_key_value_count_a_t(any_dict):
    return [key for key, value in any_dict.items()
            if value.count('a') >= 2 or value.count('t') >= 2]


# print(value_key_value_count_a_t(d))
assert value_key_value_count_a_t(d) == ['Poland', 'Canada', 'Australia']


# 142, 143, 144
# for the list named handball_elite return list of countries that
# value of 'capacity' > 5000 nad value of 'country' <= 6

def give_l(list_dict):
    return [item['country'] for item in list_dict if item['capacity'] > 5000 and
            len(item['country']) <= 6]


assert give_l(handball_elite) == ['Spain', 'France', 'Poland', 'France']


# 145
# count method for str

def str_count(any_str):
    return any_str.count('a')


# print(str_count('Alice has a cat'))
assert str_count('Alice has a cat') == 3


# 146
# count method for str with lower

def str_count_lower(any_str):
    return any_str.lower().count('a')


assert str_count_lower('Alice has a cat') == 4


# 147
# find method for str

def str_find(any_str):
    return any_str.find('cat')


assert str_find('Alice has a cat') == 12


# 148, 149, 150
# for the list named handball_elite return list of cities that
# value of 'capacity' is not an odd number nad value of 'country' <= 6

def give_l_2(list_dict):
    return [item['city'] for item in list_dict if not item['capacity'] & 1 and
            len(item['country']) <= 6]


# print(give_l_2(handball_elite))
assert give_l_2(handball_elite) == ['Barcelona', 'Paris', 'Kielce', 'Montpellier', 'Płock', 'Nantes']


# 151
# index method for str

def str_index(any_str):
    return any_str.index('cat')


assert str_index('Alice has a cat') == 12


# 152
# index method for str ( parameters )

def str_index_par(any_str):
    return any_str.index('as', 1, 10)


assert str_index_par('Alice has a cat') == 7


# 153
# rfind method for str

def str_rfind(any_str):
    return any_str.find('cat')


assert str_rfind('Alice has a cat') == 12

data = [
    {
        "name": "pawel",
        "city": "krakow",
        "age": 39,
        "hobbies": ["js", "python", "drugs"]
    },
    {
        "name": "joanna",
        "city": "krakow",
        "age": 32,
        "hobbies": ["movies", "books", "food"]
    },
    {
        "name": "igor",
        "city": "wroclaw",
        "age": 31,
        "hobbies": ["anime", "games", "movies"]
    },
    {
        "name": "dawid",
        "city": "wroclaw",
        "age": 43,
        "hobbies": ["film", "music", "bike"]
    },
    {
        "name": "piotr",
        "city": "warszawa",
        "age": 35,
        "hobbies": ['wspinaczka', 'komputery', 'anime']
    },
    {
        "name": "tomek",
        "city": "warszawa",
        "age": 38,
        "hobbies": ["shooting", "sailing", "martial arts"]
    },
    {
        "name": "rafal",
        "city": "warszawa",
        "age": 28,
        "hobbies": ["cars", "IT"]
    },
    {
        "name": "mateusz",
        "city": "wroclaw",
        "age": 30,
        "hobbies": ["bjj", "python", "java"]
    },
    {
        "name": "adrian",
        "city": "dabrowa gornicza",
        "age": 33,
        "hobbies": ["reading", "video games", "chemistry", "physics", "boardgames", "shooting"]
    },
    {
        "name": "cezary",
        "city": "kielce",
        "age": 33,
        "hobbies": ["programming", "sport shooting", "paper models", "and more"],
    },
    {
        "name": "szymon",
        "city": "wroclaw",
        "age": 30,
        "hobbies": ["crypto", "podcasts", "games"]
    },
    {
        'name': 'piotr',
        'city': 'warszawa',
        'age': 50,
        'hobbies': ['python', 'snorkeling', 'traveling']
    },
    {
        "name": "igor",
        "city": "warszawa",
        "age": 34,
        "hobbies": ["golf", "music", "art"]
    },
    {
        "name": "marcin",
        "city": "krakow",
        "age": 40,
        "hobbies": ["python", "ds", "sleep"]
    },
    {
        "name": "kasia",
        "city": "krakow",
        "age": 35,
        "hobbies": ["music"]
    },
    {
        "name": "mateusz",
        "city": "dabrowa gornicza",
        "age": 31,
        "hobbies": ["filmy"]
    }
]


# 154
# write function that return average age of course users

def avg_age_01(data_):
    number_users = 0
    for user in data_:
        number_users += user['age']
    return number_users // len(data_)


assert avg_age_01(data) == 35


# 155, 156, 157
# the same task what # 154 but use the list comprehension

def avg_age_02(persons):
    age_sum = [person['age'] for person in persons]
    return sum(age_sum) // len(persons)


assert avg_age_02(data) == 35


# 158, 159, 160
# the same task what # 155 but use the generator expression
# with lambda and map functions

def avg_age_03(persons):
    return sum(list(map(lambda person: person['age'], persons))) // len(persons)


assert avg_age_03(data) == 35


# 161, 162, 163
# create function that takes list of dictionaries and return
# dict with person and age for the people only from Warsaw , use dict comprehension

def people_from_warsaw(persons):
    return {person['name']: person['age'] for person in persons
            if 'warszawa'.lower() in person['city']}


assert people_from_warsaw(data) == {'piotr': 50, 'tomek': 38, 'rafal': 28, 'igor': 34}


# 164, 165, 166
# write function that return average age of course users only from warsaw

def avg_age_people_from_warsaw_(persons):
    r = {person['name']: person['age'] for person in persons
         if 'warszawa'.lower() in person['city']}
    return sum(r.values()) // len(r)


assert avg_age_people_from_warsaw_(data) == 37


# 167, 168, 169
# the same task what #164 but for the people from out of Warsaw
def avg_age_people_out_warsaw_(persons):
    r = {person['name']: person['age'] for person in persons
         if 'warszawa'.lower() not in person['city']}
    return sum(r.values()) // len(r)


# print(avg_age_people_from_warsaw_(data))
assert avg_age_people_out_warsaw_(data) == 34


# 171, 172, 173
# the same what #161 but for the people from out of Warsaw

def people_out_warsaw(persons):
    return {person['name']: person['age'] for person in persons
            if 'warszawa'.lower() not in person['city']}


# print(people_out_warsaw(data))

assert people_out_warsaw(data) == {'pawel': 39, 'joanna': 32, 'igor': 31, 'dawid': 43, 'mateusz': 31, 'adrian': 33,
                                   'cezary': 33, 'szymon': 30, 'marcin': 40, 'kasia': 35}


# 174, 175, 176
# the same what # 171 but only list of names

def people_out_warsaw_names(persons):
    return [person['name'] for person in persons
            if 'warszawa'.lower() not in person['city']]


# print(people_out_warsaw_names(data))
assert people_out_warsaw_names(data) == ['pawel', 'joanna', 'igor', 'dawid', 'mateusz', 'adrian', 'cezary', 'szymon',
                                         'marcin', 'kasia', 'mateusz']


# 177
# the same task what 167 but traditional method

def avg_age_people_out_warsaw_2(dataset):
    total_age = 0
    counter = 0

    for person in dataset:
        if person['city'].lower() != 'warszawa':
            total_age += person['age']
            counter += 1
    return total_age // counter


assert avg_age_people_out_warsaw_2(data) == 34


# 178, 179, 180
# using tuple comprehension create function that return
# people's names from warsaw

def give_back_names_people_from_waw(dataset):
    return tuple(names['name'] for names in dataset if names['city'].lower() == 'warszawa')


# print(give_back_names_people_from_waw(data))
assert give_back_names_people_from_waw(data) == ('piotr', 'tomek', 'rafal', 'piotr', 'igor')


# 181
# the same what 180 but traditional method function has to return list

def give_back_names_people_from_waw_2(dataset):
    names = []
    for person in dataset:
        if person['city'].lower() == 'warszawa':
            names.append(person['name'])
    return names


# print(give_back_names_people_from_waw_2(data))
assert give_back_names_people_from_waw_2(data) == ['piotr', 'tomek', 'rafal', 'piotr', 'igor']


# 182, 183, 184
# the same what 181 but use lambda and map functions

def give_back_names_people_from_waw_3(people):
    return list(map(
        lambda person: person['name'],
        filter(lambda person: person['city'].lower() == 'warszawa', people)
    ))


# print(give_back_names_people_from_waw_3(data))
assert give_back_names_people_from_waw_3(data) == ['piotr', 'tomek', 'rafal', 'piotr', 'igor']


# 185, 186, 187
# create function that return set of cities without repetition
# use set comprehension

def cities_without_repetition(dataset):
    return set(city['city'] for city in dataset)


# print(cities_without_repetition(data))
assert cities_without_repetition(data) == {'krakow', 'dabrowa gornicza', 'wroclaw', 'kielce', 'warszawa'}


# 188
# the same task what # 185 but use traditional method and return list

def cities_without_repetition_2(dataset):
    cities = []
    for city in dataset:
        cities.append(city['city'])
    return list(set(cities))


print(cities_without_repetition_2(data))


# assert cities_without_repetition_2(data) == ['krakow', 'dabrowa gornicza', 'warszawa', 'kielce', 'wroclaw']

# 189, 190, 191
# the same what 185 bud use the lambda and map functions

def cities_without_repetition_3(dataset):
    return set(map(lambda city: city['city'], dataset))


assert cities_without_repetition_3(data) == {'wroclaw', 'krakow', 'warszawa', 'kielce', 'dabrowa gornicza'}


# 192, 193, 194
# write a function that check if someone is a geezer and return bool value True or False
# geezer is a person above 35

def check_age_people(dataset):
    return bool(len([age['name'] for age in dataset if age['age'] > 35]) > 1)


assert check_age_people(data) == True


# 195, 196, 197
# the same what # 192 but function has to return str with info about amount geezers in the group

def check_age_people_2(dataset):
    age_list = [age['name'] for age in dataset if age['age'] > 35]
    return f'There are {len(age_list)} people who are older than 35 years' if len(
        age_list) >= 1 else f'There is no elderly people in the group'


# print(check_age_people_2(data))
assert check_age_people_2(data) == 'There are 5 people who are older than 35 years'


# 198
# the same what # 192 but in traditional method

def check_age_people_3(dataset):
    age_list = []
    for age in dataset:
        if age['age'] > 35:
            age_list.append(age['name'])
    return True if len(age_list) > 1 else False


assert check_age_people_3(data) == True


# 199, 200, 201
# the same what # 192 but use map , lambda and filter

def check_age_people_4(dataset):
    ages = list(map
                (lambda person: person['name'],
                 filter(lambda person_age: person_age['age'] > 35, dataset)
                 ))
    return len(ages) > 1


assert check_age_people_4(data) == True


# 202, 203, 204
# write a function that takes str and capitalize every second letter for that string

def change_second_letter(any_str):
    return ''.join(
        char.upper() if index % 2 == 0 else char
        for index, char in enumerate(any_str)
    )


# print(change_second_letter('ala ma kota'))
assert change_second_letter('ala ma kota') == 'AlA Ma kOtA'


# 205, 206, 207
# write a function that takes list contains string and returns list of tuples

def create_tuple_from_list_of_string(list_of_strings):
    return [(index, item) for index, item in enumerate(list_of_strings)]


# print(create_tuple_from_list_of_string(['home', 'dog', 'funeral', 'dental']))
assert create_tuple_from_list_of_string(['home', 'dog', 'funeral', 'dental']) == [(0, 'home'), (1, 'dog'),
                                                                                  (2, 'funeral'), (3, 'dental')]


# 208, 209, 210
# the same what # 205 but only for odd indexes

def create_tuple_from_list_of_string_odd(list_of_strings):
    return [(index, item) for index, item in enumerate(list_of_strings) if index & 1]


# print(create_tuple_from_list_of_string_odd(['home', 'dog', 'funeral', 'dental']))
assert create_tuple_from_list_of_string_odd(['home', 'dog', 'funeral', 'dental']) == [(1, 'dog'), (3, 'dental')]


# 211, 212, 213
# the same what # 205 but only for even indexes

def create_tuple_from_list_of_string_even(list_of_strings):
    return [(index, item) for index, item in enumerate(list_of_strings) if not index & 1]


# print(create_tuple_from_list_of_string_even(['home', 'dog', 'funeral', 'dental', 'word', 'war']))
assert create_tuple_from_list_of_string_even(['home', 'dog', 'funeral', 'dental', 'word', 'war']) == [(0, 'home'),
                                                                                                      (2, 'funeral'),
                                                                                                      (4, 'word')]


# 214, 215, 216
# the same what # 205 but every third index

def create_tuple_from_list_of_string_every_3th(list_of_strings):
    return [(index, item) for index, item in enumerate(list_of_strings) if index % 3 == 0]


# print(create_tuple_from_list_of_string_every_3th(['home', 'dog', 'funeral', 'dental', 'word', 'war', '6', '7', '8', '9']))
assert (create_tuple_from_list_of_string_every_3th(
    ['home', 'dog', 'funeral', 'dental', 'word', 'war', '6', '7', '8', '9'])) == [(0, 'home'), (3, 'dental'), (6, '6'),
                                                                                  (9, '9')]


# 217, 218, 219
# the same what # 214 all indexes except every third index

def create_tuple_from_list_of_string_except_every_3th(list_of_strings):
    return [(index, item) for index, item in enumerate(list_of_strings) if index % 3 != 0]


# print(create_tuple_from_list_of_string_except_every_3th(['home', 'dog', 'funeral', 'dental', 'word', 'war', '6', '7', '8', '9']))
assert (create_tuple_from_list_of_string_except_every_3th(
    ['home', 'dog', 'funeral', 'dental', 'word', 'war', '6', '7', '8', '9'])) == [(1, 'dog'), (2, 'funeral'),
                                                                                  (4, 'word'), (5, 'war'), (7, '7'),
                                                                                  (8, '8')]


# 220, 221, 222
# write a function that takes list and return dictionary with odd keys

def create_dict_from_list_of_string_odd(list_of_strings):
    return {index: item for index, item in enumerate(list_of_strings) if index & 1}


# print(create_dict_from_list_of_string_odd(['home', 'dog', 'funeral', 'dental', 'word', 'war', '6', '7', '8', '9']))
assert create_dict_from_list_of_string_odd(['home', 'dog', 'funeral', 'dental', 'word', 'war', '6', '7', '8', '9']) == {
    1: 'dog', 3: 'dental', 5: 'war', 7: '7', 9: '9'}


# 223, 224, 225
# the same what # 220 but for even keys

def create_dict_from_list_of_string_even(list_of_strings):
    return {index: item for index, item in enumerate(list_of_strings) if not index & 1}


# print(create_dict_from_list_of_string_even(['home', 'dog', 'funeral', 'dental', 'word', 'war', '6', '7', '8', '9']))
assert create_dict_from_list_of_string_even(
    ['home', 'dog', 'funeral', 'dental', 'word', 'war', '6', '7', '8', '9']) == {0: 'home', 2: 'funeral', 4: 'word',
                                                                                 6: '6', 8: '8'}


# 226, 227, 228
# the same what # 225 but for every 4th keys

def create_dict_from_list_every_4th_key(list_of_strings):
    return {index: item for index, item in enumerate(list_of_strings) if not index % 4}


# print(create_dict_from_list_every_4th_key(['home', 'dog', 'funeral', 'dental', 'word', 'war', '6', '7', '8', '9']))
assert create_dict_from_list_every_4th_key(['home', 'dog', 'funeral', 'dental', 'word', 'war', '6', '7', '8', '9']) == {
    0: 'home', 4: 'word', 8: '8'}


# 229, 230, 231
# the same what # 226 but not for every 4th keys

def create_dict_from_list_not_every_4th_key(list_of_strings):
    return {index: item for index, item in enumerate(list_of_strings) if index % 4 != 0}


# print(create_dict_from_list_not_every_4th_key(['home', 'dog', 'funeral', 'dental', 'word', 'war', '6', '7', '8', '9']))
assert create_dict_from_list_not_every_4th_key(
    ['home', 'dog', 'funeral', 'dental', 'word', 'war', '6', '7', '8', '9']) == {1: 'dog', 2: 'funeral', 3: 'dental',
                                                                                 5: 'war', 6: '6', 7: '7', 9: '9'}


# 232, 233, 234
# create function that change every second letter in the sentence

def every_second_letter(any_str):
    return ''.join(letter.lower() if index % 2 else letter.upper() for index, letter in enumerate(any_str))


# print(every_second_letter('home is roomy and i would like to buy it'))
assert every_second_letter('home is roomy and i would like to buy it') == 'HoMe iS RoOmY AnD I WoUlD LiKe tO BuY It'


# 235, 236, 237
# the same what 232 but opposite action , means start from small letter

def every_second_letter_first_small(any_str):
    return ''.join(letter.lower() if not index % 2 else letter.upper() for index, letter in enumerate(any_str))


# print(every_second_letter_first_small('home is roomy and i would like to buy it'))
assert every_second_letter_first_small(
    'home is roomy and i would like to buy it') == 'hOmE Is rOoMy aNd i wOuLd lIkE To bUy iT'


# 238, 239, 240
# write function uses closure that outer function takes str and number
# inner function should apply title and after that swapcase method and multiply by number from outer function

def hello(name, a):
    def inner():
        return f'Hello {(" " + name.title().swapcase()) * a}'

    return inner


x_fn = hello('Love is in the air', 3)
# print(x_fn())

assert x_fn() == 'Hello  lOVE iS iN tHE aIR lOVE iS iN tHE aIR lOVE iS iN tHE aIR'


# 241, 242, 243
# create a decorator that change str by swapcase method in decorated function

def swapcase(fn):
    def inner(name):
        return fn(name.swapcase())

    return inner


@swapcase
def hello(name):
    return f'Hello {name}'


# print(hello('JoHn'))
assert hello('JoHn') == 'Hello jOhN'


# 244, 245, 246
# create a decorator that multiply result of decorated function by value

def multiply(fn):
    def inner(*args, c):
        return fn(*args) * c

    return inner


@multiply
def add(a, b):
    return a + b


result = add(1, 2, c=4)
# print(result)
assert result == 12


# 247, 248, 249
# create a decorator that change str by title method in decorated function

def title(fn):
    def inner(sentence):
        return fn(sentence.title())

    return inner


@title
def i_would_have_said(sentence):
    return f'I would have said : {sentence}'


# print(i_would_have_said('My home is far from here'))
assert i_would_have_said('My home is far from here') == 'I would have said : My Home Is Far From Here'


# 251, 252, 253
# create a decorator that change str by replace method in decorated function change 'e' on '$'

def replace(fn):
    def inner(sentence):
        return fn(sentence.replace('e', '$'))

    return inner


@replace
def i_would_have_said(sentence):
    return f'I would have said : {sentence}'


# print(i_would_have_said('My home is far from here'))
assert i_would_have_said('My home is far from here') == 'I would have said : My hom$ is far from h$r$'


# 254, 255, 256
# create a decorator that change every second letter in str by upper method in decorated function

def replace_sec_letter(fn):
    def inner(sentence):
        return fn(''.join(char.upper() if index % 2 == 0 else char for index, char in enumerate(sentence)))

    return inner


@replace_sec_letter
def i_would_have_said(sentence):
    return f'I would have said : {sentence}'


# print(i_would_have_said('My home is far from here'))
assert i_would_have_said('My home is far from here') == 'I would have said : My hOmE Is fAr fRoM HeRe'


# 257, 258, 259
# create a decorator that change every 4th letter in str by upper method in decorated function

def replace_4th_letter(fn):
    def inner(sentence):
        return fn(''.join(letter.upper() if index % 4 == 0 else letter for index, letter in enumerate(sentence)))

    return inner


@replace_4th_letter
def i_would_have_said(sentence):
    return f'I would have said : {sentence}'


# print(i_would_have_said('My home is far from here'))
assert i_would_have_said('My home is far from here') == 'I would have said : My hOme Is fAr fRom Here'


# 260, 261, 262
# the same what # 257 byt opposite action

def replace_4th_letter_2(fn):
    def inner(sentence):
        return fn(''.join(letter.upper() if index % 4 != 0 else letter for index, letter in enumerate(sentence)))

    return inner


@replace_4th_letter_2
def i_would_have_said(sentence):
    return f'I would have said : {sentence}'


# print(i_would_have_said('My home is far from here'))
assert i_would_have_said('My home is far from here') == 'I would have said : MY HoME iS FaR FrOM hERE'


# 263, 264, 265
# create a decorator that count exponentiation result of decorated function

def exponentiation(fn):
    def inner(*args, c):
        return fn(*args) ** c

    return inner


@exponentiation
def add(a, b):
    return a // b


result = add(2, 1, c=4)
# print(result)
assert result == 16


# 266, 267, 268
# Write a decorator that replace white spaces from the str and count all len of that str and change
# 'I would have said' on 'The len of str is'

def count_len(fn):
    def inner(sentence):
        _ = fn(sentence)
        return f'The len of str is : {len(sentence.replace(' ', ''))}'

    return inner


@count_len
def i_would_have_said(sentence):
    return f'I would have said : {sentence}'


# print(i_would_have_said('My home is far from here'))
assert i_would_have_said('My home is far from here') == 'The len of str is : 19'


# 269, 270, 271
# create a decorator that count len of the returned list from decorated function

def len_list(fn):
    def inner(a):
        result = fn(a)
        return len(result[:6])

    return inner


@len_list
def create_list(a):
    l = list(range(a))
    return l


result = create_list(10)
# print(result)
assert result == 6


# 272, 273, 274
# write a function that add number to returned list from decorated function

def add_number_to_list(number):
    def decorator(fn):
        def inner(a):
            result = fn(a)
            result.append(number)
            return result

        return inner

    return decorator


@add_number_to_list(200)
def create_list(a):
    l = list(range(a))
    return l


result = create_list(10)
# print(result)
assert result == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 200]


# 275, 276, 277
# write a function that remove last number of list from decorated function

def remove_number_from_list(fn):
    def inner(a):
        result = fn(a)
        result.pop()
        return result

    return inner


@remove_number_from_list
def create_list(a):
    l = list(range(a))
    return l


result = create_list(10)
# print(result)
assert result == [0, 1, 2, 3, 4, 5, 6, 7, 8]


# 278, 279, 280
# create a decorator that count len of the returned list from decorated function

def sum_list(fn):
    def inner(a):
        result = fn(a)
        return sum(result)

    return inner


@sum_list
def create_list(a):
    l = list(range(a))
    return l


result = create_list(10)
# print(result)
assert result == 45


# 281, 282, 283
# create a decorator that count average of list

def avg_list(fn):
    def inner(a):
        result = fn(a)
        return sum(result) / len(result)

    return inner


@avg_list
def create_list(a):
    l = list(range(a))
    return l


result = create_list(10)
# print(result)
assert result == 4.5


# 284, 285, 286
# create a decorator that multiply return any_funct by number

def multi_num(c):
    def decorator(fn):
        def inner(*args, **kwargs):
            result = fn(*args, **kwargs)
            return result * c

        return inner

    return decorator


@multi_num(5)
def any_funct(a, b):
    return a * b


d = any_funct(10, 20)
# print(d)
assert any_funct(10, 20) == 1000


# 287, 288, 289
# create a decorator that gives possibility to create basic mathematical operation on the return any_funct
# using number and operation like a parameter of decorator

def multi_num(c, operation):
    def decorator(fn):
        def inner(*args, **kwargs):
            result = fn(*args, **kwargs)
            if operation == 'multiply':
                return result * c
            elif operation == 'add':
                return result + c
            elif operation == 'subtract':
                return result - c
            elif operation == 'divide' and c != 0:
                return result / c
            else:
                return result

        return inner

    return decorator


@multi_num(50, operation='multiply')
def any_funct(a, b):
    return a + b


d_1 = any_funct(10, 20)
# print(d_1)

assert any_funct(10, 20) == 1500


# 290, 291, 292
# create function that use closure outer fn takes exponent inner takes base of power
# exponent and base of power will be the same number

def power_n(exponent):
    def inner(base):
        return base ** exponent

    return inner


power_2 = power_n(2)
# print(power_2(4))
assert power_2(4) == 16


# 293, 294, 295
# create a decorators that change return from bye function on html code like a str and capitalize first letter of name

def capitalize(function):
    def inner(name):
        return function(name.capitalize())

    return inner


def gen_html(fn):
    def inner(name):
        result = fn(f'<b>{name}<b/>')
        return f'<h1>{result}</h1>'

    return inner


@capitalize
@gen_html
def bye(name):
    return f"Bye {name}"


# print(bye("happy holidays"))
assert bye("happy holidays") == '<h1>Bye <b>Happy holidays<b/></h1>'


# 296
# write function that convert kilometers to miles

def km_to_miles(km):
    return f'{km} km is {km * 0.621371:.2f} miles'


# print(km_to_miles(1000))
assert km_to_miles(1000) == '1000 km is 621.37 miles'


# 297
# write function that convert miles to kilometers

def miles_to_km(miles):
    return f'{miles} miles are {miles * 1.60934:.2f} kilometers'


# print(miles_to_km(1000))
assert miles_to_km(1000) == '1000 miles are 1609.34 kilometers'


# 298
# write function that convert meters to centimeters

def m_to_cm(m):
    return f'{m} meters are {m * 100:.2f} centimeters'


# print(m_to_cm(1000))
assert m_to_cm(1000) == '1000 meters are 100000.00 centimeters'


# 299
# count centimeters to meters
def cm_to_m(cm):
    return f'{cm} centimeters are {cm / 100:.2f} meters'


assert cm_to_m(1000) == '1000 centimeters are 10.00 meters'


# 300
# count meters to inches
def m_to_inches(m):
    return f'{m} meters are {m * 39.3701:.2f} inches'


# print(m_to_inches(1000))
assert m_to_inches(1000) == '1000 meters are 39370.10 inches'


# 301
# count inches to meters
def inches_to_m(inches):
    return f'{inches} inches are {inches / 39.3701:.2f} inches'


# print(inches_to_m(1000))
assert inches_to_m(1000) == '1000 inches are 25.40 inches'


# 302
# count inches to feet
def inches_to_feet(inches):
    return f'{inches} inches are {inches / 12:.2f} feet'


# print(inches_to_feet(1000))
assert inches_to_feet(1000) == '1000 inches are 83.33 feet'


# 303
# count Square kilometers to hectares
def sq_km_to_hectares(sq_km):
    return f'{sq_km} Square kilometers are {sq_km * 100:.2f} hectares'


# print(sq_km_to_hectares(1000))
assert sq_km_to_hectares(1000) == '1000 Square kilometers are 100000.00 hectares'


# 304
# count Square meters to square centimeters
def sq_m_to_sq_cm(sq_m):
    return f'{sq_m} Square meters are {sq_m * 10000:.2f} square centimeters'


# print(sq_m_to_sq_cm(1000))
assert sq_m_to_sq_cm(1000) == '1000 Square meters are 10000000.00 square centimeters'


# 305
# count Liters to milliliters
def lit_to_ml(lit):
    return f'{lit} Liters are {lit * 1000:.2f} milliliters'


# print(lit_to_ml(1000))
assert lit_to_ml(1000) == '1000 Liters are 1000000.00 milliliters'


# 306
# count Gallons (US) to liters
def gal_to_liters(g):
    return f'{g} gallons are {g * 3.78541:.2f} liters'


# print(gal_to_liters(1000))
assert gal_to_liters(1000) == '1000 gallons are 3785.41 liters'


# 307
# count Liters per cubic inch
def liters_to_cub_inches(liters):
    return f'{liters} Liters are {liters * 1000:.2f} cubic inches'


# print(liters_to_cub_inches(1000))
assert liters_to_cub_inches(1000) == '1000 Liters are 1000000.00 cubic inches'


# 308
# count Kilograms to pounds
def kg_to_pounds(kg):
    return f'{kg} Kilograms are {kg * 2.20462:.2f} pounds'


# print(kg_to_pounds(1000))
assert kg_to_pounds(1000) == '1000 Kilograms are 2204.62 pounds'


# 309
# count Pounds to kilograms
def pounds_to_kilograms(pounds):
    return f'{pounds} Pounds are {pounds / 2.20462:.2f} kilograms'


# print(pounds_to_kilograms(1000))
assert pounds_to_kilograms(1000) == '1000 Pounds are 453.59 kilograms'


# 310
# count Grams to ounces
def gr_to_ounces(gr):
    return f'{gr} Grams are {gr / 28.3495:.2f} ounces'


# print(gr_to_ounces(1000))
assert gr_to_ounces(1000) == '1000 Grams are 35.27 ounces'


# 311
# count Ounces to grams
def ounces_to_grams(ounces):
    return f'{ounces} Ounces are {ounces * 28.3495:.2f} grams'


# print(ounces_to_grams(1000))
assert ounces_to_grams(1000) == '1000 Ounces are 28349.50 grams'


# 312
# count hours to minutes
def hours_to_seconds(hours):
    return f'{hours} Hours are {hours * 60:.2f} minutes'


# print(hours_to_seconds(1000))
assert hours_to_seconds(1000) == '1000 Hours are 60000.00 minutes'


# 313
# count Minutes to seconds
def minutes_to_seconds(minutes):
    return f'{minutes} Minutes are {minutes * 60:.2f} seconds'


# print(minutes_to_seconds(1000))
assert minutes_to_seconds(1000) == '1000 Minutes are 60000.00 seconds'


# 314
# count Kilometers per hour to meters per second
def km_per_h_to_m_per_s(km_per_h):
    return f'{km_per_h} Kilometers per hour are {km_per_h / 3.6:.2f} meters per second'


# print(km_per_h_to_m_per_s(1000))
assert km_per_h_to_m_per_s(1000) == '1000 Kilometers per hour are 277.78 meters per second'


# 315
# count Meters per second to kilometers per hour
def m_per_s_to_km_per_h(m_per_s):
    return f'{m_per_s} Meters per second are {m_per_s * 3.6:.2f} kilometers per hour'


# print(m_per_s_to_km_per_h(1000))
assert m_per_s_to_km_per_h(1000) == '1000 Meters per second are 3600.00 kilometers per hour'


# 316
# count Temperature Celsius to Fahrenheit
def temp_cel_to_fah(temp_c):
    return f'{temp_c} degrees Celsius are {(temp_c * (9 / 5)) + 32} Fahrenheits'


# print(temp_cel_to_fah(100))
assert temp_cel_to_fah(100) == '100 degrees Celsius are 212.0 Fahrenheits'


# 317
# count Temperature Fahrenheit to degrees Celsius
def fahrenheit_to_celsius(fah):
    return f'{fah} Fahrenheits are {(fah - 32) * (5 / 9):.2f} degrees Celsius'


# print(fahrenheit_to_celsius(100))
assert fahrenheit_to_celsius(100) == '100 Fahrenheits are 37.78 degrees Celsius'


# 318
# count Celsius to Kelvin
def cel_to_kel(c):
    return f'{c} Celsius are {c + 273:.2f} Kelvins'


# print(cel_to_kel(100))
assert cel_to_kel(100) == '100 Celsius are 373.00 Kelvins'


# 319
# count Kelvin to Celsius

def kelvin_to_celsius(kelvin):
    return f'{kelvin} kelvins are {kelvin - 273.15:.2f} degrees Celsius'


# print(kelvin_to_celsius(100))
assert kelvin_to_celsius(100) == '100 kelvins are -173.15 degrees Celsius'


# 320
# count Kilowatt hours to joules
def kwh_to_joules(kwh):
    return f'{kwh} Kilowatt hours are {kwh * 3600000:.2f} joules'


# print(kwh_to_joules(1000))
assert kwh_to_joules(1000) == '1000 Kilowatt hours are 3600000000.00 joules'

# 321
# create function that use decimal from python library during adding two numbers

from decimal import Decimal


def add_decimal(num_1, num_2):
    return Decimal(f'{num_1}') + Decimal(str(num_2))


# print(add_decimal(0.25, 0.36))
assert add_decimal(0.25, 0.36) == Decimal('0.61')


# 322
# create function that use decimal from python library during multiply two numbers

def mult_decimal(num_1, num_2):
    return Decimal(f'{num_1}') * Decimal(str(num_2))


# print(mult_decimal(0.21, 0.42))
assert mult_decimal(0.21, 0.42) == Decimal('0.0882')


# 323, 324, 325
# using list comprehension create function that takes list of list and n and return the same list multiply by n

def mult_list_of_list_1(any_list, n):
    return [[x * n, y * n] for x, y in any_list]


# print(mult_list_of_list_1([[1, 2], [3, 4], [5, 6]], 5))
assert mult_list_of_list_1([[1, 2], [3, 4], [5, 6]], 5) == [[5, 10], [15, 20], [25, 30]]


# 326, 327, 328
# the same what # 323 but different way

def mult_list_of_list_2(any_list, n):
    return [[digit * n for digit in digits] for digits in any_list]


# print(mult_list_of_list_2([[1, 2], [3, 4], [5, 6]], 5))
assert mult_list_of_list_2([[1, 2], [3, 4], [5, 6]], 5) == [[5, 10], [15, 20], [25, 30]]


# 329, 330, 331
# create function that return seating plan in the plane in the set 25 rows and six seats in each row
# zero row doesn't exist and should be display like a None

def seating_plan(letters, rows):
    return [None] + [{letter: None for letter in letters} for _ in rows]


# print(seating_plan('ABCDEF', range(1, 25)))
assert seating_plan('ABCDEF', range(1, 25)) == [None,
                                                {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None},
                                                {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None},
                                                {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None},
                                                {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None},
                                                {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None},
                                                {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None},
                                                {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None},
                                                {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None},
                                                {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None},
                                                {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None},
                                                {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None},
                                                {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None},
                                                {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None},
                                                {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None},
                                                {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None},
                                                {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None},
                                                {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None},
                                                {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None},
                                                {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None},
                                                {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None},
                                                {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None},
                                                {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None},
                                                {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None},
                                                {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None}]


# 332, 333, 334
# using list comprehension and range inside create function that takes any str and number and return list of indexes with that string
# number of str in that list has to be the same what n

def lst_range_str(any_str, n):
    return [any_str for t in range(n)]


# print(lst_range_str('I will not swearing',6))
assert lst_range_str('I will not swearing', 6) == ['I will not swearing', 'I will not swearing', 'I will not swearing',
                                                   'I will not swearing', 'I will not swearing', 'I will not swearing']

# 335, 336, 337
# using reduce from functools library count sum of list indexes created inside by generation expression
# index should be the power of the index created from the list
from functools import reduce


def reduce_list(any_list):
    return reduce(lambda acc, ce: acc + ce, (x ** x for x in any_list))


# print(reduce_list([1, 2, 3, 4, 5]))
assert reduce_list([1, 2, 3, 4, 5]) == 3413


# 338
# sum of list implementation

def sum_implementation(any_list):
    total = 0
    for i in range(len(any_list)):
        total += any_list[i]
    return total


# print(sum_implementation([1, 2, 3, 4, 5]))
assert sum_implementation([1, 2, 3, 4, 5]) == 15


# 339
# the same what # 338 but differt way

def sum_of_consecutive_elements(any_list):
    total = 0
    for element in any_list:
        total += element
    return total


# print(sum_of_consecutive_elements([1, 2, 3, 4, 5]))
assert sum_of_consecutive_elements([1, 2, 3, 4, 5]) == 15


# 340
# The cumulative_sum function computes the cumulative sum of
# the elements of a list, i.e., at each position it creates the sum of all the elements from the beginning
# of the list to the current element. The result is returned as a list with consecutive sums.

def cumulative_sum(any_list):
    total = 0
    score = []
    for element in any_list:
        total += element
        score.append(total)
    return score


# print(cumulative_sum([1, 2, 3, 4, 5]))
assert cumulative_sum([1, 2, 3, 4, 5]) == [1, 3, 6, 10, 15]


# 341, 342, 343
# create function that count amount of unique hobbies from data collection

def amount_unique_hobbies(collection):
    return len({x for y in collection for x in y['hobbies']})


# print(amount_unique_hobbies(data))
assert amount_unique_hobbies(data) == 38


# 344, 345, 346
# the same what # 341 but use lambda and reduce

def count_unique_hobbies_2(people):
    return len(reduce(lambda acc, person: acc | set(person['hobbies']), people, set()))


# print(count_unique_hobbies_2(data))
assert count_unique_hobbies_2(data) == 38


# 347, 348, 349
# create function hash that return list with 2 first sign from values of data collection ( list of dictionaries )

def create_hash(people):
    hashes = []
    for person in people:
        text = ''

        for value in person.values():
            if isinstance(value, list):
                for item in value:
                    text += item[:2]

            else:
                text += str(value)[:2]

        hashes.append(text.lower())
    return hashes


# print(create_hash(data))
assert create_hash(data) == ['pakr39jspydr', 'jokr32mobofo', 'igwr31angamo', 'dawr43fimubi', 'piwa35wskoan',
                             'towa38shsama', 'rawa28cait',
                             'mawr30bjpyja', 'adda33revichphbosh', 'ceki33prsppaan', 'szwr30crpoga', 'piwa50pysntr',
                             'igwa34gomuar',
                             'makr40pydssl', 'kakr35mu', 'mada31fi']


# 350, 351, 352
# create function that takes data and check if there is one person under age 20 , return should be bool value

def is_young_people(people):
    return bool([person for person in people if person['age'] < 20])


# print(is_young_people(data))
assert is_young_people(data) == False


# 353, 354, 355
# the same what # but using map and lambda

def is_young_people_2(people):
    return any(map(lambda person: person['age'] < 20, people))


assert is_young_people_2(data) == False


# 356, 357, 358

def set_unique_hobbies(any_data):
    return {hobby for person in any_data for hobby in person['hobbies']}


# print(set_unique_hobbies(data))
assert set_unique_hobbies(data) == {'golf', 'video games', 'js', 'bjj', 'and more', 'wspinaczka', 'IT',
                                    'boardgames', 'chemistry', 'sport shooting', 'python', 'food', 'art', 'filmy',
                                    'bike', 'cars', 'music', 'shooting', 'physics', 'komputery', 'books', 'podcasts',
                                    'drugs', 'games', 'paper models', 'sailing', 'traveling', 'programming',
                                    'martial arts', 'ds', 'java', 'sleep', 'film', 'snorkeling', 'anime',
                                    'reading', 'crypto', 'movies'}


# 359, 360, 361
# the same what # 356 but function has to use enumerate and return dictionary

def dict_unique_hobbies(any_data):
    set_h = {hobby for person in any_data for hobby in person['hobbies']}
    sorted_hobbies = sorted(set_h)
    return {key: value for key, value in enumerate(sorted_hobbies)}


# print(dict_unique_hobbies(data))
assert dict_unique_hobbies(data) == {0: 'IT', 1: 'and more', 2: 'anime', 3: 'art', 4: 'bike', 5: 'bjj', 6: 'boardgames',
                                     7: 'books', 8: 'cars', 9: 'chemistry', 10: 'crypto', 11: 'drugs', 12: 'ds',
                                     13: 'film', 14: 'filmy', 15: 'food', 16: 'games', 17: 'golf', 18: 'java',
                                     19: 'js', 20: 'komputery', 21: 'martial arts', 22: 'movies',
                                     23: 'music', 24: 'paper models', 25: 'physics', 26: 'podcasts',
                                     27: 'programming', 28: 'python', 29: 'reading', 30: 'sailing',
                                     31: 'shooting', 32: 'sleep', 33: 'snorkeling', 34: 'sport shooting',
                                     35: 'traveling', 36: 'video games', 37: 'wspinaczka'}


# 362, 363, 364
# create function that takes list and return list only for the even indexes use index method

def list_even_indexes(any_list: list[int]) -> list[int]:
    return [i for i in any_list if not any_list.index(i) % 2]


# print(list_even_indexes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
assert list_even_indexes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 3, 5, 7, 9]


# 365, 366, 367
# corrected function from # 362 use enumerate function

def list_even_indexes_2(any_list: list[int]) -> list[int]:
    return [value for index, value in enumerate(any_list) if index % 2 == 0]


# print(list_even_indexes_2([10, 30, 10, 10, 100, 80, 10, 10, 10, 10]))
assert list_even_indexes_2([10, 30, 10, 10, 100, 80, 10, 10, 10, 10]) == [10, 10, 100, 10, 10]


# 368, 369, 370
# using list comprehension and enumerate method return list of tuples when value for index is 'home'

def list_of_tuples(any_lst: list[object]) -> list[tuple]:
    return [(index, value) for index, value in enumerate(any_lst) if value == 'home']


# print(list_of_tuples([1, 2, 3, 'home', 5, 6, 'home', 7,'home']))
assert list_of_tuples([1, 2, 3, 'home', 5, 6, 'home', 7, 'home']) == [(3, 'home'), (6, 'home'), (8, 'home')]


# 371, 372, 373
# the same what # 368 but function should return only list of indexes for value 'home'

def list_of_indexes(any_lst: list[object]) -> list[object]:
    return [index for index, value in enumerate(any_lst) if value == 'home']


# print(list_of_indexes([1, 2, 3, 'home', 5, 6, 'home', 7,'home']))
assert list_of_indexes([1, 2, 3, 'home', 5, 6, 'home', 7, 'home']) == [3, 6, 8]


# 374, 375, 376
# the same what # 371 but function should return only list with word 'home'

def list_of_values(any_lst: list[object]) -> list[object]:
    return [value for index, value in enumerate(any_lst) if value == 'home']


# print(list_of_values([1, 2, 3, 'home', 5, 6, 'home', 7,'home']))
assert list_of_values([1, 2, 3, 'home', 5, 6, 'home', 7, 'home']) == ['home', 'home', 'home']


# 377, 378, 379
# the same what # 370 but function should return dictionary , keys should be indexes from the list

def list_of_values_to_dict(any_lst: list[object]) -> dict[object, object]:
    return {index: value for index, value in enumerate(any_lst) if value == 'home'}


# print(list_of_values_to_dict([1, 2, 3, 'home', 5, 6, 'home', 7,'home']))
assert list_of_values_to_dict([1, 2, 3, 'home', 5, 6, 'home', 7, 'home']) == {3: 'home', 6: 'home', 8: 'home'}


# 380, 381, 382
# the same what # 377 but swapcase letters in word 'home'

def list_of_values_to_dict_2(any_lst: list[object]) -> dict[object, object]:
    return {index: value.swapcase() for index, value in enumerate(any_lst) if value == 'home'}


assert list_of_values_to_dict_2([1, 2, 3, 'home', 5, 6, 'home', 7, 'home']) == {3: 'HOME', 6: 'HOME', 8: 'HOME'}


# 383, 384, 385
# the same what # 380 but corrected logic in the function swapcase is replaced on title

def list_of_values_to_dict_3(any_lst: list[object]) -> dict[object, object]:
    return {index: value.title() if isinstance(value, str) else value
            for index, value in enumerate(any_lst) if value == 'home'}


assert list_of_values_to_dict_3([1, 2, 3, 'home', 5, 6, 'home', 7, 'home']) == {3: 'Home', 6: 'Home', 8: 'Home'}


# 386, 387, 388
# the same what # 383 value should be two first character by upper the rest in lower letters

def list_of_values_to_dict_4(any_lst: list[object]) -> dict[object, object]:
    return {index: (value.upper()[:2] + value.lower()[2:]) if isinstance(value, str) else value
            for index, value in enumerate(any_lst) if value == 'home'}


assert list_of_values_to_dict_4([1, 2, 3, 'home', 5, 6, 'home', 7, 'home']) == {3: 'HOme', 6: 'HOme', 8: 'HOme'}


# 389, 390, 391
# the same what # 386 but word 'home' should be 'HoMe'

def list_of_values_to_dict_5(any_lst: list[object]) -> dict[object, object]:
    return {
        index: ''.join([value[i].upper() if i % 2 == 0 else value[i].lower() for i in range(len(value))])
        for index, value in enumerate(any_lst)
        if value == 'home'
    }


assert list_of_values_to_dict_5([1, 2, 3, 'home', 5, 6, 'home', 7, 'home']) == {3: 'HoMe', 6: 'HoMe', 8: 'HoMe'}


# 392, 393, 394
# create function that changes every second letter in any str on upper
def every_second_letter_upper(any_str: str) -> str:
    return ''.join([any_str[i].upper() if i % 2 == 0 else any_str[i].lower() for i in range(len(any_str))])


assert (every_second_letter_upper('This project is a simple Python program that simulates a lottery game')
        == 'ThIs pRoJeCt iS A SiMpLe pYtHoN PrOgRaM ThAt sImUlAtEs a lOtTeRy gAmE')


# 395, 396, 397
# the same what 392 but range replace on enumerate method
def every_second_letter_upper_2(any_str: str) -> str:
    return ''.join(item.upper() if not i % 2 else item.lower() for i, item in enumerate(any_str))


# print(every_second_letter_upper_2('This project is a simple Python program that simulates a lottery game'))
assert (every_second_letter_upper_2('This project is a simple Python program that simulates a lottery game')
        == 'ThIs pRoJeCt iS A SiMpLe pYtHoN PrOgRaM ThAt sImUlAtEs a lOtTeRy gAmE')


# 398, 399, 400
# create function that takes tuple and use tuple comprehension and return new tuple when index of element is < 3

def create_tuple_index_(any_tuple: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(i for i in any_tuple if any_tuple.index(i) < 3)


assert create_tuple_index_((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)) == (1, 2, 3)


# 401
# Codewars

# Find the sum of all multiples of n below m
# n and m are natural numbers (positive integers)
# m is excluded from the multiples
#
# Examples
#
# sumMul(2, 9)   ==> 2 + 4 + 6 + 8 = 20
# sumMul(3, 13)  ==> 3 + 6 + 9 + 12 = 30
# sumMul(4, 123) ==> 4 + 8 + 12 + ... = 1860
# sumMul(4, -7)  ==> "INVALID"

def sum_mul(n, m):
    return 'INVALID' if n <= 0 or m <= 0 else sum(range(n, m, n))


assert sum_mul(2, 9) == 20


# 402
# Codewars

# You are given a string containing a sequence of character sequences separated by commas.
# Write a function which returns a new string containing the same character sequences except the first
# and the last ones but this time separated by spaces.
# If the input string is empty or the removal of the first and last items would cause the resulting
# string to be empty, return an empty value (represented as a generic value NULL in the examples below).
# Examples
#
# "1,2,3"      =>  "2"
# "1,2,3,4"    =>  "2 3"
# "1,2,3,4,5"  =>  "2 3 4"
#
# ""     =>  NULL
# "1"    =>  NULL
# "1,2"  =>  NULL

def array(string):
    return None if len(string.split(',')) < 3 else ' '.join(string.split(',')[1:-1])


assert array("1,2,3") == "2"


# 403, 404, 405
# Codewars

# Convert number to reversed array of digits
# Given a random non-negative number, you have to return the digits of this number within an array in reverse order.
# Example(Input => Output):
# 35231 => [1,3,2,5,3]
# 0 => [0]

def digitize(n):
    return list(map(int, str(n)[::-1]))


assert digitize(35231) == [1, 3, 2, 5, 3]


# 406, 407, 408
# the same what 403 but different way

def digitize_2(n):
    return [int(x) for x in str(n)[::-1]]


assert digitize_2(35231) == [1, 3, 2, 5, 3]


# 409
# sort list by surnames

def sorted_surnames_list(any_list):
    return sorted(any_list, key=lambda item: item.split()[-1])


assert (sorted_surnames_list(["Scarlett Johansson", "Leonardo Dicaprio", "Tom Hanks", "Meryl Streep"])
        == ['Leonardo Dicaprio', 'Tom Hanks', 'Scarlett Johansson', 'Meryl Streep'])


# 410
# the same what 409 but different way


def sorted_surnames_list_2(any_list):
    return sorted(any_list, key=lambda item: len(item.split()[-1]))


assert (sorted_surnames_list_2(["Scarlett Johansson", "Leonardo Dicaprio", "Tom Hanks", "Meryl Streep"])
        == ['Tom Hanks', 'Meryl Streep', 'Leonardo Dicaprio', 'Scarlett Johansson'])


# 411
# the same what 409 but different way

def sorted_surnames_list_3(any_list):
    return sorted(any_list, key=lambda item: len(item.split()[-1]), reverse=True)


assert (sorted_surnames_list_3(["Scarlett Johansson", "Leonardo Dicaprio", "Tom Hanks", "Meryl Streep"])
        == ['Scarlett Johansson', 'Leonardo Dicaprio', 'Meryl Streep', 'Tom Hanks'])


# 412
# Codewars

# Write a function that returns a string in which firstname is swapped with last name.
# Example(Input --> Output)
# "john McClane" --> "McClane john"

def name_shuffler(str_):
    x, y = str_.split(' ', 1)
    return f'{y} {x}'


assert name_shuffler("john McClane") == "McClane john"

data_5 = [
    {
        "name": "pawel",
        "age": 39,
        "city": "krakow",
        "hobbies": ["js", "python", "drugs"]
    },
    {
        "name": "kamil",
        "age": 28,
        "city": "gryfino",
        "hobbies": ["js", "python", "godot"]
    },
    {
        "name": "szymon",
        "age": 30,
        "city": "legnica",
        "hobbies": ["crypto", "work", "movies"]
    },
    {
        "name": "mateusz",
        "age": 30,
        "city": "wroclaw",
        "hobbies": ["bjj", "coding", "movies"]
    },
    {
        'name': 'piotr',
        'age': 34,
        'city': 'warszawa',
        'hobbies': ['climbing', 'running', 'python']
    },
    {
        'name': 'dawid',
        'age': 36,
        'city': 'torun',
        'hobbies': ['boardgames', 'football', 'squash']
    },
    {
        "name": "aleksandra",
        "age": 29,
        "city": "poznan",
        "hobbies": ["music", "art", "math"]
    },
    {
        "name": "renata",
        "age": 29,
        "city": "sosnowiec",
        "hobbies": ["photography", "literature", "trips"]
    },
    {
        'name': "lukasz",
        'age': 37,
        'city': 'brwinow',
        'hobbies': ['Cycling', 'Home Beer brewing', 'Learning new things'],
    },
    {
        "name": "bartek",
        "age": 47,
        "city": "warszawa",
        "hobbies": ["games", "music", "movies"]
    },
    {
        "name": "igor",
        "age": 31,
        "city": "wroclaw",
        "hobbies": ["anime", "mangi", "games"]
    },
    {
        "name": "magda",
        "age": 31,
        "city": "torun",
        "hobbies": ["books", "jogging", "plants"]
    },
    {
        "name": "karol",
        "age": 38,
        "city": "warszawa",
        "hobbies": ["sport", "music", "culinary"]
    },
    {
        "name": "pawel",
        "age": 33,
        "city": "poznan",
        "hobbies": ["music", "traveling", "photography"]
    }
]


# 413, 414, 415
# create function that takes list of dictionaries and return numerated strings of names besides index 0
# use generation expression


def numerated_names(data_list):
    return "\n".join([f'{idx}. {person['name'].title()}' for idx, person in enumerate(data_list)][1:])


# print(numerated_names(data_5))
assert numerated_names(data_5) == """1. Kamil
2. Szymon
3. Mateusz
4. Piotr
5. Dawid
6. Aleksandra
7. Renata
8. Lukasz
9. Bartek
10. Igor
11. Magda
12. Karol
13. Pawel"""


# 416, 417, 418
# the same what # 413 but list of names has to be sorted


def numerated_names_sorted(data_list):
    sorted_data = sorted(data_list, key=lambda person: person['name'].lower())

    return '\n'.join([f"{idx + 1}. {person['name'].title()}" for idx, person in enumerate(sorted_data)])


# print(numerated_names_sorted(data_5))
assert numerated_names_sorted(data_5) == """1. Aleksandra
2. Bartek
3. Dawid
4. Igor
5. Kamil
6. Karol
7. Lukasz
8. Magda
9. Mateusz
10. Pawel
11. Pawel
12. Piotr
13. Renata
14. Szymon"""


# 419, 420, 421
# the same what # 413 but list of people who has in their hobbies 'music'

def numerated_names_music(data_list):
    return "\n".join(
        [f'{idx}. {person['name'].title()}' for idx, person in enumerate(data_list) if 'music' in person['hobbies']][
        1:])


# print(numerated_names_music(data_5))
assert numerated_names_music(data_5) == '''9. Bartek
12. Karol
13. Pawel'''


# 422, 423, 424
# create function that takes list of dictionaries and return dict : key - name , value - hobbies only when movies are in hobbies

def dict_name_hobbies_movies(data_list):
    return {person['name']: person['hobbies'] for person in data_list if 'movies' in person['hobbies']}


# print(dict_name_hobbies_movies(data_5))
assert dict_name_hobbies_movies(data_5) == {'szymon': ['crypto', 'work', 'movies'],
                                            'mateusz': ['bjj', 'coding', 'movies'],
                                            'bartek': ['games', 'music', 'movies']}


# 425, 426, 427
# the same what # 422 but function has to return list of tuples second index in tuple should be a list of hobbies

def list_tuples_name_hobbies_movies(data_list):
    return [(person['name'], person['hobbies']) for person in data_list if 'movies' in person['hobbies']]


# print(list_tuples_name_hobbies_movies(data_5))
assert list_tuples_name_hobbies_movies(data_5) == [('szymon', ['crypto', 'work', 'movies']),
                                                   ('mateusz', ['bjj', 'coding', 'movies']),
                                                   ('bartek', ['games', 'music', 'movies'])]


# 428, 429, 430
# create function that takes list of dictionaries nad return numerated names and hobbies for people who have movies in their hobbies

def numerated_names_hobbies_for_movies(data_list):
    list_tuples = [(person['name'], person['hobbies']) for person in data_list if 'movies' in person['hobbies']]

    return '\n'.join([f'{idx}. {pers_hob}' for idx, pers_hob in enumerate(list_tuples)])


# print(numerated_names_hobbies_for_movies(data_5))
assert numerated_names_hobbies_for_movies(data_5) == '''0. ('szymon', ['crypto', 'work', 'movies'])
1. ('mateusz', ['bjj', 'coding', 'movies'])
2. ('bartek', ['games', 'music', 'movies'])'''


# 431, 432, 433
# The same what # 428 but different style of output

def numerated_names_hobbies_for_movies_2(data_list):
    list_tuples = [(person['name'], person['hobbies']) for person in data_list if 'movies' in person['hobbies']]

    return '\n'.join([f'{idx}. {name}: {hobbies}.' for idx, (name, hobbies) in enumerate(list_tuples)])


# print(numerated_names_hobbies_for_movies_2(data_5))
assert numerated_names_hobbies_for_movies_2(data_5) == '''0. szymon: ['crypto', 'work', 'movies'].
1. mateusz: ['bjj', 'coding', 'movies'].
2. bartek: ['games', 'music', 'movies'].'''


# 434, 435, 436


def numerated_names_hobbies_for_movies_2(data_list):
    list_tuples = [(person['name'], person['hobbies']) for person in data_list if 'movies' in person['hobbies']]

    return '\n'.join([f'{idx}. {name}: {', '.join(hobbies)}.' for idx, (name, hobbies) in enumerate(list_tuples)])


# print(numerated_names_hobbies_for_movies_2(data_5))
assert numerated_names_hobbies_for_movies_2(data_5) == '''0. szymon: crypto, work, movies.
1. mateusz: bjj, coding, movies.
2. bartek: games, music, movies.'''


# 437, 438, 439
# create function that takes list of dictionaries and return dictionary key: name value: city for people over or equal 34 years old


def dict_name_city_age_over_34(data_list):
    return {person['name']: person['city'] for person in data_list if person['age'] >= 34}


# print(sth(data_5))
assert dict_name_city_age_over_34(data_5) == {'pawel': 'krakow', 'piotr': 'warszawa', 'dawid': 'torun',
                                              'lukasz': 'brwinow', 'bartek': 'warszawa', 'karol': 'warszawa'}


# 440, 441, 442


def str_name_city_age_over_34(data_list):
    list_tuples = [(person['name'].title(), person['age'], person['city'].title()) for person in data_list if
                   person['age'] >= 34]
    # return list_tuples
    return '\n'.join([f'{idx}. {name}: {age}: {city}.' for idx, (name, age, city) in enumerate(list_tuples)])


# print(str_name_city_age_over_34(data_5))
assert str_name_city_age_over_34(data_5) == '''0. Pawel: 39: Krakow.
1. Piotr: 34: Warszawa.
2. Dawid: 36: Torun.
3. Lukasz: 37: Brwinow.
4. Bartek: 47: Warszawa.
5. Karol: 38: Warszawa.'''

expowiska = [
    {
        "name": "Dragon Lair",
        "monsters": [
            {
                "name": "Dragon",
                "hp": 1000,
                "exp": 700,
                "count_monster_on_spawn": 10,
                "loot": [
                    {"item_name": "Dragon Ham", "npc_value": 50},
                    {"item_name": "Gold Coin", "npc_value": 1},
                    {"item_name": "Green Dragon Scale", "npc_value": 100},
                    {"item_name": "Dragonbone Staff", "npc_value": 15000},
                    {"item_name": "Strong Health Potion", "npc_value": 100},
                    {"item_name": "Dragon Shield", "npc_value": 4000},
                    {"item_name": "Life Crystal", "npc_value": 50},
                    {"item_name": "Small Diamond", "npc_value": 300}
                ]
            },
            {
                "name": "Dragon Hatchling",
                "hp": 300,
                "exp": 200,
                "count_monster_on_spawn": 8,
                "loot": [
                    {"item_name": "Dragon Ham", "npc_value": 50},
                    {"item_name": "Gold Coin", "npc_value": 1},
                    {"item_name": "Small Emerald", "npc_value": 250}
                ]
            },
            {
                "name": "Dragon Lord",
                "hp": 2100,
                "exp": 2100,
                "count_monster_on_spawn": 2,
                "loot": [
                    {"item_name": "Dragon Ham", "npc_value": 50},
                    {"item_name": "Gold Coin", "npc_value": 1},
                    {"item_name": "Royal Helmet", "npc_value": 30000},
                    {"item_name": "Dragon Scale Mail", "npc_value": 40000},
                    {"item_name": "Life Crystal", "npc_value": 50},
                    {"item_name": "Small Ruby", "npc_value": 250},
                    {"item_name": "Dragonbone Staff", "npc_value": 15000},
                    {"item_name": "Magic Plate Armor", "npc_value": 80000}
                ]
            }
        ]
    },
    {
        "name": "Orc Fortress",
        "monsters": [
            {
                "name": "Orc Berserker",
                "hp": 380,
                "exp": 270,
                "count_monster_on_spawn": 15,
                "loot": [
                    {"item_name": "Double Axe", "npc_value": 260},
                    {"item_name": "Orc Tooth", "npc_value": 100},
                    {"item_name": "Gold Coin", "npc_value": 1},
                    {"item_name": "Health Potion", "npc_value": 50},
                    {"item_name": "Battle Hammer", "npc_value": 350}
                ]
            },
            {
                "name": "Orc Leader",
                "hp": 450,
                "exp": 280,
                "count_monster_on_spawn": 3,
                "loot": [
                    {"item_name": "Battle Hammer", "npc_value": 350},
                    {"item_name": "Gold Coin", "npc_value": 1},
                    {"item_name": "Orc Leather", "npc_value": 60},
                    {"item_name": "Halberd", "npc_value": 400}
                ]
            },
            {
                "name": "Orc Shaman",
                "hp": 240,
                "exp": 170,
                "count_monster_on_spawn": 8,
                "loot": [
                    {"item_name": "Staff", "npc_value": 40},
                    {"item_name": "Gold Coin", "npc_value": 1},
                    {"item_name": "Leather Armor", "npc_value": 12},
                    {"item_name": "Mana Potion", "npc_value": 50},
                    {"item_name": "Orc Tooth", "npc_value": 100}
                ]
            },
            {
                "name": "Orc Warlord",
                "hp": 950,
                "exp": 950,
                "count_monster_on_spawn": 1,
                "loot": [
                    {"item_name": "Double Axe", "npc_value": 260},
                    {"item_name": "Gold Coin", "npc_value": 1},
                    {"item_name": "Orc Trophy", "npc_value": 5000},
                    {"item_name": "Warrior Helmet", "npc_value": 5000}
                ]
            }
        ]
    },
    {
        "name": "Necromancer Tomb",
        "monsters": [
            {
                "name": "Necromancer",
                "hp": 580,
                "exp": 580,
                "count_monster_on_spawn": 12,
                "loot": [
                    {"item_name": "Skull Staff", "npc_value": 6000},
                    {"item_name": "Gold Coin", "npc_value": 1},
                    {"item_name": "Rope Belt", "npc_value": 500},
                    {"item_name": "Dark Shield", "npc_value": 4000},
                    {"item_name": "Strong Mana Potion", "npc_value": 80},
                    {"item_name": "Bone Shoulderplate", "npc_value": 1500}
                ]
            },
            {
                "name": "Crypt Shambler",
                "hp": 300,
                "exp": 210,
                "count_monster_on_spawn": 6,
                "loot": [
                    {"item_name": "Bone Club", "npc_value": 90},
                    {"item_name": "Ghoul Snack", "npc_value": 150},
                    {"item_name": "Gold Coin", "npc_value": 1},
                    {"item_name": "Small Stone", "npc_value": 50}
                ]
            },
            {
                "name": "Priestess",
                "hp": 300,
                "exp": 230,
                "count_monster_on_spawn": 3,
                "loot": [
                    {"item_name": "Life Ring", "npc_value": 900},
                    {"item_name": "Gold Coin", "npc_value": 1},
                    {"item_name": "Skull", "npc_value": 50},
                    {"item_name": "Red Rose", "npc_value": 50},
                    {"item_name": "Mace", "npc_value": 90}
                ]
            }
        ]
    },
    {
        "name": "Ancient Scarab Cave",
        "monsters": [
            {
                "name": "Ancient Scarab",
                "hp": 900,
                "exp": 1000,
                "count_monster_on_spawn": 4,
                "loot": [
                    {"item_name": "Scarab Coin", "npc_value": 100},
                    {"item_name": "Gold Coin", "npc_value": 1},
                    {"item_name": "Gold Ingot", "npc_value": 5000},
                    {"item_name": "Small Ruby", "npc_value": 250},
                    {"item_name": "Time Ring", "npc_value": 2000}
                ]
            },
            {
                "name": "Scarab",
                "hp": 220,
                "exp": 150,
                "count_monster_on_spawn": 12,
                "loot": [
                    {"item_name": "Scarab Coin", "npc_value": 100},
                    {"item_name": "Gold Coin", "npc_value": 1},
                    {"item_name": "Small Sapphire", "npc_value": 250},
                    {"item_name": "Iron Ore", "npc_value": 400}
                ]
            }
        ]
    },
    {
        "name": "Minotaur Tower",
        "monsters": [
            {
                "name": "Minotaur Guard",
                "hp": 400,
                "exp": 250,
                "count_monster_on_spawn": 6,
                "loot": [
                    {"item_name": "Minotaur Leather", "npc_value": 80},
                    {"item_name": "Gold Coin", "npc_value": 1},
                    {"item_name": "Chain Armor", "npc_value": 200},
                    {"item_name": "Halberd", "npc_value": 400}
                ]
            },
            {
                "name": "Minotaur Archer",
                "hp": 230,
                "exp": 185,
                "count_monster_on_spawn": 8,
                "loot": [
                    {"item_name": "Iron Helmet", "npc_value": 150},
                    {"item_name": "Crossbow", "npc_value": 500},
                    {"item_name": "Gold Coin", "npc_value": 1},
                    {"item_name": "Steel Arrow", "npc_value": 5}
                ]
            },
            {
                "name": "Minotaur Mage",
                "hp": 215,
                "exp": 190,
                "count_monster_on_spawn": 4,
                "loot": [
                    {"item_name": "Spellbook", "npc_value": 150},
                    {"item_name": "Gold Coin", "npc_value": 1},
                    {"item_name": "Minotaur Horn", "npc_value": 50},
                    {"item_name": "Mana Potion", "npc_value": 50}
                ]
            },
            {
                "name": "Minotaur",
                "hp": 100,
                "exp": 50,
                "count_monster_on_spawn": 12,
                "loot": [
                    {"item_name": "Mace", "npc_value": 90},
                    {"item_name": "Gold Coin", "npc_value": 1},
                    {"item_name": "Minotaur Leather", "npc_value": 80},
                    {"item_name": "Leather Armor", "npc_value": 12}
                ]
            }
        ]
    },
    {
        "name": "Cyclops Mountain",
        "monsters": [
            {
                "name": "Cyclops",
                "hp": 260,
                "exp": 275,
                "count_monster_on_spawn": 8,
                "loot": [
                    {"item_name": "Gold Coin", "npc_value": 1},
                    {"item_name": "Battle Hammer", "npc_value": 350},
                    {"item_name": "Cyclops Toe", "npc_value": 100},
                    {"item_name": "Meat", "npc_value": 5}
                ]
            },
            {
                "name": "Cyclops Smith",
                "hp": 335,
                "exp": 345,
                "count_monster_on_spawn": 4,
                "loot": [
                    {"item_name": "Gold Coin", "npc_value": 1},
                    {"item_name": "Iron Ore", "npc_value": 400},
                    {"item_name": "Mace", "npc_value": 90}
                ]
            },
            {
                "name": "Cyclops Drone",
                "hp": 395,
                "exp": 395,
                "count_monster_on_spawn": 6,
                "loot": [
                    {"item_name": "Gold Coin", "npc_value": 1},
                    {"item_name": "Health Potion", "npc_value": 50},
                    {"item_name": "Cyclops Toe", "npc_value": 100},
                    {"item_name": "Strong Health Potion", "npc_value": 100}
                ]
            }
        ]
    },
    {
        "name": "Poison Spider Cave",
        "monsters": [
            {
                "name": "Poison Spider",
                "hp": 85,
                "exp": 90,
                "count_monster_on_spawn": 20,
                "loot": [
                    {"item_name": "Gold Coin", "npc_value": 1},
                    {"item_name": "Poisonous Slime", "npc_value": 30},
                    {"item_name": "Spider Fangs", "npc_value": 30}
                ]
            },
            {
                "name": "Giant Spider",
                "hp": 1200,
                "exp": 900,
                "count_monster_on_spawn": 2,
                "loot": [
                    {"item_name": "Gold Coin", "npc_value": 1},
                    {"item_name": "Platinum Coin", "npc_value": 100},
                    {"item_name": "Spider Silk", "npc_value": 3000},
                    {"item_name": "Knight Armor", "npc_value": 5000}
                ]
            }
        ]
    },
    {
        "name": "Tortoise Cave",
        "monsters": [
            {
                "name": "Tortoise",
                "hp": 250,
                "exp": 195,
                "count_monster_on_spawn": 15,
                "loot": [
                    {"item_name": "Gold Coin", "npc_value": 1},
                    {"item_name": "Fish", "npc_value": 5},
                    {"item_name": "Tortoise Egg", "npc_value": 100}
                ]
            },
            {
                "name": "Thornback Tortoise",
                "hp": 450,
                "exp": 355,
                "count_monster_on_spawn": 5,
                "loot": [
                    {"item_name": "Gold Coin", "npc_value": 1},
                    {"item_name": "Platinum Coin", "npc_value": 100},
                    {"item_name": "Leather Armor", "npc_value": 12},
                    {"item_name": "Tortoise Shield", "npc_value": 1500}
                ]
            }
        ]
    },
    {
        "name": "Amazon Camp",
        "monsters": [
            {
                "name": "Amazon",
                "hp": 110,
                "exp": 60,
                "count_monster_on_spawn": 12,
                "loot": [
                    {"item_name": "Gold Coin", "npc_value": 1},
                    {"item_name": "Sword", "npc_value": 85},
                    {"item_name": "Leather Boots", "npc_value": 10}
                ]
            },
            {
                "name": "Valkyrie",
                "hp": 125,
                "exp": 95,
                "count_monster_on_spawn": 6,
                "loot": [
                    {"item_name": "Gold Coin", "npc_value": 1},
                    {"item_name": "Plate Armor", "npc_value": 400},
                    {"item_name": "Longsword", "npc_value": 160}
                ]
            }
        ]
    },
    {
        "name": "Hydra Cave",
        "monsters": [
            {
                "name": "Hydra",
                "hp": 2600,
                "exp": 2100,
                "count_monster_on_spawn": 3,
                "loot": [
                    {"item_name": "Gold Coin", "npc_value": 1},
                    {"item_name": "Platinum Coin", "npc_value": 100},
                    {"item_name": "Hydra Head", "npc_value": 1000},
                    {"item_name": "Great Health Potion", "npc_value": 190},
                    {"item_name": "Royal Helmet", "npc_value": 30000}
                ]
            }
        ]
    }
]


# 443, 444, 445
# Create function that takes list of dictionaries and return int , number that is answer for the question:
# Knowing that I can't handle monsters that have over 600hp, where will I gain the most experience (exp)?

def max_exp(dataset):
    max_exp_value = max(monster['exp'] for location in dataset for monster in location['monsters'])

    return max_exp_value


assert max_exp(expowiska) == 2100


# 446, 447, 448
# Create function that takes list of dictionaries and return dictionary that is answer for the question:
# Which monster has the best exp to hp ratio (the more exp for less hp the better)

def best_exp_to_hp_ratio(dataset):
    best_monster = max(
        (
            {'monster': monster['name'], 'exp_to_hp': monster['exp'] / monster['hp']}
            for location in dataset
            for monster in location['monsters']
        ),
        key=lambda m: m['exp_to_hp'],
        default=None
    )
    return best_monster


# print(best_exp_to_hp_ratio(expowiska))
assert best_exp_to_hp_ratio(expowiska) == {'monster': 'Ancient Scarab', 'exp_to_hp': 1.1111111111111112}


# 449
# The same what # 446 but traditional way


def best_exp_to_hp_ratio_2(dataset):
    best_monster = None
    best_ratio = 0

    for location in dataset:
        for monster in location['monsters']:

            ratio = monster['exp'] / monster['hp']

            if ratio > best_ratio:
                best_ratio = ratio
                best_monster = {
                    'monster': monster['name'],
                    'exp_to_hp': best_ratio
                }

    return best_monster


assert best_exp_to_hp_ratio_2(expowiska) == {'monster': 'Ancient Scarab', 'exp_to_hp': 1.1111111111111112}


# 450, 451, 452
# create function that takes list of dictionaries and return dictionary which is answer for the following question:
# Knowing that every monster always drops all the loot, which hunting ground will give me the most money?
#
# - Monsters will only appear once on hunting grounds and will not reappear after being killed


def best_loot_location(dataset):
    max_loot_value = 0
    best_location = None

    for location in dataset:
        total_loot_value = 0
        for monster in location['monsters']:
            loot_value_per_monster = sum(item['npc_value'] for item in monster['loot'])
            total_loot_value += loot_value_per_monster * monster['count_monster_on_spawn']

        if total_loot_value > max_loot_value:
            max_loot_value = total_loot_value
            best_location = {
                'location': location['name'],
                'total_loot_value': max_loot_value
            }

    return best_location


# print(best_loot_location(expowiska))
assert best_loot_location(expowiska) == {'location': 'Dragon Lair', 'total_loot_value': 529120}


# 453, 454, 455
# The same what 450 but different way


def best_loot_location_2(dataset):
    best_location = max(
        (
            {
                'location': location['name'],
                'total_loot_value': sum(
                    sum(item['npc_value'] for item in monster['loot']) * monster['count_monster_on_spawn']
                    for monster in location['monsters']
                )
            }
            for location in dataset
        ),
        key=lambda loc: loc['total_loot_value'],
        default=None
    )
    return best_location


assert best_loot_location_2(expowiska) == {'location': 'Dragon Lair', 'total_loot_value': 529120}

pokemons_data = [
    {
        "name": "Bulbasaur",
        "type": ["Grass", "Poison"],
        "hp": 45,
        "attack": 49,
        "defense": 49,
        "beats": ["Water", "Rock", "Ground"],
    },
    {
        "name": "Ivysaur",
        "type": ["Grass", "Poison"],
        "hp": 60,
        "attack": 62,
        "defense": 63,
        "beats": ["Water", "Rock", "Ground"],
    },
    {
        "name": "Venusaur",
        "type": ["Grass", "Poison"],
        "hp": 80,
        "attack": 82,
        "defense": 83,
        "beats": ["Water", "Rock", "Ground"],
    },
    {
        "name": "Charmander",
        "type": ["Fire"],
        "hp": 39,
        "attack": 52,
        "defense": 43,
        "beats": ["Grass", "Bug", "Ice", "Steel"],
    },
    {
        "name": "Charmeleon",
        "type": ["Fire"],
        "hp": 58,
        "attack": 64,
        "defense": 58,
        "beats": ["Grass", "Bug", "Ice", "Steel"],
    },
    {
        "name": "Charizard",
        "type": ["Fire", "Flying"],
        "hp": 78,
        "attack": 84,
        "defense": 78,
        "beats": ["Grass", "Bug", "Ice", "Steel"],
    },
    {
        "name": "Squirtle",
        "type": ["Water"],
        "hp": 44,
        "attack": 48,
        "defense": 65,
        "beats": ["Fire", "Rock", "Ground"],
    },
    {
        "name": "Wartortle",
        "type": ["Water"],
        "hp": 59,
        "attack": 63,
        "defense": 80,
        "beats": ["Fire", "Rock", "Ground"],
    },
    {
        "name": "Blastoise",
        "type": ["Water"],
        "hp": 79,
        "attack": 83,
        "defense": 100,
        "beats": ["Fire", "Rock", "Ground"],
    },
    {
        "name": "Caterpie",
        "type": ["Bug"],
        "hp": 45,
        "attack": 30,
        "defense": 35,
        "beats": ["Grass", "Psychic", "Dark"],
    },
    {
        "name": "Metapod",
        "type": ["Bug"],
        "hp": 50,
        "attack": 20,
        "defense": 55,
        "beats": ["Grass", "Psychic", "Dark"],
    },
    {
        "name": "Butterfree",
        "type": ["Bug", "Flying"],
        "hp": 60,
        "attack": 45,
        "defense": 50,
        "beats": ["Grass", "Fighting", "Bug"],
    },
    {
        "name": "Weedle",
        "type": ["Bug", "Poison"],
        "hp": 40,
        "attack": 35,
        "defense": 30,
        "beats": ["Grass", "Fairy", "Fighting"],
    },
    {
        "name": "Kakuna",
        "type": ["Bug", "Poison"],
        "hp": 45,
        "attack": 25,
        "defense": 50,
        "beats": ["Grass", "Fairy", "Fighting"],
    },
    {
        "name": "Beedrill",
        "type": ["Bug", "Poison"],
        "hp": 65,
        "attack": 90,
        "defense": 40,
        "beats": ["Grass", "Fairy", "Fighting"],
    },
    {
        "name": "Pidgey",
        "type": ["Normal", "Flying"],
        "hp": 40,
        "attack": 45,
        "defense": 40,
        "beats": ["Bug", "Grass", "Fighting"],
    },
    {
        "name": "Pidgeotto",
        "type": ["Normal", "Flying"],
        "hp": 63,
        "attack": 60,
        "defense": 55,
        "beats": ["Bug", "Grass", "Fighting"],
    },
    {
        "name": "Pidgeot",
        "type": ["Normal", "Flying"],
        "hp": 83,
        "attack": 80,
        "defense": 75,
        "beats": ["Bug", "Grass", "Fighting"],
    },
    {
        "name": "Rattata",
        "type": ["Normal"],
        "hp": 30,
        "attack": 56,
        "defense": 35,
        "beats": ["Ghost"],
    },
    {
        "name": "Raticate",
        "type": ["Normal"],
        "hp": 55,
        "attack": 81,
        "defense": 60,
        "beats": ["Ghost"],
    },
    {
        "name": "Spearow",
        "type": ["Normal", "Flying"],
        "hp": 40,
        "attack": 60,
        "defense": 30,
        "beats": ["Bug", "Grass", "Fighting"],
    },
    {
        "name": "Fearow",
        "type": ["Normal", "Flying"],
        "hp": 65,
        "attack": 90,
        "defense": 65,
        "beats": ["Bug", "Grass", "Fighting"],
    },
    {
        "name": "Ekans",
        "type": ["Poison"],
        "hp": 35,
        "attack": 60,
        "defense": 44,
        "beats": ["Grass", "Fairy", "Fighting"],
    },
    {
        "name": "Arbok",
        "type": ["Poison"],
        "hp": 60,
        "attack": 95,
        "defense": 69,
        "beats": ["Grass", "Fairy", "Fighting"],
    },
    {
        "name": "Pikachu",
        "type": ["Electric"],
        "hp": 35,
        "attack": 55,
        "defense": 40,
        "beats": ["Water", "Flying"],
    },
    {
        "name": "Raichu",
        "type": ["Electric"],
        "hp": 60,
        "attack": 90,
        "defense": 55,
        "beats": ["Water", "Flying"],
    },
    {
        "name": "Sandshrew",
        "type": ["Ground"],
        "hp": 50,
        "attack": 75,
        "defense": 85,
        "beats": ["Fire", "Electric", "Poison"],
    }
]


# 456, 457, 458
# create function that takes list od dictionaries and returns int , number that is answer on the following question:
# How many Pokemon are there that beat Water Pokemon and have an attack greater than 70?


def check_num_pok(any_data):
    return len([name['name'] for name in any_data if 'Water' in name['beats'] and name['attack'] > 70])


# print(check_num_pok(pokemons_data))
assert check_num_pok(pokemons_data) == 2


# 459, 460, 461
# create function that takes list od dictionaries and returns int , number that is answer on the following question:
# What is the average attack power of Pokemons that beat at least 3 types of Pokemon?


def average_attack_force_value(data):
    values_lst = [a_value['attack'] for a_value in data if len(a_value['beats']) >= 3]
    return round((sum(values_lst) / len(values_lst)), 3)


assert average_attack_force_value(pokemons_data) == 60.739


# 462, 463, 464
# create function that takes list od dictionaries and returns str , number that is answer on the following question:
# Which Pokémon has the highest Attack and Defense totals among those beating Grass-type Pokémon?


def strongest_pokemon(data):
    grass_beaters = [pokemon for pokemon in data if "Grass" in pokemon["beats"]]
    strongest = max(grass_beaters, key=lambda p: p["attack"] + p["defense"])
    return strongest["name"]


assert strongest_pokemon(pokemons_data) == 'Arbok'


# 465, 467, 468
# create function that takes list of dictionaries and returns sorted names list for the pokemons that have
# attack > 50 and defence > 70

def sorted_list_pokemons(any_data):
    return sorted([p_name['name'] for p_name in any_data if p_name['attack'] > 50 and p_name['defense'] > 70])


# print(sorted_list_pokemons(pokemons_data))
assert sorted_list_pokemons(pokemons_data) == ['Blastoise', 'Charizard', 'Pidgeot', 'Sandshrew', 'Venusaur',
                                               'Wartortle']


# 469, 470, 471
# create function that takes list of dictionaries and returns dictionary for the pokemons that have
# hp > 70, key: name, value: beats


def dict_pokemons_hp_over_70(any_data):
    return {p_name['name']: p_name['beats'] for p_name in any_data if p_name['hp'] > 70}


# print(dict_pokemons_hp_over_70(pokemons_data))
assert dict_pokemons_hp_over_70(pokemons_data) == {'Venusaur': ['Water', 'Rock', 'Ground'],
                                                   'Charizard': ['Grass', 'Bug', 'Ice', 'Steel'],
                                                   'Blastoise': ['Fire', 'Rock', 'Ground'],
                                                   'Pidgeot': ['Bug', 'Grass', 'Fighting']}


# 472, 473, 473
# create function that takes list of dictionaries and returns list of tuples if 'Flying' is in 'type' and not 'Normal' in the 'type'
# tuple has to includes name and list of type


def list_of_tuples_for_fly_norm(any_data):
    return [(p_name['name'], p_name['type']) for p_name in any_data if
            'Flying' in p_name['type'] and 'Normal' not in p_name['type']]


assert (list_of_tuples_for_fly_norm(pokemons_data)) == [('Charizard', ['Fire', 'Flying']),
                                                        ('Butterfree', ['Bug', 'Flying'])]


# 474, 475, 476
# The same what # 472 but name should be swapcase and reverse


def list_of_tuples_for_fly_norm_swap_reverse(any_data):
    return [(p_name['name'].swapcase()[::-1], p_name['type']) for p_name in any_data if
            'Flying' in p_name['type'] and 'Normal' not in p_name['type']]


# print(list_of_tuples_for_fly_norm_swap_reverse(pokemons_data))
assert list_of_tuples_for_fly_norm_swap_reverse(pokemons_data) == [('DRAZIRAHc', ['Fire', 'Flying']),
                                                                   ('EERFRETTUb', ['Bug', 'Flying'])]

movies = [
    {
        "title": "Nausicaä of the Valley of the Wind",
        "polish_title": "Nausicaä z Doliny Wiatru",
        "year": 1984,
        "genre": ["Animation", "Adventure", "Sci-Fi"],
        "main_character": "Nausicaä",
        "main_character_sex": "Female",
        "duration": 117,
        "imdb_rating": 8.0,
        "director": "Hayao Miyazaki",
        "box_office": 9019660,
        "soundtrack_by": "Joe Hisaishi"
    },
    {
        "title": "Castle in the Sky",
        "polish_title": "Laputa – podniebny zamek",
        "year": 1986,
        "genre": ["Animation", "Adventure", "Family"],
        "main_character": "Sheeta",
        "main_character_sex": "Female",
        "duration": 124,
        "imdb_rating": 8.0,
        "director": "Hayao Miyazaki",
        "box_office": 6218229,
        "soundtrack_by": "Joe Hisaishi"
    },
    {
        "title": "Grave of the Fireflies",
        "polish_title": "Grobowiec świetlików",
        "year": 1988,
        "genre": ["Animation", "Drama", "War"],
        "main_character": "Yokokawa Seita",
        "main_character_sex": "Male",
        "duration": 88,
        "imdb_rating": 8.5,
        "director": "Isao Takahata",
        "box_office": 519421,
        "soundtrack_by": "Michio Mamiya"
    },
    {
        "title": "My Neighbor Totoro",
        "polish_title": "Mój sąsiad Totoro",
        "year": 1988,
        "genre": ["Animation", "Comedy", "Family"],
        "main_character": "Satsuki Kusakabe",
        "main_character_sex": "Female",
        "duration": 86,
        "imdb_rating": 8.1,
        "director": "Hayao Miyazaki",
        "box_office": 30336425,
        "soundtrack_by": "Joe Hisaishi"
    },
    {
        "title": "Kiki's Delivery Service",
        "polish_title": "Podniebna poczta Kiki",
        "year": 1989,
        "genre": ["Animation", "Family", "Fantasy"],
        "main_character": "Kiki",
        "main_character_sex": "Female",
        "duration": 103,
        "imdb_rating": 7.8,
        "director": "Hayao Miyazaki",
        "box_office": 10403278,
        "soundtrack_by": "Joe Hisaishi"
    },
    {
        "title": "Only Yesterday",
        "polish_title": "Powrót do marzeń",
        "year": 1991,
        "genre": ["Animation", "Drama", "Romance"],
        "main_character": "Taeko Okajima",
        "main_character_sex": "Female",
        "duration": 119,
        "imdb_rating": 7.6,
        "director": "Isao Takahata",
        "box_office": 608562,
        "soundtrack_by": "Katz Hoshi"
    },
    {
        "title": "Porco Rosso",
        "polish_title": "Szkarłatny pilot",
        "year": 1992,
        "genre": ["Animation", "Adventure", "Comedy"],
        "main_character": "Porco Rosso",
        "main_character_sex": "Male",
        "duration": 94,
        "imdb_rating": 7.7,
        "director": "Hayao Miyazaki",
        "box_office": 1458536,
        "soundtrack_by": "Joe Hisaishi"
    },
    {
        "title": "Ocean Waves",
        "polish_title": "Szum morza",
        "year": 1993,
        "genre": ["Animation", "Drama", "Romance"],
        "main_character": "Taku Morisaki",
        "main_character_sex": "Male",
        "duration": 72,
        "imdb_rating": 6.6,
        "director": "Tomomi Mochizuki",
        "box_office": 87738,
        "soundtrack_by": "Shigeru Nagata"
    },
    {
        "title": "Pom Poko",
        "polish_title": "Szopy w natarciu",
        "year": 1994,
        "genre": ["Animation", "Comedy", "Drama"],
        "main_character": "Shoukichi",
        "main_character_sex": "Male",
        "duration": 119,
        "imdb_rating": 7.3,
        "director": "Isao Takahata",
        "box_office": 1279218,
        "soundtrack_by": "Shang Shang Typhoon"
    },
    {
        "title": "Whisper of the Heart",
        "polish_title": "Szept serca",
        "year": 1995,
        "genre": ["Animation", "Drama", "Family"],
        "main_character": "Shizuku Tsukishima",
        "main_character_sex": "Female",
        "duration": 111,
        "imdb_rating": 7.8,
        "director": "Yoshifumi Kondō",
        "box_office": 4420615,
        "soundtrack_by": "Yuji Nomi"
    },
    {
        "title": "Princess Mononoke",
        "polish_title": "Księżniczka Mononoke",
        "year": 1997,
        "genre": ["Animation", "Action", "Adventure"],
        "main_character": "Ashitaka",
        "main_character_sex": "Male",
        "duration": 133,
        "imdb_rating": 8.3,
        "director": "Hayao Miyazaki",
        "box_office": 170347532,
        "soundtrack_by": "Joe Hisaishi"
    },
    {
        "title": "My Neighbors the Yamadas",
        "polish_title": "Rodzinka Yamadów",
        "year": 1999,
        "genre": ["Animation", "Comedy", "Family"],
        "main_character": "Matsuko Yamada",
        "main_character_sex": "Female",
        "duration": 104,
        "imdb_rating": 7.1,
        "director": "Isao Takahata",
        "box_office": 22261,
        "soundtrack_by": "Akiko Yano"
    },
    {
        "title": "Spirited Away",
        "polish_title": "W krainie bogów",
        "year": 2001,
        "genre": ["Animation", "Adventure", "Family"],
        "main_character": "Chihiro",
        "main_character_sex": "Female",
        "duration": 124,
        "imdb_rating": 8.6,
        "director": "Hayao Miyazaki",
        "box_office": 358135197,
        "soundtrack_by": "Joe Hisaishi"
    },
    {
        "title": "The Cat Returns",
        "polish_title": "Narzeczona dla kota",
        "year": 2002,
        "genre": ["Animation", "Adventure", "Comedy"],
        "main_character": "Haru",
        "main_character_sex": "Female",
        "duration": 75,
        "imdb_rating": 7.1,
        "director": "Hiroyuki Morita",
        "box_office": 54505827,
        "soundtrack_by": "Yuji Nomi"
    },
    {
        "title": "Howl's Moving Castle",
        "polish_title": "Ruchomy zamek Hauru",
        "year": 2004,
        "genre": ["Animation", "Adventure", "Family"],
        "main_character": "Sofi",
        "main_character_sex": "Female",
        "duration": 119,
        "imdb_rating": 8.2,
        "director": "Hayao Miyazaki",
        "box_office": 240420227,
        "soundtrack_by": "Joe Hisaishi"
    },
    {
        "title": "Tales from Earthsea",
        "polish_title": "Opowieści z Ziemiomorza",
        "year": 2006,
        "genre": ["Animation", "Adventure", "Fantasy"],
        "main_character": "Arren",
        "main_character_sex": "Male",
        "duration": 115,
        "imdb_rating": 6.3,
        "director": "Gorō Miyazaki",
        "box_office": 68673762,
        "soundtrack_by": "Tamiya Terashima"
    },
    {
        "title": "Ponyo",
        "polish_title": "Ponyo",
        "year": 2008,
        "genre": ["Animation", "Adventure", "Comedy"],
        "main_character": "Ponyo",
        "main_character_sex": "Female",
        "duration": 101,
        "imdb_rating": 7.6,
        "director": "Hayao Miyazaki",
        "box_office": 205918431,
        "soundtrack_by": "Joe Hisaishi"
    },
    {
        "title": "Arrietty",
        "polish_title": "Tajemniczy świat Arrietty",
        "year": 2010,
        "genre": ["Animation", "Adventure", "Drama"],
        "main_character": "Arrietty",
        "main_character_sex": "Female",
        "duration": 94,
        "imdb_rating": 7.6,
        "director": "Hiromasa Yonebayashi",
        "box_office": 149660003,
        "soundtrack_by": "Cécile Corbel"
    },
    {
        "title": "From Up on Poppy Hill",
        "polish_title": "Makowe wzgórze",
        "year": 2011,
        "genre": ["Animation", "Comedy", "Drama"],
        "main_character": "Umi Matsuzaki",
        "main_character_sex": "Female",
        "duration": 91,
        "imdb_rating": 7.4,
        "director": "Gorō Miyazaki",
        "box_office": 61485364,
        "soundtrack_by": "Satoshi Takebe"
    },
    {
        "title": "The Wind Rises",
        "polish_title": "Zrywa się wiatr",
        "year": 2013,
        "genre": ["Animation", "Biography", "Drama"],
        "main_character": "Jirō Horikoshi",
        "main_character_sex": "Male",
        "duration": 126,
        "imdb_rating": 7.8,
        "director": "Hayao Miyazaki",
        "box_office": 136865294,
        "soundtrack_by": "Joe Hisaishi"
    },
    {
        "title": "The Tale of the Princess Kaguya",
        "polish_title": "Księżniczka Kaguya",
        "year": 2013,
        "genre": ["Animation", "Drama", "Family"],
        "main_character": "Princess Kaguya",
        "main_character_sex": "Female",
        "duration": 137,
        "imdb_rating": 8.0,
        "director": "Isao Takahata",
        "box_office": 24751400,
        "soundtrack_by": "Joe Hisaishi"
    },
    {
        "title": "When Marnie Was There",
        "polish_title": "Marnie. Przyjaciółka ze snów",
        "year": 2014,
        "genre": ["Animation", "Drama", "Family"],
        "main_character": "Anna Sasaki",
        "main_character_sex": "Female",
        "duration": 103,
        "imdb_rating": 7.6,
        "director": "Hiromasa Yonebayashi",
        "box_office": 35012681,
        "soundtrack_by": "Takatsugu Muramatsu"
    },
    {
        "title": "The Red Turtle",
        "polish_title": "Czerwony żółw",
        "year": 2016,
        "genre": ["Animation", "Drama", "Family"],
        "main_character": "The Man",
        "main_character_sex": "Male",
        "duration": 80,
        "imdb_rating": 7.5,
        "director": "Michaël Dudok de Wit",
        "box_office": 6613503,
        "soundtrack_by": "Laurent Perez del Mar"
    },
    {
        "title": "Earwig and the Witch",
        "polish_title": "Skorek i czarownica",
        "year": 2020,
        "genre": ["Animation", "Adventure", "Family"],
        "main_character": "Earwig",
        "main_character_sex": "Female",
        "duration": 82,
        "imdb_rating": 4.7,
        "director": "Gorō Miyazaki",
        "box_office": 842744,
        "soundtrack_by": "Satoshi Takebe"
    },
    {
        "title": "The Boy and the Heron",
        "polish_title": "Chłopiec i czapla",
        "year": 2023,
        "genre": ["Animation", "Adventure", "Drama"],
        "main_character": "Mahito Maki",
        "main_character_sex": "Male",
        "duration": 124,
        "imdb_rating": 7.5,
        "director": "Hayao Miyazaki",
        "box_office": 173437244,
        "soundtrack_by": "Joe Hisaishi"
    }
]


# 477, 478, 479
# create a function that returns dictionary that :
# key: movies with a female lead value: year of production that have an IMDb rating of 8.0 or higher


def dict_film_female(any_data):
    return {item['title']: item['year'] for item in any_data if
            item['main_character_sex'] == 'Female' and item['imdb_rating'] >= 8}


assert dict_film_female(movies) == {'Nausicaä of the Valley of the Wind': 1984, 'Castle in the Sky': 1986,
                                    'My Neighbor Totoro': 1988, 'Spirited Away': 2001, "Howl's Moving Castle": 2004,
                                    'The Tale of the Princess Kaguya': 2013}


# 480, 481, 482
# the same what # 477 but function has to return list of tuples


def list_tuples_film_female(any_data):
    return [(item['title'], item['year']) for item in any_data if
            item['main_character_sex'] == 'Female' and item['imdb_rating'] >= 8]


assert list_tuples_film_female(movies) == [('Nausicaä of the Valley of the Wind', 1984), ('Castle in the Sky', 1986),
                                           ('My Neighbor Totoro', 1988), ('Spirited Away', 2001),
                                           ("Howl's Moving Castle", 2004), ('The Tale of the Princess Kaguya', 2013)]


# 483, 484, 485
# create a function that returns tuple with the answer on th efollowing question :
# What is the highest grossing film genre (excluding "Animation") produced by director Hayao Miyazaki?


def dict_genre_film_hayao(any_data):
    list_of_movies_hayao = [film for film in any_data if film['director'] == 'Hayao Miyazaki']

    genre_without_animation = [[genre for genre in film['genre'] if genre != 'Animation'] for film in
                               list_of_movies_hayao]

    genre_revenue_pairs = [
        (genre, film["box_office"])
        for film in list_of_movies_hayao
        for genre in film["genre"] if genre != "Animation"
    ]

    genre_revenues = {
        genre: sum(revenue for g, revenue in genre_revenue_pairs if g == genre)
        for genre, _ in genre_revenue_pairs
    }

    highest_revenue_genre = max(genre_revenues, key=genre_revenues.get)
    highest_revenue = genre_revenues[highest_revenue_genre]

    return highest_revenue_genre, highest_revenue


assert dict_genre_film_hayao(movies) == ('Adventure', 1164955056)


# 486, 487, 489
# create a function that returns tuple with the answer on th efollowing question :
# Find the shortest Ghibli movie that earned more than the average earnings of all movies.
# View the movie title, length, and its revenue.


def shortest_film_above_avg(any_data):
    avg_revenue = sum(film["box_office"] for film in any_data) / len(any_data)

    films_above_avg = [film for film in any_data if film["box_office"] > avg_revenue]

    shortest_film = min(films_above_avg, key=lambda film: film["duration"])

    return shortest_film["title"], shortest_film["duration"], shortest_film["box_office"]


assert shortest_film_above_avg(movies) == ('Arrietty', 94, 149660003)

f1_1998_season = {
    'scoring': {
        '1st': 10,
        '2nd': 6,
        '3rd': 4,
        '4th': 3,
        '5th': 2,
        '6th': 1
    },
    'teams': {
        'williams': {
            'car': 'FW20',
            'nationality': 'Great Britain',
            'drivers': [
                {
                    'name': 'Damon Hill',
                    'nationality': 'Great Britain'
                },
                {
                    'name': 'Jacques Villeneuve',
                    'nationality': 'Canada'
                }
            ],
        },
        'ferrari': {
            'car': 'F300',
            'nationality': 'Italy',
            'drivers': [
                {
                    'name': 'Michael Schumacher',
                    'nationality': 'Germany'
                },
                {
                    'name': 'Eddie Irvine',
                    'nationality': 'Great Britain'
                }
            ],
        },
        'benetton': {
            'car': 'B198',
            'nationality': 'Italy',
            'drivers': [
                {
                    'name': 'Giancarlo Fisichella',
                    'nationality': 'Italy'
                },
                {
                    'name': 'Alexander Wurz',
                    'nationality': 'Austria'
                }
            ],
        },
        'mclaren': {
            'car': 'MP4/13',
            'nationality': 'Great Britain',
            'drivers': [
                {
                    'name': 'David Coulthard',
                    'nationality': 'Great Britain'
                },
                {
                    'name': 'Mika Häkkinen',
                    'nationality': 'Finland'
                }
            ],
        },
        'jordan': {
            'car': '198',
            'nationality': 'Ireland',
            'drivers': [
                {
                    'name': 'Heinz-Harald Frentzen',
                    'nationality': 'Germany'
                },
                {
                    'name': 'Ralf Schumacher',
                    'nationality': 'Germany'
                }
            ],
        },
        'peugeot': {
            'car': 'AP01',
            'nationality': 'France',
            'drivers': [
                {
                    'name': 'Olivier Panis',
                    'nationality': 'France'
                },
                {
                    'name': 'Jarno Trulli',
                    'nationality': 'Italy'
                }
            ],
        },
        'sauber': {
            'car': 'C17',
            'nationality': 'Switzerland',
            'drivers': [
                {
                    'name': 'Jean Alesi',
                    'nationality': 'France'
                },
                {
                    'name': 'Johnny Herbert',
                    'nationality': 'Great Britain'
                }
            ],
        },
        'arrows': {
            'car': 'A19',
            'nationality': 'Great Britain',
            'drivers': [
                {
                    'name': 'Pedro Diniz',
                    'nationality': 'Brazil'
                },
                {
                    'name': 'Mika Salo',
                    'nationality': 'Finland'
                }
            ],
        },
        'stewart': {
            'car': 'SF02',
            'nationality': 'Great Britain',
            'drivers': [
                {
                    'name': 'Rubens Barrichello',
                    'nationality': 'Brazil'
                },
                {
                    'name': 'Jan Magnussen',
                    'nationality': 'Denmark'
                },
                {
                    'name': 'Jos Verstappen',
                    'nationality': 'Netherlands'
                }
            ],
        },
        'tyrrell': {
            'car': '026',
            'nationality': 'Great Britain',
            'drivers': [
                {
                    'name': 'Ricardo Rosset',
                    'nationality': 'Brazil'
                },
                {
                    'name': 'Toranosuke Takagi',
                    'nationality': 'Japan'
                }
            ],
        },
        'minardi': {
            'car': 'M198',
            'nationality': 'Italy',
            'drivers': [
                {
                    'name': 'Pedro Diniz',
                    'nationality': 'Brazil'
                },
                {
                    'name': 'Esteban Tuero',
                    'nationality': 'Argentina'
                }
            ],
        },
    },
    'rounds': {
        'australia': {
            'summary': {
                'winner': 'Mika Häkkinen',
                'pole_position': 'Mika Häkkinen',
                'fastest_lap': 'Mika Häkkinen'
            },
            'race_result': {
                '1st': 'Mika Häkkinen',
                '2nd': 'David Coulthard',
                '3rd': 'Heinz-Harald Frentzen',
                '4th': 'Eddie Irvine',
                '5th': 'Jacques Villeneuve',
                '6th': 'Johnny Herbert',
            },
        },
        'brazil': {
            'summary': {
                'winner': 'Mika Häkkinen',
                'pole_position': 'Mika Häkkinen',
                'fastest_lap': 'Mika Häkkinen'
            },
            'race_result': {
                '1st': 'Mika Häkkinen',
                '2nd': 'David Coulthard',
                '3rd': 'Michael Schumacher',
                '4th': 'Alexander Wurz',
                '5th': 'Heinz-Harald Frentzen',
                '6th': 'Giancarlo Fisichella',
            },
        },
        'argentina': {
            'summary': {
                'winner': 'Michael Schumacher',
                'pole_position': 'David Coulthard',
                'fastest_lap': 'Alexander Wurz'
            },
            'race_result': {
                '1st': 'Michael Schumacher',
                '2nd': 'Mika Häkkinen',
                '3rd': 'Eddie Irvine',
                '4th': 'Alexander Wurz',
                '5th': 'Jean Alesi',
                '6th': 'David Coulthard',
            },
        },
        'san_marino': {
            'summary': {
                'winner': 'David Coulthard',
                'pole_position': 'David Coulthard',
                'fastest_lap': 'Michael Schumacher'
            },
            'race_result': {
                '1st': 'David Coulthard',
                '2nd': 'Michael Schumacher',
                '3rd': 'Eddie Irvine',
                '4th': 'Jacques Villeneuve',
                '5th': 'Heinz-Harald Frentzen',
                '6th': 'Jean Alesi',
            },
        },
        'spain': {
            'summary': {
                'winner': 'Mika Häkkinen',
                'pole_position': 'Mika Häkkinen',
                'fastest_lap': 'Mika Häkkinen'
            },
            'race_result': {
                '1st': 'Mika Häkkinen',
                '2nd': 'David Coulthard',
                '3rd': 'Michael Schumacher',
                '4th': 'Alexander Wurz',
                '5th': 'Rubens Barrichello',
                '6th': 'Jacques Villeneuve',
            },
        },
        'monaco': {
            'summary': {
                'winner': 'Mika Häkkinen',
                'pole_position': 'Mika Häkkinen',
                'fastest_lap': 'Mika Häkkinen'
            },
            'race_result': {
                '1st': 'Mika Häkkinen',
                '2nd': 'Giancarlo Fisichella',
                '3rd': 'Eddie Irvine',
                '4th': 'Mika Salo',
                '5th': 'Jacques Villeneuve',
                '6th': 'Pedro Diniz',
            },
        },
        'canada': {
            'summary': {
                'winner': 'Michael Schumacher',
                'pole_position': 'David Coulthard',
                'fastest_lap': 'Michael Schumacher'
            },
            'race_result': {
                '1st': 'Michael Schumacher',
                '2nd': 'Giancarlo Fisichella',
                '3rd': 'Eddie Irvine',
                '4th': 'Alexander Wurz',
                '5th': 'Rubens Barrichello',
                '6th': 'Jan Magnussen',
            },
        },
        'france': {
            'summary': {
                'winner': 'Michael Schumacher',
                'pole_position': 'Mika Häkkinen',
                'fastest_lap': 'David Coulthard'
            },
            'race_result': {
                '1st': 'Michael Schumacher',
                '2nd': 'Eddie Irvine',
                '3rd': 'Mika Häkkinen',
                '4th': 'Jacques Villeneuve',
                '5th': 'Alexander Wurz',
                '6th': 'David Coulthard',
            },
        },
        'britain': {
            'summary': {
                'winner': 'Michael Schumacher',
                'pole_position': 'Mika Häkkinen',
                'fastest_lap': 'Michael Schumacher'
            },
            'race_result': {
                '1st': 'Michael Schumacher',
                '2nd': 'Mika Häkkinen',
                '3rd': 'Eddie Irvine',
                '4th': 'Alexander Wurz',
                '5th': 'Giancarlo Fisichella',
                '6th': 'Ralf Schumacher',
            },
        },
        'austria': {
            'summary': {
                'winner': 'Mika Häkkinen',
                'pole_position': 'Mika Häkkinen',
                'fastest_lap': 'David Coulthard'
            },
            'race_result': {
                '1st': 'Mika Häkkinen',
                '2nd': 'David Coulthard',
                '3rd': 'Michael Schumacher',
                '4th': 'Eddie Irvine',
                '5th': 'Ralf Schumacher',
                '6th': 'Jacques Villeneuve',
            },
        },
        'german': {
            'summary': {
                'winner': 'Mika Häkkinen',
                'pole_position': 'Mika Häkkinen',
                'fastest_lap': 'David Coulthard'
            },
            'race_result': {
                '1st': 'Mika Häkkinen',
                '2nd': 'David Coulthard',
                '3rd': 'Jacques Villeneuve',
                '4th': 'Damon Hill',
                '5th': 'Michael Schumacher',
                '6th': 'Ralf Schumacher',
            },
        },
        'hungary': {
            'summary': {
                'winner': 'Michael Schumacher',
                'pole_position': 'Mika Häkkinen',
                'fastest_lap': 'Michael Schumacher'
            },
            'race_result': {
                '1st': 'Michael Schumacher',
                '2nd': 'David Coulthard',
                '3rd': 'Jacques Villeneuve',
                '4th': 'Damon Hill',
                '5th': 'Heinz-Harald Frentzen',
                '6th': 'Mika Häkkinen',
            },
        },
        'belgium': {
            'summary': {
                'winner': 'Damon Hill',
                'pole_position': 'Mika Häkkinen',
                'fastest_lap': 'Michael Schumacher'
            },
            'race_result': {
                '1st': 'Damon Hill',
                '2nd': 'Ralf Schumacher',
                '3rd': 'Jean Alesi',
                '4th': 'Heinz-Harald Frentzen',
                '5th': 'Pedro Diniz',
                '6th': 'Jarno Trulli',
            },
        },
        'italy': {
            'summary': {
                'winner': 'Michael Schumacher',
                'pole_position': 'Michael Schumacher',
                'fastest_lap': 'Mika Häkkinen'
            },
            'race_result': {
                '1st': 'Michael Schumacher',
                '2nd': 'Eddie Irvine',
                '3rd': 'Ralf Schumacher',
                '4th': 'Mika Häkkinen',
                '5th': 'Jean Alesi',
                '6th': 'Damon Hill',
            },
        },
        'luxembourg': {
            'summary': {
                'winner': 'Mika Häkkinen',
                'pole_position': 'Michael Schumacher',
                'fastest_lap': 'Mika Häkkinen'
            },
            'race_result': {
                '1st': 'Mika Häkkinen',
                '2nd': 'Michael Schumacher',
                '3rd': 'David Coulthard',
                '4th': 'Eddie Irvine',
                '5th': 'Heinz-Harald Frentzen',
                '6th': 'Giancarlo Fisichella',
            },
        },
        'japan': {
            'summary': {
                'winner': 'Mika Häkkinen',
                'pole_position': 'Michael Schumacher',
                'fastest_lap': 'Michael Schumacher'
            },
            'race_result': {
                '1st': 'Mika Häkkinen',
                '2nd': 'Eddie Irvine',
                '3rd': 'David Coulthard',
                '4th': 'Damon Hill',
                '5th': 'Heinz-Harald Frentzen',
                '6th': 'Jacques Villeneuve',
            },
        },
    }
}


# 490, 491, 492
# create a function that returns dictionary with the answer on th efollowing question :
# Create a dictionary with the final driver classification.


def get_driver_standings(season_data):
    scoring_system = season_data['scoring']

    standings = {
        driver: sum(
            scoring_system.get(position, 0)
            for round_data in season_data['rounds'].values()
            for position, race_driver in round_data['race_result'].items()
            if race_driver == driver
        )
        for round_data in season_data['rounds'].values()
        for driver in round_data['race_result'].values()
    }

    sorted_standings = dict(sorted(standings.items(), key=lambda item: item[1], reverse=True))

    return sorted_standings


assert get_driver_standings(f1_1998_season) == {'Mika Häkkinen': 100, 'Michael Schumacher': 86, 'David Coulthard': 56,
                                                'Eddie Irvine': 47, 'Jacques Villeneuve': 21, 'Damon Hill': 20,
                                                'Heinz-Harald Frentzen': 17, 'Alexander Wurz': 17,
                                                'Giancarlo Fisichella': 16, 'Ralf Schumacher': 14, 'Jean Alesi': 9,
                                                'Rubens Barrichello': 4, 'Mika Salo': 3, 'Pedro Diniz': 3,
                                                'Johnny Herbert': 1, 'Jan Magnussen': 1, 'Jarno Trulli': 1}


# 493, 494, 495
# create a function that returns dictionary with the answer on the following question :
# Create a dictionary with each grand prix(round) and its winner.


def get_round_winners(season_data):
    return {
        round_name: round_info['summary']['winner']
        for round_name, round_info in season_data['rounds'].items()
    }


assert get_round_winners(f1_1998_season) == {'australia': 'Mika Häkkinen', 'brazil': 'Mika Häkkinen',
                                             'argentina': 'Michael Schumacher', 'san_marino': 'David Coulthard',
                                             'spain': 'Mika Häkkinen', 'monaco': 'Mika Häkkinen',
                                             'canada': 'Michael Schumacher', 'france': 'Michael Schumacher',
                                             'britain': 'Michael Schumacher', 'austria': 'Mika Häkkinen',
                                             'german': 'Mika Häkkinen', 'hungary': 'Michael Schumacher',
                                             'belgium': 'Damon Hill', 'italy': 'Michael Schumacher',
                                             'luxembourg': 'Mika Häkkinen', 'japan': 'Mika Häkkinen'}


# 496, 497, 498
# create a function that returns list with the answer on the following question :
# Did brothers Michael and Ralf Schumacher stand on the podium together in 1998? If so, in which race(s)?


def find_schumacher_podiums(season_data):
    return [
        round_name.capitalize()  # Dodajemy nazwę rundy z kapitalizacją
        for round_name, round_info in season_data['rounds'].items()
        if 'Michael Schumacher' in list(round_info['race_result'].values())[:3] and 'Ralf Schumacher' in list(
            round_info['race_result'].values())[:3]
    ]


assert (find_schumacher_podiums(f1_1998_season)) == ['Italy']


# 499
# create function that takes list and element and append it to the list


def append_to_list(any_list, element):
    any_list.append(element)
    return any_list


assert append_to_list([1, 2, 3, 4], 'find_schumacher_podiums') == [1, 2, 3, 4, 'find_schumacher_podiums']


# 500
# create function that takes list and remove last element from list


def pop_from_list(any_list):
    any_list.pop()
    return any_list


assert pop_from_list([1, 2, 3, 4, 'find_schumacher_podiums']) == [1, 2, 3, 4]


# 501
# create function that takes tuple and return count method of number 3


def tuple_count(any_tuple):
    return any_tuple.count(3)


assert tuple_count((1, 2, 3, 3, 3)) == 3


# 502
# create function that takes tuple and return index for index method for number 3 in range (3, 5)


def tuple_index_check(any_tuple):
    return any_tuple.index(3, 3, 6)


assert tuple_index_check((1, 2, 4, 1, 3, 3, 14, 3)) == 4

set1 = {1, 2, 3}
set2 = {3, 4, 5, 100, 999999}


# 503
# create function that takes set and add element to it using add method


def add_element_to_set_(any_set, element):
    any_set.add(element)
    return any_set


# print(add_element_to_set_(set1, 10))
assert add_element_to_set_(set1, 10) == {10, 1, 2, 3}


# 504
# remove method for set

def remove_element_set(any_set, element):
    any_set.remove(element)
    return any_set


# print(remove_element_set(set1, 10))
assert remove_element_set(set1, 10) == {1, 2, 3}


# 505
# discard method for set

def discard_element_set(any_set, element):
    any_set.discard(element)
    return any_set


# print(discard_element_set(set1, 1))
assert discard_element_set(set1, 1) == {2, 3}


# 506
# update method for set

def update_set(any_set, any_list):
    any_set.update(any_list)
    return any_set


# print(update_set(set1, [1, 2, 3, 5, 60, 70, 800, 9, 10]))
assert update_set(set1, [1, 2, 3, 5, 60, 70, 800, 9, 10]) == {800, 1, 2, 3, 5, 70, 9, 10, 60}


# 507
# copy method for set

def copy_set(any_set):
    return set(any_set.copy())


# print(copy_set(set1))
assert copy_set(set1) == {800, 1, 2, 3, 5, 70, 9, 10, 60}


# 508
# union method for set

def union_set(any_set, any_set_2):
    return any_set.union(any_set_2)


# print(union_set(set1, set2))
assert union_set(set1, set2) == {800, 1, 2, 3, 100, 5, 70, 4, 9, 10, 60, 999999}


# 509
# union method short |

def union_set_2(any_set, any_set_2):
    return any_set | any_set_2


# print(union_set_2(set1, set2))
assert union_set_2(set1, set2) == {800, 1, 2, 3, 100, 5, 70, 4, 9, 10, 60, 999999}


# 510
# intersection method

def intersection_set(any_set, any_set_2):
    return any_set.intersection(any_set_2)


# print(intersection_set(set1, set2))
assert intersection_set(set1, set2) == {3, 5}


# 511
# intersection method short &

def intersection_set_2(any_set, any_set_2):
    return any_set & any_set_2


# print(intersection_set_2(set1, set2))
assert intersection_set_2(set1, set2) == {3, 5}


# 512
# difference method

def difference_set(any_set, any_set_2):
    return any_set.difference(any_set_2)


# print(difference_set(set1, set2))
assert difference_set(set1, set2) == {800, 1, 2, 70, 9, 10, 60}


# 513
# difference method - short

def difference_set_2(any_set, any_set_2):
    return any_set - any_set_2


# print(difference_set_2(set1, set2))
assert difference_set_2(set1, set2) == {800, 1, 2, 70, 9, 10, 60}


# 514
# symmetric difference method for set

def symmetric_difference_set(any_set, any_set_2):
    return any_set.symmetric_difference(any_set_2)


# print(symmetric_difference_set({1, 2, 3}, {2, 3, 4}))
assert symmetric_difference_set({1, 2, 3}, {2, 3, 4}) == {1, 4}


# 515
# symmetric difference method for set

def symmetric_difference_set_2(any_set, any_set_2):
    return any_set ^ any_set_2


# print(symmetric_difference_set_2({1, 2, 3}, {2, 3, 4}))
assert symmetric_difference_set_2({1, 2, 3}, {2, 3, 4}) == {1, 4}


# 515
# issubset method for set

def issubset_set(any_set, any_set_2):
    return any_set.issubset(any_set_2)


# print(issubset_set(set1, set2))
assert issubset_set(set1, set2) == False


# 516
# intersection_update method for set

def intersection_update(any_set, any_set_2):
    return any_set.intersection(any_set_2)


# print(intersection_update(set1, set2))
assert intersection_update(set1, set2) == {3, 5}


# 517
# intersection_update method for set - short  &=

def intersection_update_2(any_set, any_set_2):
    any_set &= any_set_2
    return any_set


# print(intersection_update_2(set1, set2))
assert intersection_update_2(set1, set2) == {3, 5}


# 518
# symmetric_difference_update method for set - short  ^=

def symmetric_difference_update(any_set, any_set_2):
    any_set ^= any_set_2
    return any_set


# print(symmetric_difference_update(set1, set2))
assert symmetric_difference_update(set1, set2) == {100, 4, 999999}


# 519
# symmetric_difference_update method for set

def symmetric_difference_update_2(any_set, any_set_2):
    any_set.symmetric_difference_update(any_set_2)
    return any_set


# print(symmetric_difference_update_2(set1, set2))
assert symmetric_difference_update_2(set1, set2) == {3, 5}


# 520
# difference_update method for set

def difference_update(any_set, any_set_2):
    any_set.difference_update(any_set_2)
    return any_set


# print(difference_update(set1, set2))
assert difference_update(set1, set2) == set()


# 521
# difference_update method for set short -=

def difference_update_2(any_set, any_set_2):
    any_set -= any_set_2
    return any_set


# print(difference_update_2(set1, set2))
assert difference_update_2(set1, set2) == set()


# 522
# Codewars function
# Create a method all which takes two params:
#
#     a sequence
#     a function (function pointer in C)
#
# and returns true if the function in the params returns true for every element in the sequence.
# Otherwise, it should return false. If the sequence is empty, it should return true,
# since technically nothing failed the test.
#
# Example
#
# all((1, 2, 3, 4, 5), greater_than_9) -> false
# all((1, 2, 3, 4, 5), less_than_9)    -> True

def _all(seq, fun):
    return all(map(fun, seq))


numbers = [2, 4, 6, 8]
is_even = lambda x: x % 2 == 0
assert _all(numbers, is_even) == True


# 523
# the same what # 522 but different way

def _all_2(seq, fun):
    return all(fun(item) for item in seq)


assert _all_2(numbers, is_even) == True


# 524
# Codewars
#
# Given an array of Player objects and a position (first position is 1), return the name of the chosen Player.
# name is a property of Player objects, e.g Player.name
#
# Example:
#
# duck_duck_goose([a, b, c, d], 1) should return a.name
# duck_duck_goose([a, b, c, d], 5) should return a.name

def get_player_name(players, position):
    return players[(position - 1) % len(players)].name


class Player:
    def __init__(self, name):
        self.name = name


players = [Player("Alice"), Player("Bob"), Player("Charlie")]

assert get_player_name(players, 1) == "Alice"


# 525
# create function that takes int and iterable and return index % len(iterable)
# Example
# cyclic_index(0, iterable) → 0
# cyclic_index(1, iterable) → 1
# cyclic_index(2, iterable) → 2
# cyclic_index(3, iterable) → 0
# cyclic_index(4, iterable) → 1


def cyclic_index(index, iterable):
    return index % len(iterable)


assert cyclic_index(2, iterable=[0, 1, 2]) == 2


# 527
# Create function that use closure

def outer(name):
    def inner(city):
        return f'I am {name} and I come from {city}'

    return inner


n_1 = outer('Mike Tyson')
n_2 = n_1('New York')
n_3 = n_1('Chicago')
# print(n_3)

assert n_2 == 'I am Mike Tyson and I come from New York'
assert n_3 == 'I am Mike Tyson and I come from Chicago'


# 528
# Create function that use closure for simple mathematical operation

def power(base):
    def inner(exponent):
        return base ** exponent

    return inner


power_2 = power(2)
power_3 = power_2(3)
power_4 = power_2(4)
power_5 = power_2(5)

assert power_3 == 8
assert power_4 == 16
assert power_5 == 32


# 529
# Create function that use closure for simple mathematical operation


def math_1(num):
    def inner(a, b):
        return num * (a + b)

    return inner


st = math_1(5)
sum_1 = st(3, 5)
sum_2 = st(3, 10)

assert sum_1 == 40
assert sum_2 == 65


# 530
# Create function that use closure for simple mathematical operation

def math_2(n):
    def inner(a, b):
        return (n / a) + b

    return inner


st_2 = math_2(2)
seq = st_2(1, 5)
seq_1 = st_2(2, 5)

assert seq == 7.0
assert seq_1 == 6.0


# 531
# create function that takes string and return string and
# decorator that change returned string from that funtion


def capitalize_str(fn):
    def inner(name):
        return fn(name.capitalize())

    return inner


def reverse(fn):
    def wrapper(text):
        return fn(text[::-1])

    return wrapper


def add_sth(fn):
    def in_2(txt):
        return fn(txt) + ' ,you have to go now'

    return in_2


@add_sth
@reverse
@capitalize_str
def say_hi(name):
    return f'Hi {name}'


@capitalize_str
@reverse
def say_hello(name):
    return f'Hello {name}'


a = say_hi('alice')
b = say_hello('john')

assert a == 'Hi Ecila ,you have to go now'
assert b == 'Hello nhoJ'


# 532
# create function that generate list and decorator that modify this list


def append_list(fn):
    def inner(n, c):
        any_lst = fn(n)
        any_lst.append(c)

        return any_lst

    return inner


@append_list
def create_list(n):
    return list(range(n))


n_lst = create_list(20, 1000)
# print(n_lst)
assert n_lst == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 1000]


# 533
# the same what 534 but decorator has to be take parameter

def remove_last_element(fn):
    def inner(n):
        any_lst = fn(n)
        any_lst.pop()
        return any_lst

    return inner


def insert_any_list_to_indexes(start, stop, x_lst):
    def decorator(fn):
        def wrapper(n):
            any_lst = fn(n)
            any_lst[start: stop] = x_lst
            return any_lst

        return wrapper

    return decorator


def insert_any_element_index(index, element):
    def decorator(fn):
        def wrapper(n):
            any_lst = fn(n)
            any_lst.insert(index, element)
            return any_lst

        return wrapper

    return decorator


def extend_list(extra_lst):
    def decorator(fn):
        def wrapper(n):
            any_lst = fn(n)
            any_lst.extend(extra_lst)
            return any_lst

        return wrapper

    return decorator


def append_list(c):
    def decorator(fn):
        def wrapper(n):
            any_lst = fn(n)
            any_lst.append(c)
            return any_lst

        return wrapper

    return decorator


@insert_any_list_to_indexes(7, 11, ['Candy', '777', 777, 'Chicago'])
@insert_any_element_index(5, 'Better now than never')
@remove_last_element
@extend_list([800, 900])
@append_list(1000)
def create_list(n):
    return list(range(n))


n_lst = create_list(20)
assert n_lst == [0, 1, 2, 3, 4, 'Better now than never', 5, 'Candy', '777', 777, 'Chicago', 10, 11, 12, 13, 14, 15, 16,
                 17, 18, 19, 1000, 800]

# 534

# write a function :
# volume_pyramid_without_base
# that takes height of the pyramid and volume without the base
# mathematical formula on volume pyramid : V = 1 / 3 * H * P
# H - height of pyramid
# P - the area of the base
# additionally create decorator for few bases that takes parameters of the bases and apply for the original function
# to achieve volume of the pyramid with exact base

# from decimal import Decimal, ROUND_HALF_UP
from math import tan, radians


def pyramid_polygon_n_(n, a):
    angle_in_radians = radians(180 / n)
    cot_value = 1 / tan(angle_in_radians)
    base_area = 4 * n * (a ** 2) * cot_value

    def decorator(fn):
        def wrapper(n):
            return round(fn(n) * base_area, 2)

        return wrapper

    return decorator


def pyramid_rectangle(a_rec, b_rec):
    base_area = a_rec * b_rec

    def decorator(fn):
        def wrapper(n):
            return round(fn(n) * base_area, 2)

        return wrapper

    return decorator


def pyramid_square(a_sq):
    base_area = a_sq ** 2

    def decorator(fn):
        def wrapper(n):
            return round(fn(n) * base_area, 2)

        return wrapper

    return decorator


def pyramid_triangle(a_tr, h_tr):
    base_area = 1 / 2 * a_tr * h_tr

    def decorator(fn):
        def wrapper(n):
            # result = Decimal(fn(n) * base_area).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)
            # return float(result)
            return round(fn(n) * base_area, 2)

        return wrapper

    return decorator


@pyramid_triangle(3, 5)
def volume_pyramid_without_base(h_pyr):
    return 1 / 3 * h_pyr


# print(volume_pyramid_without_base(10))
assert volume_pyramid_without_base(10) == 25.0


@pyramid_square(5)
def volume_pyramid_without_base(h_pyr):
    return 1 / 3 * h_pyr


# print(volume_pyramid_without_base(10))
assert volume_pyramid_without_base(10) == 83.33


@pyramid_rectangle(5, 8)
def volume_pyramid_without_base(h_pyr):
    return 1 / 3 * h_pyr


# print(volume_pyramid_without_base(10))
assert volume_pyramid_without_base(10) == 133.33


@pyramid_polygon_n_(6, 5)
def volume_pyramid_without_base(h_pyr):
    return 1 / 3 * h_pyr


# print(volume_pyramid_without_base(10))
assert volume_pyramid_without_base(10) == 3464.1

# 535
# Create function that use in argument lambda function and takes sentence or int
# and return list in 1st version str in 2nd version
# use generic typing from typing

from typing import Callable, TypeVar, List

T = TypeVar('T')
R = TypeVar('R')


def sentence(cb: Callable[[T], R], txt: T) -> List[R]:
    return [cb(txt)]


assert sentence(lambda x: str(x).upper(), 42) == ['42']
assert sentence(lambda x: str(x).upper(), 'ala ma kota') == ['ALA MA KOTA']


# 536
# the same but 2nd version

def sentence(cb: Callable[[T], R], txt: T) -> R:
    return cb(txt)


assert sentence(lambda x: str(x).upper(), 42) == '42'
assert sentence(lambda x: str(x).upper(), 'ala ma kota') == 'ALA MA KOTA'

# 537
# write a simple function that takes 2 parameters and return list, create generic typing

TT = TypeVar('TT', int, str)


def combine_(aa: TT, bb: TT) -> list[TT]:
    return [aa, bb]


res_1 = combine_(1, 2)
res_2 = combine_('1', '2')

assert res_1 == [1, 2]
assert res_2 == ['1', '2']

# 538
# the same what # 537 use sequence protocol during typing

U = TypeVar('U')


def magic(data_77: Sequence[U]) -> U:
    return data_77[0]


v = magic((3000, 2, 3))
v_1 = magic((100000, 2))
v_3 = magic(['Future Branch', 'Westworld'])

assert v == 3000
assert v_1 == 100000
assert v_3 == 'Future Branch'


# 539
# create function that takes unlimited positional parameters and return len from this collection , apply typing


def my_max(*args: int) -> int:
    return len(args)


x = my_max(1, 2, 3, 4, 6, 7)

assert x == 6


# 540
# create function that takes int parameters and returns tuple with list inside

def create_tuple_with_list(a, b, c, *args):
    t = a, b, c, *args
    return t


assert create_tuple_with_list(1, 2, 3, [4, 5, 6, 7]) == (1, 2, 3, [4, 5, 6, 7])


# 541
# create function that takes double list of tuples and return dict

def create_from_double_tuple_dict(d_tuple):
    return dict(d_tuple)


# print(dict(create_from_double_tuple_dict([(1, 2), (3, 4), (4, 4)])))
assert dict(create_from_double_tuple_dict([(1, 2), (3, 4), (4, 4)])) == {1: 2, 3: 4, 4: 4}

# 542
# write a simple function that takes dict and return list of values for len > 6

names_dict = {
    1: "Alexander",
    2: "Bob",
    3: "Charlotte",
    4: "Diana",
    5: "Ethan",
    6: "Fiona"
}


def create_new_lst_from_dict(any_dict):
    return [values for values in any_dict.values() if len(values) >= 6]


# print(create_new_lst_from_dict(names_dict))
assert create_new_lst_from_dict(names_dict) == ['Alexander', 'Charlotte']

# 543
# the same what 542 but function has to return dictionary for the same condition

def create_new_lst_from_dict_20(any_dict):
    return {key: value for key, value in any_dict.items() if len(value) >= 6}


# print(create_new_lst_from_dict_20(names_dict))
assert create_new_lst_from_dict_20(names_dict) == {1: 'Alexander', 3: 'Charlotte'}

# 544, 545, 546
# write function that takes any tuple and returns its elements in following order:
# a1, b1, *rest = t5
# *rest_1, a2, b2 = t5
# a3, *rest_2, b3, c3 = t5

def tuple_unpack_1(any_tuple):
    a1, b1, *rest = any_tuple
    return a1, b1, rest

# print(tuple_unpack_1((1, 2, 3, 4, 5, 6, 7)))
assert tuple_unpack_1((1, 2, 3, 4, 5, 6, 7)) == (1, 2, [3, 4, 5, 6, 7])


def tuple_unpack_2(any_tuple):
    *rest, a1, b1  = any_tuple
    return rest, a1, b1

# print(tuple_unpack_2((1, 2, 3, 4, 5, 6, 7)))
assert tuple_unpack_2((1, 2, 3, 4, 5, 6, 7)) == ([1, 2, 3, 4, 5], 6, 7)

def tuple_unpack_3(any_tuple):
    a1, *rest, b1  = any_tuple
    return a1, rest, b1

# print(tuple_unpack_3((1, 2, 3, 4, 5, 6, 7)))
assert tuple_unpack_3((1, 2, 3, 4, 5, 6, 7)) == (1, [2, 3, 4, 5, 6], 7)

# 547, 548, 549
# write the same fn what 544 but function has to take any string and return following result:
# two first elements from str and str
# two first elements from str and list , use join
# two first elements from str and list , use join - list - each one letter like seaparated index


def tuple_unpack_4(any_str):
    a1, b1, *rest = any_str
    return a1, b1, ''.join(rest)

assert tuple_unpack_4('Home is very close') == ('H', 'o', 'me is very close')


def tuple_unpack_5(any_str):
    a1, b1, *rest = any_str
    return a1, b1, ''.join(rest).split(',')

# print(tuple_unpack_5('Home is very close'))
assert tuple_unpack_5('Home is very close') == ('H', 'o', ['me is very close'])


def tuple_unpack_6(any_str):
    a1, b1, *rest = any_str
    return a1, b1, rest

# print(tuple_unpack_6('Home is very close'))
assert tuple_unpack_6('Home is very close') == ('H', 'o', ['m', 'e', ' ', 'i', 's', ' ', 'v', 'e', 'r', 'y', ' ', 'c', 'l', 'o', 's', 'e'])

# 550
# the same what 459 but fn takes a list


def tuple_unpack_7(any_str):
    a1, b1, *rest = any_str
    return a1, b1, rest

# print(tuple_unpack_7([1, 2, 3, 4, 5, 6, 7]))
assert tuple_unpack_7([1, 2, 3, 4, 5, 6, 7]) == (1, 2, [3, 4, 5, 6, 7])
