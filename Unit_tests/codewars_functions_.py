def close_compare(a, b, margin=0):
    # return 0 if not abs(a - b) < margin and not a > b else (1 if not abs(a - b) > margin and not a > b else -1)
    return -1 if a < b and abs(a - b) > margin else (1 if a > b else 0)


# print(close_compare(3, 5, 3))
# print(close_compare(3, 5, 0))
# print(close_compare(2, 5, 3))
# print(close_compare(5, 5, 3))
# print(close_compare(4, 5, ))
# print(close_compare(5, 5, ))
# print(close_compare(6, 5, ))


# test.assert_equals(close_compare(4, 5), -1)
# test.assert_equals(close_compare(5, 5), 0)
# test.assert_equals(close_compare(6, 5), 1
# test.assert_equals(close_compare(2, 5, 3), 0)
# test.assert_equals(close_compare(5, 5, 3), 0)
# test.assert_equals(close_compare(8, 5, 3), 0)
# test.assert_equals(close_compare(8.1, 5, 3), 1)
# test.assert_equals(close_compare(1.99, 5, 3), -1)

def to_jaden_case(string):
    return ' '.join(word.capitalize() for word in string.split())


print(to_jaden_case('Hello world my new home is far from here'))


def to_jaden_case_1(string):
    return [word.capitalize() for word in string.split()]


# print(to_jaden_case_1('Hello world my new home is far from here'))


def get_count(sentence):
    t = []
    for word in sentence:
        if 'a' in word:
            t.append('a')
        if 'e' in word:
            t.append('e')
        if 'i' in word:
            t.append('i')
        if 'o' in word:
            t.append('o')
        if 'u' in word:
            t.append('u')
    return len(t)


print(get_count('Hello world my new home is far from here'))


def get_count_2(sentence):
    t = []
    for word in sentence:
        for vowel in 'aeiou':
            if vowel in word:
                t.append(vowel)
    return len(t)


def get_count_3(sentence):
    t = [vowel for word in sentence for vowel in 'aeiou' if vowel in word]
    return len(t)


def past(h, m, s):
    return (h * 3600000) + (m * 60000) + (s * 1000)


# print(past(0, 1, 1))

def get_middle(s):
    return s[len(s) // 2 - 1:len(s) // 2 + 1] if not len(s) % 2 else s[len(s) // 2]


print(get_middle('test'))
print(get_middle('testing'))


def abbrev_name(name):
    return '.'.join(word[0].capitalize() for word in name.split())


print(abbrev_name('Sam Harris'))


def descending_order(num):
    return int(''.join(sorted(str(num), reverse=True)))


print(descending_order(42145))


def DNA_strand(dna):
    new_l = []
    for letter in dna:
        if letter == 'A':
            new_l.append('T')
        elif letter == 'T':
            new_l.append('A')
        elif letter == 'C':
            new_l.append('G')
        elif letter == 'G':
            new_l.append('C')

    return ''.join(new_l)


def DNA_strand_1(dna):
    # return ''.join(['T' if letter == 'A' else 'A' if letter == 'T' else 'G' if letter == 'C' else 'C' for letter in dna])
    return ''.join(
        ['T' if letter == 'A' else 'A' if letter == 'T' else 'G' if letter == 'C' else 'G' for letter in dna])


# print(DNA_strand("AAAA"))
# print(DNA_strand("ATTGC"))
# print(DNA_strand_1("ATTGC"))
# print(DNA_strand("GTAT"))

def basic_op_2(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        return value1 / value2
    else:
        raise ValueError("Nieznany operator")


def basic_op(operator, value1, value2):
    return (
        value1 + value2 if operator == '+' else
        value1 - value2 if operator == '-' else
        value1 * value2 if operator == '*' else
        value1 / value2 if operator == '/' else None
    )


def basic_op_3(operator, value1, value2):
    return eval(f'{value1} {operator} {value2}')


print(basic_op_3('-', 5, 7))


def contains_all_alphabet_letters(s):
    alphabet_set = set("abcdefghijklmnopqrstuvwxyz")
    s_set = set(s.lower())  # Zakładam, że wielkość liter nie ma znaczenia

    return all(letter in s_set for letter in alphabet_set)


def is_pangram(s):
    return True if all(letter in set(s.lower()) for letter in set("abcdefghijklmnopqrstuvwxyz")) else False


# print(is_pangram("The quick brown fox jumps over the lazy dog"))

def has_duplicate_letters_1(s):
    for letter in s:
        if s.count(letter) > 1:
            return True
    return False


def has_duplicate_letters(string):
    return all(string.lower().count(letter) <= 1 for letter in string)


def is_isogram(string):
    return len(set(string.lower())) == len(string)


print(has_duplicate_letters("Dermatoglyphics"))
print(has_duplicate_letters("moose"))
print(has_duplicate_letters("aba"))
print(has_duplicate_letters(""))


def disemvowel(string_):
    # vowels = "AEIOUaeiou"

    return ''.join(char for char in string_ if char not in "AEIOUaeiou")


print(disemvowel("This website is for losers LOL!"))


def some_f(anystr):
    return ' '.join([word[::3] for word in anystr.split()])


print(some_f("Ala ma kota a kot ma ale123"))


def some_f_1(anyint):
    return int(str(anyint)[1:-1])


print(some_f_1(12398765455))


def count_by(x, n):
    new_l = []
    for i in range(x, x * n + 1, x):
        new_l.append(i)
    return new_l


print(count_by(2, 5))


def count_by_2(x, n):
    return [x for x in range(x, x * n + 1, x)]


print(count_by_2(2, 5))


def get_sum(a, b):
    return sum([num for num in range(a, b + 1)])


print(get_sum(-1, 2))


def get_sum(a, b):
    return sum(range(min(a, b), max(a, b) + 1))


def better_than_average(class_points, your_points):
    return True if len(class_points) / sum(class_points) < your_points else False


def square_sum(numbers):
    return sum([num ** 2 for num in numbers])


print(square_sum([0, 3, 4, 5]))


def find_it(seq):
    return [num for num in seq if seq.count(num) % 2][0]


print(find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]))
print(find_it([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]))


def sum_two_smallest_numbers(numbers):
    sorted_list = sorted(numbers)
    return sorted_list[0] + sorted_list[1]


print(sum_two_smallest_numbers([5, 8, 12, 18, 22]))


def maps(a):
    # return list(set([num * 2 for num in a]))
    return [num * 2 for num in set(a)]


print(maps([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]))


def lovefunc(flower1, flower2):
    return (flower1 % 2 == 1 and flower2 % 2 == 0) or (flower1 % 2 == 0 and flower2 % 2 == 1)


print(lovefunc(2, 2))
print(lovefunc(0, 2))
print(lovefunc(168, 328))


def build_tower(n):
    tower = []
    for i in range(n):
        spaces = ' ' * (n - i - 1)
        stars = '*' * (2 * i + 1)
        tower.append(spaces + stars + spaces)

    return tower


def bulid_tower_1(n):
    return [' ' * (n - i - 1) + '*' * (2 * i + 1) + ' ' * (n - i - 1) for i in range(n)]


print(bulid_tower_1(3))


def series_sum(n):
    if n == 0:
        return "0.00"

    total = 0.0
    denominator = 1

    for _ in range(n):
        total += 1 / denominator
        denominator += 3

    return "{:.2f}".format(total)


print(series_sum(1))


def open_or_senior(data):
    return ["Senior" if i >= 55 and k > 7 else "Open" for i, k in data]


def digitize(n):
    return [int(i) for i in str(n)][::-1]


def leo(oscar):
    if oscar == 88:
        return "Leo finally won the oscar! Leo is happy"
    elif oscar == 86:
        return "Not even for Wolf of wallstreet?!"
    elif not (oscar == 88 or oscar == 86) and oscar < 88:
        return "When will you give Leo an Oscar?"
    elif oscar > 88:
        return "Leo got one already!"


# print(leo(100))

def pipe_fix(nums):
    return [num for num in range(nums[0], nums[-1] + 1)]


print(pipe_fix([1, 2, 3, 4, 5, 9]))


def sum_mix(arr):
    return sum(int(i) for i in arr)


# print(sum_mix([9, 3, '7', '3']))


def hero(bullets, dragons):
    return dragons * 2 <= bullets


# print(hero(100, 40))

def cannons_ready(gunners):
    return "Fire!" if all(response == 'aye' for response in gunners.values()) else "Shiver me timbers!"


def shorten_to_date(long_date):
    return " ".join(long_date.split(", ")[:-1])


def correct(s):
    change_s = {'0': 'O', '1': 'I', '5': 'S'}
    return ''.join(change_s.get(char, char) for char in s)


def correct_1(string):
    return string.replace('1', 'I').replace('0', 'O').replace('5', 'S')


def reverse(st):
    # Your Code Here
    return ' '.join(st.split()[::-1])


def correct_polish_letters(st):
    new_dict = {'ą': 'a',
                'ć': 'c',
                'ę': 'e',
                'ł': 'l',
                'ń': 'n',
                'ó': 'o',
                'ś': 's',
                'ź': 'z',
                'ż': 'z'}

    return ''.join(new_dict[letter] if letter in new_dict else letter for letter in st)


print(correct_polish_letters('Władek ślusarz'))

# 01
import statistics


def create_list(i, j):
    return [i, j] * 4


print(create_list(1, 2))
print(create_list(True, False))

# 02

couples_dict = {
    'Alice': 28,
    'Bob': 30,
    'Charlie': 25,
    'Diana': 22,
    'Eve': 35,
    'Frank': 32
}


def list_keys(d):
    temp = []
    for key in d:
        temp.append(key)
    # return temp
    return list(d.keys())
    # return d.values()
    # return d.items()


print(list_keys(couples_dict))

# 03

word_list = ['cat', 'banana', 'carrot', 'dog', 'elephant']


def find_short_words(words):
    temp = []
    for word in words:
        if len(word) < 5:
            temp.append(word)

    return temp


l = find_short_words(word_list)
print(l)

# 04

a_list = [1, 2, 3, 4, 5]


def suma(numbers):
    result = 0
    for number in numbers:
        result += number

    return result


print(suma(a_list))


# 05
def suma_2(numbers):
    result = numbers[0]
    for number in numbers[1:]:
        result += number

    return result


print(suma_2(a_list))


# 06
def mean(numbers):
    return statistics.mean(numbers)


print(mean(a_list))


# 07
def mean_2(numbers):
    return sum(numbers) / len(numbers)


print(mean_2(a_list))

size = 5

# 08

for row in range(1, size + 1):
    for columns in range(row):
        print("*", end="")
    print()

for row in range(1, size + 1)[::-1]:
    for columns in range(row):
        print("*", end="")
    print()


# 09

def check_odd(number):
    return 'Odd' if number % 2 else 'Even'


print(check_odd(2))

# 10

mixed_list = [42, 3.14, "hello", 7, 2.718, "world", 10]


def check_val_list(items):
    new_list = []
    new_list_str = []
    new_list_int = []
    for item in items:
        if isinstance(item, float):
            new_list.append(item)
        if isinstance(item, str):
            new_list_str.append(item)
        else:
            new_list_int.append(item)
    return new_list, new_list_str, new_list_int


print(check_val_list(mixed_list))

# 11

mixed_list_2 = [42, 3.14, "hello", True, [1, 2, 3], {'key': 'value'}, None, (4, 5), 'world', False]


def create_list_last_3_index(items):
    new_list = []
    for item in items[:-4:-1]:
        new_list.append(item)
    return new_list


print(f'The new list made up of last three indexes of mixed list :\n{create_list_last_3_index(mixed_list_2)}')


def array_madness(a, b):
    return sum([num_a ** 2 for num_a in a]) > sum([num_b ** 3 for num_b in b])


print(array_madness([61], [5, 18, 26, 17, 19, 14, 28, 13, 27]))


def sum_array(arr):
    # return sum(list(set(sorted(arr)))[1:-1])
    return sum(sorted(arr)[1:-1])


print(sum_array([6, 0, 1, 10, 10]))


def sum_array_1(arr):
    return sum(sorted(arr)[1:-1]) if len(arr) > 2 else 0


print(sum_array_1([3, 5]))
print(sum_array_1([5]))
print(sum_array_1([]))


def rps(p1, p2):
    beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if beats[p1] == p2:
        return "Player 1 won!"
    if beats[p2] == p1:
        return "Player 2 won!"
    return "Draw!"


def rps_1(p1, p2):
    hand = {'rock': 0, 'paper': 1, 'scissors': 2}
    results = ['Draw!', 'Player 1 won!', 'Player 2 won!']
    return results[hand[p1] - hand[p2]]


def count_sheeps(sheep):
    # TODO May the force be with you
    return str(sheep).count('True')


def eliminate_sth_in_list(any_list):
    return [item for item in any_list if item is not bool].count(5)


print(eliminate_sth_in_list([True, True, True, False,
                             True, True, 5, True,
                             True, 2, True, False,
                             True, False, False, True,
                             True, 5, True, True,
                             False, False, True, True]))


def summation(num):
    return sum(item for item in range(1, num + 1))


def number(bus_stops):
    sum_index_0 = 0
    sum_index_1 = 0
    for element in bus_stops:
        sum_index_0 += element[0]
        sum_index_1 += element[1]
    return sum_index_0 - sum_index_1


def number_1(bus_stops):
    sum_index_0 = sum(element[0] for element in bus_stops)
    sum_index_1 = sum(element[1] for element in bus_stops)
    return sum_index_0 - sum_index_1


def number_2(bus_stops):
    return sum([stop[0] - stop[1] for stop in bus_stops])


def number_3(bus_stops):
    sum = 0
    for i in bus_stops:
        sum += i[0] - i[1]
    return sum


from functools import reduce


def grow(arr):
    return reduce(lambda x, y: x * y, arr)


def grow_1(arr):
    product = 1
    for i in arr:
        product *= i
    return product


def powers_of_two(n):
    return [2 ** num for num in range(0, n + 1)]


def how_much_i_love_you(nb_petals):
    phrases = ["I love you", "a little", "a lot", "passionately", "madly", "not at all"]

    index = (nb_petals - 1) % len(phrases)

    return phrases[index]


def find_multiples(integer, limit):
    return [num for num in range(integer, limit + 1) if not num % integer]


def count_squares(cuts):
    return (cuts + 1) ** 3 - (cuts - 1) ** 3


def count_squares_1(x):
    return 6 * x ** 2 + 2


def sort_array(source_array):
    return sorted(item for item in source_array if item % 2)


print(sort_array([5, 8, 6, 3, 4]))


def sort_array_2(source_array):
    odd_numbers = sorted(item for item in source_array if item % 2)
    return [even if even % 2 == 0 else odd_numbers.pop(0) for even in source_array]


def well(x):
    return 'Fail!' if x.count('good') == 0 else 'Publish!' if x.count('good') <= 2 else 'I smell a series!'


def well_2(x):
    if x.count('good') == 0:
        return 'Fail!'
    elif x.count('good') <= 2:
        return 'Publish!'
    else:
        return 'I smell a series!'


def cube_checker(volume, side):
    return abs(volume ** (1 / 3) - side) < 1e-10 if volume > 0 and side > 0 else False


def simple_multiplication(number):
    return 8 * number if not number % 2 else 9 * number


def rot13(message):
    result = ''
    for char in message:
        if char.isalpha():
            shift = 13 if char.islower() else -13
            result += chr(
                (ord(char) - ord('a' if char.islower() else 'A') + shift) % 26 + ord('a' if char.islower() else 'A'))
        else:
            result += char
    return result


def duplicate_encode(word):
    word = word.lower()
    return ''.join([')' if word.count(char) > 1 else '(' for char in word])


def collinearity(x1, y1, x2, y2):
    return x1 * y2 == x2 * y1


def validate_pin(pin):
    return (len(pin) == 4 or len(pin) == 6) and pin.isdigit()


def validate_pin_2(pin):
    return len(pin) in [4, 6] and pin.isdigit()


def set_alarm(employed, vacation):
    return employed and not vacation


def string_to_array(s):
    return s.split() or ['']


def string_to_array_2(string):
    return string.split(" ")


def switch_it_up(number):
    numbers_dict = {
        0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine"
    }
    if number in numbers_dict:
        return numbers_dict[number]


def switch_it_up_1(n):
    return ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine'][n]


def switch_it_up_3(number):
    dict = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        0: "Zero"}

    return dict.get(number)


def domain_name(url):
    url = url.split("//")[-1]

    if url.startswith("www."):
        url = url[4:]

    url = url.split("/")[0]

    if "." in url:
        parts = url.split(".")
        if len(parts) > 2:
            if parts[-1] in ["com", "net", "org", "jp", "za", "uk"]:
                url = parts[-3]
            else:
                url = parts[-2]
        else:
            url = parts[0]

    return url


def domain_name_1(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]


def tribonacci_1(signature, n):
    if n == 0:
        return []
    elif n <= len(signature):
        return signature[:n]
    else:
        result = signature[:]
        for i in range(n - len(signature)):
            next_term = sum(result[-3:])
            result.append(next_term)
        return result


def tribonacci(signature, n):
    res = signature[:n]
    for i in range(n - 3): res.append(sum(res[-3:]))
    return res


def printer_error(s):
    error_count = sum(1 for char in s if char > 'm')
    return f"{error_count}/{len(s)}"


def invert(lst):
    return [-x for x in lst]


def define_suit(card):
    if 'C' in card:
        return 'clubs'
    if 'D' in card:
        return 'diamonds'
    if 'H' in card:
        return 'hearts'
    if 'S' in card:
        return 'spades'


def define_suit_1(card):
    d = {'C': 'clubs', 'S': 'spades', 'D': 'diamonds', 'H': 'hearts'}
    return d[card[-1]]


def define_suit_2(card):
    return {'C': 'clubs', 'S': 'spades', 'D': 'diamonds', 'H': 'hearts'}[card[-1]]


def ensure_question(s):
    return s + '?' if not s.endswith('?') else s


def ensure_question_2(s):
    return s if s.endswith('?') else s + '?'


def ice_brick_volume(radius, bottle_length, rim_length):
    return (((2 * radius) ** 2) * (bottle_length - rim_length)) / 2


def longest(a1, a2):
    return ''.join(sorted(set(a1 + a2)))


def count_smileys(arr):
    return sum([1 for sign in arr if
                len(sign) == 2 and sign[0] in (':', ';') and sign[1] in (')', 'D') or len(sign) == 3 and sign[0] in (
                    ':', ';') and sign[1] in ('-', '~') and sign[2] in (')', 'D')])


def duck_duck_goose(players, goose):
    return players[(goose - 1) % len(players)].name


def same_case(a, b):
    if not a.isalpha() or not b.isalpha():
        return -1
    elif a.islower() == b.islower() or a.isupper() == b.isupper():
        return 1
    else:
        return 0


def same_case_1(a, b):
    return a.isupper() == b.isupper() if a.isalpha() and b.isalpha() else -1


def min_max(lst):
    return [min(lst), max(lst)]


def sum_dig_pow(a, b):
    def is_eureka(num):
        digits = [int(digit) for digit in str(num)]
        return num == sum(digit ** (index + 1) for index, digit in enumerate(digits))

    return sorted(num for num in range(a, b + 1) if is_eureka(num))


def dig_pow(n):
    return sum(int(x) ** y for y, x in enumerate(str(n), 1))


def sum_dig_pow_2(a, b):
    return [x for x in range(a, b + 1) if x == dig_pow(x)]


def sum_dig_pow_3(a, b):
    return [x for x in range(a, b + 1) if sum(int(d) ** i for i, d in enumerate(str(x), 1)) == x]


def flick_switch(lst):
    switch = True
    return [switch := not switch if word == 'flick' else switch for word in lst]


def multiply(n):
    return n * 5 ** len(str(abs(n)))


def take(arr, n):
    return arr[:n]


def usdcny(usd):
    return f"{round(usd * 6.75, 2)} Chinese Yuan"


def usdcny(usd):
    return f"{round(usd * 6.75, 2):.2f} Chinese Yuan"


def hello(name=""):
    return "Hello, World!" if not name else f'Hello, {name.capitalize()}!'


def greet(language):
    dictionary = {
        "english": "Welcome",
        "czech": "Vitejte",
        "danish": "Velkomst",
        "dutch": "Welkom",
        "estonian": "Tere tulemast",
        "finnish": "Tervetuloa",
        "flemish": "Welgekomen",
        "french": "Bienvenue",
        "german": "Willkommen",
        "irish": "Failte",
        "italian": "Benvenuto",
        "latvian": "Gaidits",
        "lithuanian": "Laukiamas",
        "polish": "Witamy",
        "spanish": "Bienvenido",
        "swedish": "Valkommen",
        "welsh": "Croeso"
    }
    return dictionary.get(language, 'Welcome')


def get_key(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key
    return None


def get_key_1(dictionary, value):
    return next((key for key, val in dictionary.items() if val == value), None)


def include(arr, item):
    return item in arr


def each_cons(lst, n):
    return [lst[i:i + n] for i in range(len(lst) - n + 1)]


def merge_arrays(arr1, arr2):
    return list(sorted(set(arr1 + arr2)))


def mouth_size(animal):
    return 'small' if animal.lower() == 'alligator' else 'wide'


def is_digit(n):
    return len(n) == 1 and n.isdigit() and int(n) in range(0, 10)


def to_freud(sentence):
    return '' if not sentence else ' '.join("sex" for item in sentence.split())


def string_clean(s):
    return ''.join(char for char in s if not char.isdigit())


def pythagorean_triple(integers):
    integers.sort()
    return integers[0] ** 2 + integers[1] ** 2 == integers[2] ** 2


def two_sum(numbers, target):
    num_indices = {}
    for i, num in enumerate(numbers):
        complement = target - num
        if complement in num_indices:
            return (num_indices[complement], i)
        num_indices[num] = i


def two_sum_2(nums, t):
    for i, x in enumerate(nums):
        for j, y in enumerate(nums):
            if i != j and x + y == t:
                return [i, j]


def dir_reduc(arr):
    opposite = {'NORTH': 'SOUTH', 'SOUTH': 'NORTH', 'EAST': 'WEST', 'WEST': 'EAST'}
    stack = []
    for direction in arr:
        if stack and stack[-1] == opposite[direction]:
            stack.pop()
        else:
            stack.append(direction)
    return stack


def sum_of_differences(arr):
    return 0 if len(arr) <= 1 else sum(
        sorted(arr, reverse=True)[i] - sorted(arr, reverse=True)[i + 1] for i in range(len(arr) - 1))


def sum_of_differences_2(arr):
    return max(arr) - min(arr) if arr else 0


class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew

    def is_worth_it(self):
        draft_after_crew = self.draft - (self.crew * 1.5)
        return draft_after_crew > 20


def if_chuck_says_so():
    return not True


def quadratic(x1, x2):
    return (1, -(x1 + x2), x1 * x2)


def integrate(coefficient, exponent):
    new_coefficient = coefficient // (exponent + 1)
    new_exponent = exponent + 1
    return f"{new_coefficient}x^{new_exponent}"


def integrate_2(coefficient, exponent):
    return f'{coefficient // (exponent + 1)}x^{exponent + 1}'


def goals(*args):
    return sum(args)


def goals_2(*a):
    return sum(a)


def calculate_years(principal, interest, tax, desired):
    years = 0
    while principal < desired:
        principal += principal * interest * (1 - tax)
        years += 1
    return years


def who_is_paying(name):
    return [name] if len(name) <= 2 else [name, name[0:2]]


def whose_move(last_player, win):
    return 'white' if last_player == 'black' and win == False else (
        'white' if last_player == 'white' and win == True else 'black')


def whoseMove_2(lastPlayer, win):
    return lastPlayer if win else 'white' if lastPlayer == 'black' else 'black'


def stringy(size):
    return ''.join(['1' if not i % 2 else '0' for i in range(size)])


def stringy_2(size):
    return ('10' * size)[:size]


def triple_trouble(str1, str2, str3):
    return ''.join([str1[i] + str2[i] + str3[i] for i in range(len(str1))])


def triple_trouble_2(one, two, three):
    return ''.join(''.join(a) for a in zip(one, two, three))


def validate_hello(greetings):
    words = {"hello": "english", "ciao": "italian", "salut": "french", "hallo": "german", "hola": "spanish",
             "ahoj": "czech republic", "czesc": "polish"}
    return any(word in greetings.lower() for word in words)


def validate_hello_2(greetings):
    return any(x in greetings.lower() for x in ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc'])


def symmetric_point(p, q):
    return [2 * q[0] - p[0], 2 * q[1] - p[1]]


def is_palindrome(s):
    return s.lower() == s.lower()[::-1]


def count(s):
    return {char: s.count(char) for char in s}


def six_toast(num):
    return abs(num - 6)


from math import factorial


def am_i_wilson(n):
    return False if n <= 1 else (factorial(n - 1) + 1) % (n * n) == 0


factorial_cache = {}


def factorial_cached(n):
    if n in factorial_cache:
        return factorial_cache[n]
    result = factorial(n)
    factorial_cache[n] = result
    return result


def am_i_wilson_2(P):
    if P <= 1:
        return False
    return (factorial_cached(P - 1) + 1) % (P * P) == 0


from math import ceil


def aspect_ratio(x: int, y: int):
    return ceil(y * (16 / 9)), y


def lowercase_count(strng):
    return sum(1 for letter in strng if letter.islower())


def lowercase_count_2(strng):
    return sum(a.islower() for a in strng)


def draw_stairs(n):
    for i in range(n):
        print(" " * i + "I")


def draw_stairs_2(n):
    return '\n'.join(' ' * i + 'I' for i in range(n))


def derive(coefficient, exponent):
    return f'{coefficient * exponent}x^{exponent - 1}'


def people_with_age_drink(age):
    if age < 14:
        return "drink toddy"
    if 14 <= age < 18:
        return "drink coke"
    if 18 <= age < 21:
        return "drink beer"
    else:
        return "drink whisky"


def people_with_age_drink_2(age):
    if age > 20: return 'drink whisky'
    if age > 17: return 'drink beer'
    if age > 13: return 'drink coke'
    return 'drink toddy'


def build_string(*args):
    return "I like {}!".format(", ".join(args))


def any_arrows(arrows):
    for arrow in arrows:
        if 'damaged' not in arrow or not arrow['damaged']:
            return True
    return False


def any_arrows_2(arrows):
    return any('damaged' not in arrow or not arrow['damaged'] for arrow in arrows)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def info(self):
        return f'{self.name}s age is {self.age}'


class Solution:
    @staticmethod
    def main(*args):
        print("Hello World!")


class Solution_2:
    def main(self):
        print('Hello World!')


import random


class Ghost:
    def __init__(self):
        self.color = random.choice(["white", "yellow", "purple", "red"])


def filter_list(l):
    return [item for item in l if isinstance(item, int)]


import random

log = []


def roll_dice():
    log.append("roll_dice")
    return random.randint(1, 6)


def move():
    log.append("move")
    print("Moving...")


def combat():
    log.append("combat")
    print("Combat...")


def get_coins():
    log.append("get_coins")
    print("Getting coins...")


def buy_health():
    log.append("buy_health")
    print("Buying health...")


def print_status():
    log.append("print_status")
    print("Printing status...")


def do_turn():
    roll_result = roll_dice()
    move()
    combat()
    get_coins()
    buy_health()
    print_status()


def do_turn_2():
    roll_dice()
    move()
    combat()
    get_coins()
    buy_health()
    print_status()


def do_turn_3():
    steps = [roll_dice, move, combat,
             get_coins, buy_health, print_status]

    for step in steps:
        step()


def move_1(position, roll):
    return (roll * 2) + position


def fake_bin(x):
    result = ''
    for num in x:
        if int(num) >= 5:
            result += '1'
        else:
            result += '0'
    return result


def fake_bin_2(x):
    return ''.join(['1' if int(digit) >= 5 else '0' for digit in x])


def is_divisible(n, x, y):
    return n % x == 0 and n % y == 0


def get_volume_of_cuboid(length, width, height):
    return length * width * height


def get_ascii(str):
    return ord(str)


from datetime import datetime, timedelta


def period_is_late(last, today, cycle_length):
    days_passed = (today - last).days
    return days_passed > cycle_length


def mango(quantity, price):
    return (quantity - quantity // 3) * price


def pillars(num_pill, dist, width):
    return 0 if num_pill <= 1 else ((num_pill - 1) * dist * 100) + (num_pill - 2) * width


def pillars_2(num_pill, dist, width):
    return dist * 100 * (num_pill - 1) + width * (num_pill - 2) * (num_pill > 1)


def add_binary(a, b):
    return str(bin(a + b))[2:]


def add_binary_1(a, b):
    return format(a + b, 'b')


def first_non_consecutive(arr):
    for i in range(len(arr) - 1):
        if arr[i + 1] != arr[i] + 1:
            return arr[i + 1]


def check_alive(health):
    return False if health <= 0 else True


def check_alive_2(health):
    return health > 0


def two_sort(array):
    return '***'.join(sorted(array)[0])


def two_sort_2(lst):
    return '***'.join(min(lst))


def duty_free(price, discount, holiday_cost):
    return holiday_cost // (price * discount / 100)


def two_highest(arg1):
    if not arg1:
        return []
    elif len(arg1) == 1:
        return arg1
    new_list = [max(arg1), max([x for x in arg1 if x < max(arg1)])]
    return new_list if new_list[0] != new_list[1] else max(arg1)


def two_highest_2(arg1):
    return sorted(set(arg1), reverse=True)[:2]


def chromosome_check(chromosome):
    return "Congratulations! You're going to have a son." if 'Y' in chromosome else "Congratulations! You're going to have a daughter."


def is_even(n):
    return False if n % 2 or isinstance(n, float) else True


def is_even_2(n):
    return not n % 2 and not isinstance(n, float)


def is_even_3(n):
    return not n % 2


def billboard(name, price=30):
    cost = 0
    for _ in range(len(name)):
        cost += price
    return cost


def distinct(seq):
    seen = set()
    return [x for x in seq if not (x in seen or seen.add(x))]


def find_short(s):
    return min(len(item) for item in s.split())


def find_shortest_word(text):
    return min((len(item), item) for item in text.split())[1]


def delete_nth(order, max_e):
    result = []
    counts = {}
    for num in order:
        if num not in counts:
            counts[num] = 0
        if counts[num] < max_e:
            result.append(num)
            counts[num] += 1
    return result


def array(s):
    return None if not s or len(s.split(',')) <= 2 else ' '.join(num for num in s.split(',')[1:-1])


def array_2(strng):
    return ' '.join(strng.split(',')[1:-1]) or None


def is_opposite(s1, s2):
    return False if not s1 and not s2 else s1.swapcase() == s2


def is_opposite_2(s1, s2):
    return False if not (s1 or s2) else s1.swapcase() == s2


def is_valid_walk(walk):
    if len(walk) != 10:
        return False

    north_south = 0
    east_west = 0

    for direction in walk:
        if direction == 'n':
            north_south += 1
        elif direction == 's':
            north_south -= 1
        elif direction == 'e':
            east_west += 1
        elif direction == 'w':
            east_west -= 1

    return north_south == 0 and east_west == 0


def isValidWalk(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')


def isValidWalk_2(walk):
    if (walk.count('n') == walk.count('s') and
            walk.count('e') == walk.count('w') and
            len(walk) == 10):
        return True
    return False


def print_array(arr):
    return ",".join([str(item) for item in arr])


def greet_5(name):
    return "Hello, my love!" if name == "Johnny" else f"Hello, {name}!"


def solution(a, b):
    return a + b + a if len(a) < len(b) else b + a + b


def friend(x):
    return [name for name in x if len(name) == 4]


def job_matching(candidate, job):
    return candidate['min_salary'] <= job['max_salary'] or (candidate['min_salary'] - 0.1 * candidate['min_salary']) <= \
        job['max_salary']


def match(candidate, job):
    return candidate['min_salary'] * 0.9 <= job['max_salary']


def solution_5(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp):
    return ((given_mass1 / molar_mass1 + given_mass2 / molar_mass2) * (temp + 273.15) * 0.082) / volume


def split_and_merge(string_, separator):
    return " ".join(separator.join(word) for word in string_.split(" "))


import re


def increment_string(s):
    match = re.search(r'(\d+)$', s)

    if match:
        num = match.group()
        num_len = len(num)
        new_num = str(int(num) + 1)
        new_num = new_num.zfill(num_len)
        return s[:match.start()] + new_num
    else:
        return s + '1'


def cookie(x):
    return f'Who ate the last cookie? It was {"Zach" if type(x) is str else "Monica" if type(x) in [int, float] else "the dog"}!'


def no_boring_zeros(n):
    return 0 if not n else int(str(n).rstrip('0'))


def no_boring_zeros_2(n):
    try:
        return int(str(n).rstrip('0'))
    except ValueError:
        return 0


def area_or_perimeter(l, w):
    return l * w if l == w else 2 * l + 2 * w


def area_or_perimeter_2(l, w):
    return l * w if l == w else (l + w) * 2


def enough(cap, on, wait):
    return 0 if cap - on >= wait else abs(cap - (on + wait))


def enough_2(cap, on, wait):
    return max(0, wait - (cap - on))


def position(alphabet):
    alphabet_dict = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': 7,
        'h': 8,
        'i': 9,
        'j': 10,
        'k': 11,
        'l': 12,
        'm': 13,
        'n': 14,
        'o': 15,
        'p': 16,
        'q': 17,
        'r': 18,
        's': 19,
        't': 20,
        'u': 21,
        'v': 22,
        'w': 23,
        'x': 24,
        'y': 25,
        'z': 26
    }

    return f'Position of alphabet: {alphabet_dict.get(alphabet)}'


def get_char(c):
    return chr(c)


def find_average(numbers):
    return 0 if not numbers else sum(numbers) / len(numbers)


def high(x):
    alphabet_dict = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': 7,
        'h': 8,
        'i': 9,
        'j': 10,
        'k': 11,
        'l': 12,
        'm': 13,
        'n': 14,
        'o': 15,
        'p': 16,
        'q': 17,
        'r': 18,
        's': 19,
        't': 20,
        'u': 21,
        'v': 22,
        'w': 23,
        'x': 24,
        'y': 25,
        'z': 26
    }

    return sum([alphabet_dict[letter] for letter in x if letter in alphabet_dict])


def high_2(x):
    alphabet_dict = {
        'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
        'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19,
        't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26
    }

    max_score = 0
    highest_word = ''

    words = x.split()
    for word in words:
        score = sum(alphabet_dict[letter] for letter in word)
        if score > max_score:
            max_score = score
            highest_word = word

    return highest_word


def seats_in_theater(tot_cols, tot_rows, col, row):
    return (tot_cols - (col - 1)) * (tot_rows - row)


def final_grade(exam, projects):
    if exam > 90 or projects > 10: return 100
    if exam > 75 and projects >= 5: return 90
    if exam > 50 and projects >= 2: return 75
    return 0


def problem(a):
    return "Error" if isinstance(a, str) else (a * 50) + 6


def problem_2(a):
    try:
        return a * 50 + 6
    except TypeError:
        return "Error"


def xor(a, b):
    return (a and not b) or (not a and b)


def xor_2(a, b):
    return a != b


def plural(n):
    return n != 1


def get_real_floor(n):
    if 0 < n < 13:
        return n - 1
    elif n <= 0:
        return n
    else:
        return n - 2


def get_real_floor_2(n):
    if n <= 0: return n
    if n < 13: return n - 1
    if n > 13: return n - 2


def multiple_of_index(arr):
    return [arr[i] for i in range(len(arr)) if i == 0 or (i != 0 and arr[i] % i == 0)] if arr[0] == 0 else [arr[i] for i
                                                                                                            in range(1,
                                                                                                                     len(arr))
                                                                                                            if arr[
                                                                                                                i] % i == 0]


def multiple_of_index_2(arr):
    return [j for i, j in enumerate(arr) if (j == 0 and i == 0) or (i != 0 and j % i == 0)]


def update_light(current):
    return {"green": "yellow", "yellow": "red", "red": "green"}[current]


def update_light_2(current):
    light_order = {'red': 'green', 'yellow': 'red', 'green': 'yellow'}

    return light_order[current]


def sum_str(a, b):
    return str(int(a or 0) + int(b or 0))


def accum_1(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))


def accum(s):
    result = ""
    for i, char in enumerate(s):
        result += char.upper() + char.lower() * i
        if i < len(s) - 1:
            result += "-"
    return result


def find(array, el):
    return array.index(el) if el in array else 'Not found'


def decrypt(text, n):
    if text in ("", None):
        return text

    ndx = len(text) // 2

    for i in range(n):
        a = text[:ndx]
        b = text[ndx:]
        text = "".join(b[i:i + 1] + a[i:i + 1] for i in range(ndx + 1))
    return text


def encrypt(text, n):
    for i in range(n):
        text = text[1::2] + text[::2]
    return text


def name_shuffler(str_):
    return ' '.join(str_.split()[::-1])


def expression_matter(a, b, c):
    return max(
        a * b * c,
        a + b + c,
        a * (b + c),
        (a + b) * c,
        a * b + c,
        a + b * c
    )


def check_for_factor(base, factor):
    return not (base % factor)


def odd_count_2(n):
    return n // 2


def odd_count(n):
    return len(range(1, n, 2))


from math import ceil


def century_2(year):
    return ceil(year / 100)


def century(year):
    return (year + 99) // 100


def no_space(x):
    return x.replace(' ', '')


def unusual_five():
    return len('abcde')


def nth_even(n):
    return 2 * (n - 1)


def mul_by_n(lst, n):
    return [item * n for item in lst]


def mix(s1, s2):
    def count_letters(s):
        counts = {}
        for char in s:
            if char.islower():
                counts[char] = counts.get(char, 0) + 1
        return counts

    s1_counts = count_letters(s1)
    s2_counts = count_letters(s2)

    result = []

    for char in set(s1_counts.keys()) | set(s2_counts.keys()):
        s1_freq = s1_counts.get(char, 0)
        s2_freq = s2_counts.get(char, 0)

        if s1_freq > 1 or s2_freq > 1:
            if s1_freq > s2_freq:
                result.append(f"1:{char * s1_freq}")
            elif s1_freq < s2_freq:
                result.append(f"2:{char * s2_freq}")
            else:
                result.append(f"=:{char * s1_freq}")

    result.sort(key=lambda x: (-len(x), x))

    return '/'.join(result)


def count_sheep(num):
    sheep_count = ""
    for i in range(1, num + 1):
        sheep_count += f"{i} sheep..."
    return sheep_count


def count_sheep_2(num):
    return ''.join(f"{i} sheep..." for i in range(1, num + 1)) if num > 0 else ''


def how_much_water(water, load, clothes):
    if clothes > 2 * load:
        return 'Too much clothes'
    elif clothes < load:
        return 'Not enough clothes'
    return round(water * 1.1 ** (clothes - load), 2)


def how_much_water_2(l, x, n):
    return "Too much clothes" if n > 2 * x else "Not enough clothes" if n < x else round(1.1 ** (n - x) * l, 2)


def get_status(is_busy):
    return {'status': 'busy'} if is_busy else {'status': 'available'}


def get_status_2(is_busy): return {'status': ("busy" if is_busy else "available")}


def bar_triang(point_a, point_b, point_c):
    return [round((point_a[0] + point_b[0] + point_c[0]) / 3, 4), round((point_a[1] + point_b[1] + point_c[1]) / 3, 4)]


def describe_age(a):
    t = "You're a(n) "
    return f"{t + 'kid'}" if a <= 12 else \
        f"{t + 'teenager'}" if 13 <= a <= 17 else \
            f"{t + 'adult'}" if 18 <= a <= 64 else \
                f"{t + 'elderly'}"


def describe_age_2(a):
    return "You're a(n) " + ('kid' if a <= 12 else 'teenager' if a <= 17 else 'adult' if a <= 64 else 'elderly')


def nb_dig(n, d):
    count = 0
    for k in range(n + 1):
        square = k * k
        square_str = str(square)
        count += square_str.count(str(d))
    return count


from math import pow


def number_to_pwr(number, p):
    return pow(number, p)


def number_to_pwr_2(number, p):
    result = 1
    for _ in range(p):
        result *= number
    return result


class Hero:
    def __init__(self, name='Hero'):
        self.name = name
        self.position = '00'
        self.health = 100
        self.damage = 5
        self.experience = 0


def create_array(n):
    res = []
    i = 1
    while i <= n:
        res += [i]
        i += 1
    return res


geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]


def goose_filter(birds):
    return [item for item in birds if item not in geese]


def subtract_sum(n):
    fruits = {
        1: 'kiwi', 2: 'pear', 3: 'kiwi', 4: 'banana', 5: 'melon',
        6: 'banana', 7: 'melon', 8: 'pineapple', 9: 'apple', 10: 'pineapple',
        11: 'cucumber', 12: 'pineapple', 13: 'cucumber', 14: 'orange',
        15: 'grape', 16: 'orange', 17: 'grape', 18: 'apple', 19: 'grape',
        20: 'cherry', 21: 'pear', 22: 'cherry', 23: 'pear', 24: 'kiwi',
        25: 'banana', 26: 'kiwi', 27: 'apple', 28: 'melon', 29: 'banana',
        30: 'melon', 31: 'pineapple', 32: 'melon', 33: 'pineapple',
        34: 'cucumber', 35: 'orange', 36: 'apple', 37: 'orange', 38: 'grape',
        39: 'orange', 40: 'grape', 41: 'cherry', 42: 'pear', 43: 'cherry',
        44: 'pear', 45: 'apple', 46: 'pear', 47: 'kiwi', 48: 'banana',
        49: 'kiwi', 50: 'banana', 51: 'melon', 52: 'pineapple', 53: 'melon',
        54: 'apple', 55: 'cucumber', 56: 'pineapple', 57: 'cucumber',
        58: 'orange', 59: 'cucumber', 60: 'orange', 61: 'grape', 62: 'cherry',
        63: 'apple', 64: 'cherry', 65: 'pear', 66: 'cherry', 67: 'pear',
        68: 'kiwi', 69: 'pear', 70: 'kiwi', 71: 'banana', 72: 'apple',
        73: 'banana', 74: 'melon', 75: 'pineapple', 76: 'melon', 77: 'pineapple',
        78: 'cucumber', 79: 'pineapple', 80: 'cucumber', 81: 'apple',
        82: 'grape', 83: 'orange', 84: 'grape', 85: 'cherry', 86: 'grape',
        87: 'cherry', 88: 'pear', 89: 'cherry', 90: 'apple', 91: 'kiwi',
        92: 'banana', 93: 'kiwi', 94: 'banana', 95: 'melon', 96: 'banana',
        97: 'melon', 98: 'pineapple', 99: 'apple', 100: 'pineapple'
    }

    while True:
        sum_of_digits = sum(int(digit) for digit in str(n))
        n -= sum_of_digits
        if n in fruits:
            return fruits[n]


# flatten_method
def flatten_and_sort(array):
    return sorted([element for row in array for element in row])


def chunk_list(lst, chunk_size):
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]


def sale_hotdogs(n):
    return n * 100 if n < 5 else 95 * n if n >= 5 and n < 10 else n * 90


def old_young(age):
    return "children" if age < 16 else "young man" if age < 50 else "old man"


def sale_hotdogs_2(n):
    return n * (100 if n < 5 else 95 if n < 10 else 90)


def sale_hotdogs_3(n):
    return n * [90, 95, 100][(n < 10) + (n < 5)]


class Ball:
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type


def zero_fuel(distance_to_pump, mpg, fuel_left):
    return mpg * fuel_left >= distance_to_pump


def sum_digits(number):
    return sum(int(unit) for unit in str(abs(number)))


def get_age(age):
    return int(age[0])


def apple(x):
    return "It's hotter than the sun!!" if int(
        x) ** 2 > 1000 else "Help yourself to a honeycomb Yorkie for the glovebox."


def is_vow(inp):
    return [chr(num) if chr(num).lower() in {'a', 'e', 'i', 'o', 'u'} else num for num in inp]


def replace_with_vowels(array):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    result = []
    for num in array:
        if chr(num).lower() in vowels:
            result.append(chr(num))
        else:
            result.append(num)
    return result


def round_to_next5(n):
    return n if n % 5 == 0 else ((n + 4) // 5) * 5


def round_to_next5_2(n):
    return n + (5 - n) % 5


def factorial_2(n):
    if n == 0:
        return 1
    else:
        score = 1
        for i in range(1, n + 1):
            score *= i
        return score


import math


def factorial_1(n):
    return math.factorial(n)


def first(seq, n=1):
    return [] if n == 0 else seq[:n]


def first_2(seq, n=1):
    return seq[:n]


def whatday(num):
    days_of_week = {
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday",
        1: "Sunday"
    }

    if num in (1, 2, 3, 4, 5, 6, 7):
        return days_of_week[num]
    return 'Wrong, please enter a number between 1 and 7'


def whatday_2(num):
    switcher = {
        1: 'Sunday',
        2: 'Monday',
        3: 'Tuesday',
        4: 'Wednesday',
        5: 'Thursday',
        6: 'Friday',
        7: 'Saturday'
    }
    return switcher.get(num, 'Wrong, please enter a number between 1 and 7')


from math import pi


def square_area(A):
    return round((2 * A / pi) ** 2, 2)


def weather_info(temp):
    c_t = (temp - 32) * (5 / 9)
    if c_t > 0:
        return f"{c_t} is above freezing temperature"
    else:
        return f"{c_t} is freezing temperature"


def multi_table(number):
    table = ""
    for i in range(1, 11):
        result = i * number
        table += f"{i} * {number} = {result}"
        if i != 10:
            table += "\n"
    return table


def multi_table_2(number):
    return '\n'.join(f'{i} * {number} = {i * number}' for i in range(1, 11))


def to_binary(n):
    return int(bin(n)[2:])


def small_enough(array, limit):
    return all(item <= limit for item in array)


def small_enough_2(array, limit):
    return max(array) <= limit


def capitalize(s):
    even_chars = ''.join(char.upper() if index % 2 == 0 else char for index, char in enumerate(s))
    odd_chars = ''.join(char.upper() if index % 2 != 0 else char for index, char in enumerate(s))
    return [even_chars, odd_chars]


def capitalize_2(s):
    result = ['', '']
    for i, c in enumerate(s):
        result[0] += c.lower() if i % 2 else c.upper()
        result[1] += c.upper() if i % 2 else c.lower()
    return result


def capitalize_3(s):
    s = ''.join(c if i % 2 else c.upper() for i, c in enumerate(s))
    return [s, s.swapcase()]


def eval_object(v):
    if "operation" in v:
        operation = v["operation"]
        if operation == "+":
            return v["a"] + v["b"]
        elif operation == "-":
            return v["a"] - v["b"]
        elif operation == "/":
            return v["a"] / v["b"]
        elif operation == "*":
            return v["a"] * v["b"]
        elif operation == "%":
            return v["a"] % v["b"]
        elif operation == "**":
            return v["a"] ** v["b"]
    return 1


def get_grade(s1, s2, s3):
    score = (s1 + s2 + s3) / 3

    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    return 'F'


def greet_1(name, owner):
    return 'Hello boss' if name == owner else 'Hello guest'


def rental_car_cost(d):
    return -50 + d * 40 if d >= 7 else (40 if d == 1 else -20 + d * 40)


def no_odds(values):
    return [item for item in values if not item % 2]


def zero(op=None):
    if op is None:
        return 0
    else:
        return op(0)


def one(op=None):
    if op is None:
        return 1
    else:
        return op(1)


def two(op=None):
    if op is None:
        return 2
    else:
        return op(2)


def three(op=None):
    if op is None:
        return 3
    else:
        return op(3)


def four(op=None):
    if op is None:
        return 4
    else:
        return op(4)


def five(op=None):
    if op is None:
        return 5
    else:
        return op(5)


def six(op=None):
    if op is None:
        return 6
    else:
        return op(6)


def seven(op=None):
    if op is None:
        return 7
    else:
        return op(7)


def eight(op=None):
    if op is None:
        return 8
    else:
        return op(8)


def nine(op=None):
    if op is None:
        return 9
    else:
        return op(9)


def plus(x):
    return lambda y: y + x


def minus(x):
    return lambda y: y - x


def times(x):
    return lambda y: y * x


def divided_by(x):
    return lambda y: y // x


def identity_1(a): return a


def zero_1(f=identity_1): return f(0)


def one_1(f=identity_1): return f(1)


def two_1(f=identity_1): return f(2)


def three_1(f=identity_1): return f(3)


def four_1(f=identity_1): return f(4)


def five_1(f=identity_1): return f(5)


def six_1(f=identity_1): return f(6)


def seven_1(f=identity_1): return f(7)


def eight_1(f=identity_1): return f(8)


def nine_1(f=identity_1): return f(9)


def plus_1(b): return lambda a: a + b


def minus_1(b): return lambda a: a - b


def times_1(b): return lambda a: a * b


def divided_by_1(b): return lambda a: a // b


def bonus_time(salary, bonus):
    return f'${salary * 10}' if bonus else f'${salary}'


def bonus_time_2(salary, bonus):
    return f"${salary * 10 if bonus else salary}"


def type_validation(variable, _type):
    return type(variable).__name__ == _type


def playerRankUp(pts):
    return "Well done! You have advanced to the qualifying stage. Win 2 out of your next 3 games to rank up." if pts >= 100 else False


from datetime import datetime


def is_today(date):
    return datetime.today().date() == date.date()


def kata_13_december(lst):
    new_l = []

    for i in lst:
        if i % 2:
            new_l.append(i)
    return new_l


def kata_13_december_2(lst):
    return [item for item in lst if item & 1]


def fillable_2(stock, merch, n):
    return merch in stock and stock[merch] >= n


def fillable_3(stock, merch, n):
    return stock.get(merch, 0) >= n


def factorial(n):
    if n < 0 or n > 12:
        raise ValueError
    return 1 if n <= 1 else n * factorial(n - 1)


def row_sum_odd_numbers(n):
    start_number = (n - 1) * n + 1

    row_sum = sum(range(start_number, start_number + 2 * n, 2))

    return row_sum


def row_sum_odd_numbers_1(n):
    return n ** 3


def uefa_euro_2016(teams, scores):
    if scores[0] == scores[1]:
        return f'At match {teams[0]} - {teams[1]}, teams played draw.'
    elif scores[1] > scores[0]:
        return f'At match {teams[0]} - {teams[1]}, {teams[1]} won!'
    return f'At match {teams[0]} - {teams[1]}, {teams[0]} won!'


def next_id(arr):
    used_ids = set(arr)
    next_id = 0
    while next_id in used_ids:
        next_id += 1

    return next_id


def odds(arr):
    return [item for item in arr if item & 1]


odds_list = lambda arr: [odd for odd in arr if odd % 2]


def approx_equals(a, b):
    return abs(a - b) <= 0.001


def parse_float(string):
    return None if any(c.isalpha() for c in string) else float(string)


def find_even_index(arr):
    n = len(arr)
    left_sum = [0] * n
    right_sum = [0] * n

    left_sum[0] = arr[0]
    for i in range(1, n):
        left_sum[i] = left_sum[i - 1] + arr[i]

    right_sum[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        right_sum[i] = right_sum[i + 1] + arr[i]

    for i in range(n):
        if left_sum[i] == right_sum[i]:
            return i

    return -1


def find_even_index_1(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i + 1:]):
            return i
    return -1


def find_equilibrium_index(arr):
    n = len(arr)

    for i in range(n):
        if sum(arr[:i]) == sum(arr[i + 1:]) and not (sum(arr[:i]) & 1):
            return i
    return -1


def solution_4(nums):
    return [] if not nums else sorted(nums)


def solut_5(nums):
    return sorted(nums or [])


def capitals(word):
    return [index for index, char in enumerate(word) if char.isupper()]


def uppercase_letters(s):
    return [char for index, char in enumerate(s) if char.isupper()]


def uppercase_letters_2(s):
    return [char for char in s if char.isupper()]


def check_uppercase_letters(s):
    return any(char.isupper() for char in s)


def isValid(formula):
    if (1 in formula and 2 in formula) or (3 in formula and 4 in formula):
        return False

    if (5 in formula and 6 not in formula) or (6 in formula and 5 not in formula):
        return False

    if 7 not in formula and 8 not in formula:
        return False

    return True


def next_item(sequence, item):
    found = False
    for i in sequence:
        if found:
            return i
        if i == item:
            found = True
    return None


def gimme(input_array):
    return input_array.index(sorted(input_array)[1])


def round_it(n):
    if '.' in str(n):
        integer_part, decimal_part = str(n).split('.')

        if len(integer_part) < len(decimal_part):
            return math.ceil(n)
        elif len(integer_part) > len(decimal_part):
            return math.floor(n)
        return round(n)
    else:
        return int(n)


def round_it_2(n):
    left, right = (len(part) for part in str(n).split("."))
    return ceil(n) if left < right else int(n) if left > right else round(n)


def spacey(array):
    string = ''
    return [string := string + item for item in array]


def spacey_2(array):
    result = []
    string = ''
    for item in array:
        string += item
        result.append(string)
    return result


def spacey_3(array):
    return [''.join(array[:i + 1]) for i in range(len(array))]


def reverse_letter(st):
    return ''.join([l for l in st if l.isalnum() and not l.isdigit()][::-1])
    # return ''.join([l for l in n if l.isalpha() ][::-1])


def meets_requirements(string):
    has_lower = False
    has_upper = False
    has_digit = False
    is_alnum = True

    for char in string:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        elif not char.isalnum():
            is_alnum = False

    return has_lower and has_upper and has_digit and len(string) >= 6 and is_alnum


# regex= r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{6,}$'

regex = (
    '^'  # start line
    '(?=.*\d)'  # must contain one digit from 0-9
    '(?=.*[a-z])'  # must contain one lowercase characters
    '(?=.*[A-Z])'  # must contain one uppercase characters
    '[a-zA-Z\d]'  # permitted characters (alphanumeric only)
    '{6,}'  # length at least 6 chars
    '$'  # end line
)

from math import gcd


def mn_lcm(m, n):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def lcm(a, b):
        return a * b // gcd(a, b)

    start = min(m, n)
    end = max(m, n)

    result = start
    for i in range(start + 1, end + 1):
        result = lcm(result, i)
    return result


def number_1_2(lines):
    return [f'{index + 1}: {value}' for index, value in enumerate(lines)]


def number_1_3(lines):
    return ['%d: %s' % v for v in enumerate(lines, 1)]


def number_1_4(lines):
    return [f'{index}: {value}' for index, value in enumerate(lines, 1)]


def find_next_square(sq):
    root = sq ** 0.5
    return -1 if (root - int(root)) != 0 else int((root + 1) ** 2)


def find_next_square_1(sq):
    root = sq ** 0.5
    if root.is_integer():
        return (root + 1) ** 2
    return -1


def odd_or_even(arr):
    return [0] if not arr else ('odd' if sum(arr) & 1 else 'even')


def odd_or_even_1_2(arr):
    return 'odd' if sum(arr) & 1 else 'even'


def thirt(n):
    seq = [1, 10, 9, 12, 3, 4]

    result = n
    sum_of_products = 0
    index = 0

    while True:
        digits = [int(d) for d in str(result)]

        for i in range(len(digits) - 1, -1, -1):
            sum_of_products += digits[i] * seq[index]
            index = (index + 1) % len(seq)

        if result == sum_of_products:
            return result
        else:
            result = sum_of_products
            sum_of_products = 0
            index = 0


def can_i_play(now_hour, start_hour, end_hour):
    if start_hour <= end_hour:
        return start_hour <= now_hour < end_hour
    else:
        return now_hour >= start_hour or now_hour < end_hour


class PokeScan:
    def __init__(self, name, level, pkmntype):
        self.name = name
        self.level = level
        self.pkmntype = pkmntype

    def info(self):
        if self.level <= 20:
            level_observation = "weak"
        elif 20 < self.level <= 50:
            level_observation = "fair"
        else:
            level_observation = "strong"

        if self.pkmntype == "water":
            type_observation = "wet"
        elif self.pkmntype == "fire":
            type_observation = "fiery"
        elif self.pkmntype == "grass":
            type_observation = "grassy"
        else:
            type_observation = "unknown"

        return f"{self.name}, a {type_observation} and {level_observation} Pokemon."


def is_it_letter(s):
    return s.isalpha()


import datetime


def week_start_date(dt):
    days_difference = dt.weekday()

    start_of_week = dt - datetime.timedelta(days=days_difference)

    return start_of_week


def week_end_date(dt):
    days_difference = 6 - dt.weekday()

    end_of_week = dt + datetime.timedelta(days=days_difference)

    return end_of_week


def tacofy(word):
    taco = ['shell']
    for letter in word.lower():
        if letter in 'aeiou':
            taco.append('beef')
        elif letter == 't':
            taco.append('tomato')
        elif letter == 'l':
            taco.append('lettuce')
        elif letter == 'c':
            taco.append('cheese')
        elif letter == 'g':
            taco.append('guacamole')
        elif letter == 's':
            taco.append('salsa')
    taco.append('shell')
    return taco


def tacofy_2(word):
    ingred = {
        'a': 'beef', 'u': 'beef', 'i': 'beef', 'o': 'beef', 'e': 'beef',
        't': 'tomato', 'c': 'cheese', 'l': 'lettuce', 'g': 'guacamole', 's': 'salsa'
    }
    return ['shell'] + [ingred[c] for c in word.lower() if c in ingred] + ['shell']


import re

TACODICT = {
    't': 'tomato',
    'l': 'lettuce',
    'c': 'cheese',
    'g': 'guacamole',
    's': 'salsa'
}


def tacofy_3(word):
    return ['shell'] + [TACODICT.get(c, 'beef') for c in re.sub('[^aeioutlcgs]+', '', word.lower())] + ['shell']


def corrections(x):
    return f'{x} is more than zero.' if x > 0 else f'{x} is equal to or less than zero.'


def sort_by_length(arr):
    return sorted(arr, key=len)


def sort_by_letter(arr):
    return sorted(arr, key=str.lower)


# print(sort_by_letter(["a", "of", "dog", "food"]))

def adjacent_element_product(array):
    max_product = float('-inf')

    for i in range(len(array) - 1):
        product = array[i] * array[i + 1]
        max_product = max(max_product, product)
    return max_product


def adjacent_element_product_2(array):
    return max(array[i] * array[i + 1] for i in range(len(array) - 1))


def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    sum_s_age = age_1 ** 2 + age_2 ** 2 + age_3 ** 2 + age_4 ** 2 + age_5 ** 2 + age_6 ** 2 + age_7 ** 2 + age_8 ** 2
    return sum_s_age ** 0.5 // 2


def predict_age_1(*ages):
    return sum(a * a for a in ages) ** .5 // 2


def solve(s):
    upper_count = sum(1 for l in s if l.isupper())
    lower_count = sum(1 for l in s if l.islower())
    return s.lower() if lower_count >= upper_count else s.upper()


def show_sequence(n):
    if not n:
        return f'0={n}'
    elif n < 0:
        return f'{n}<0'
    return '+'.join([str(i) for i in range(n + 1)]) + f' = {sum(range(n + 1))}'


def find_longest(arr):
    max_length = 0
    max_number = None
    for num in arr:
        length = len(str(num))
        if length > max_length:
            max_length = length
            max_number = num
    return max_number


def find_longest_1(arr):
    return max(arr, key=lambda x: len(str(x)))


def words_to_marks(s):
    alphabet_dict = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': 7,
        'h': 8,
        'i': 9,
        'j': 10,
        'k': 11,
        'l': 12,
        'm': 13,
        'n': 14,
        'o': 15,
        'p': 16,
        'q': 17,
        'r': 18,
        's': 19,
        't': 20,
        'u': 21,
        'v': 22,
        'w': 23,
        'x': 24,
        'y': 25,
        'z': 26
    }
    return sum([alphabet_dict[letter] for letter in s if letter in alphabet_dict])


def words_to_marks_2(s):
    return sum('_abcdefghijklmnopqrstuvwxyz'.index(e) for e in s)


def sum_cubes(n):
    return sum(n ** 3 for n in range(n + 1))


def gps(s, x):
    if len(x) <= 1:
        return 0

    max_speed = 0
    for i in range(1, len(x)):
        delta_distance = x[i] - x[i - 1]
        speed = (3600 * delta_distance) / s
        max_speed = max(max_speed, speed)

    return int(max_speed)


from collections import Counter


def highest_rank(arr):
    counter = Counter(arr)
    sorted_counter = sorted(counter.items(), key=lambda x: (-x[1], -x[0]))
    return sorted_counter[0][0]


from collections import Counter


def highest_rank_2(arr):
    counter = Counter(arr)
    sorted_counter = sorted(counter.items(), key=lambda x: (-x[1], -x[0]))
    return sorted_counter[0][0]


def remove_smallest(numbers):
    if not numbers:
        return []
    min_index = numbers.index(min(numbers))
    return numbers[:min_index] + numbers[min_index + 1:]


def remove_smallest_2(numbers):
    a = numbers[:]
    if a:
        a.remove(min(a))
    return a


def spacify(string):
    return ' '.join(string)


def sum_triangular_numbers(n):
    total_sum = 0
    for i in range(1, n + 1):
        triangular_number = (i * (i + 1)) // 2
        total_sum += triangular_number
    return total_sum if n > 0 else 0


def sum_triangular_numbers_1(n):
    return n * (n + 1) * (n + 2) / 6 if n > 0 else 0


def sum_triangular_numbers_2(n):
    total, a = 0, 0
    for i in range(n):
        a += i + 1
        total += a
    return total


def sum_triangular_numbers_3(n):
    return 0 if n < 0 else n * (n + 1) * (n + 2) // 6


def remove_url_anchor(url):
    return url[:url.index('#')] if '#' in url else url


def remove_url_anchor_2(url):
    return url.split('#')[0]


def remove_url_anchor_3(url):
    return url.partition('#')[0]


class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack

    def __str__(self): return "Fighter({}, {}, {})".format(self.name, self.health, self.damage_per_attack)

    __repr__ = __str__


def declare_winner(fighter1, fighter2, first_attacker):
    current_attacker = fighter1 if fighter1.name == first_attacker else fighter2
    current_defender = fighter2 if fighter1.name == first_attacker else fighter1

    while True:
        current_defender.health -= current_attacker.damage_per_attack
        if current_defender.health <= 0:
            return current_attacker.name
        current_attacker, current_defender = current_defender, current_attacker


def declare_winner_1(fighter1, fighter2, first_attacker):
    cur, opp = (fighter1, fighter2) if first_attacker == fighter1.name else (fighter2, fighter1)
    while cur.health > 0:
        opp.health -= cur.damage_per_attack
        cur, opp = opp, cur
    return opp.name


def switcheroo(s):
    return s.replace('a', '&').replace('b', 'a').replace('&', 'b')


def switcheroo_2(s):
    new_string = ""
    for char in s:
        if char == 'a':
            new_string += 'b'
        elif char == 'b':
            new_string += 'a'
        else:
            new_string += char
    return new_string


def switcheroo_3(s):
    return s.translate(str.maketrans('ab', 'ba'))


from math import pi


def stereometry(r, h):
    return (
        round(4 * pi * (r ** 2), 3), round(pi * (r ** 2 - h ** 2), 3), round(2 * pi * ((r ** 2 - h ** 2) ** 0.5), 3))


from math import pi, sqrt


def stereometry_1(r, h):
    return round(4 * pi * r ** 2, 3), round(pi * (radius := r ** 2 - h ** 2), 3), round(2 * pi * sqrt(radius), 3)


def get_even_numbers(arr):
    return [num for num in arr if not num & 1]


# for even if not num & 1 , for odd if num & 1

def get_even_numbers_2(arr):
    return list(filter(lambda x: not x % 2, arr))


dict_1 = {
    'a': '1',
    'e': '2',
    'i': '3',
    'o': '4',
    'u': '5'
}


def encode(s):
    encoded_string = ''
    for letter in s:
        if letter in dict_1:
            encoded_string += dict_1[letter]
        else:
            encoded_string += letter
    return encoded_string


def decode(s):
    decoded_string = ''
    for char in s:
        if char in dict_1.values():
            for letter, code in dict_1.items():
                if code == char:
                    decoded_string += letter
                    break
        else:
            decoded_string += char
    return decoded_string


tbl1 = str.maketrans("aeiou", "12345")
tbl2 = str.maketrans("12345", "aeiou")


def encode_1(st):
    return st.translate(tbl1)


def decode_1(st):
    return st.translate(tbl2)


CIPHER = ("aeiou", "12345")


def encode_2(st):
    return st.translate(str.maketrans(CIPHER[0], CIPHER[1]))


def decode_3(st):
    return st.translate(str.maketrans(CIPHER[1], CIPHER[0]))


def diamond(n):
    if n % 2 == 0 or n < 1:
        return None

    diamond_str = ""
    for i in range(n):
        spaces = abs(n // 2 - i)
        diamonds = n - 2 * spaces
        diamond_str += " " * spaces + "*" * diamonds + "\n"

    return diamond_str


def divisors(n):
    divisors_count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            divisors_count += 1
    return divisors_count


def divisors_2(n):
    return sum(n % i == 0 for i in range(1, n + 1))


def divisors_3(n):
    return sum(not n % i for i in range(1, n + 1))


def check_sum_list(l):
    return sum(l) if len(l) < 2 else sum(sorted(l)[-2:])


# print(check_sum_list([-1, 5, 5, 6, 6, 11]))

def without_last(lst):
    return lst[:-1]


def is_it_good_pass(password):
    return True if len(password) >= 8 else False


def find_longest_word(sentence):
    words = sentence.split()
    the_longest = max(words, key=len)
    return the_longest


def find_longest_word_2(sentence):
    return max(sentence.split(), key=len)


def solution_2(value):
    return f'Value is {str(value).zfill(5)}'


def filter_string(st):
    return int(''.join(x for x in st if x.isdigit()))


def contain_all_rots(strng, arr):
    return all(strng[i:] + strng[:i] in arr for i in range(len(strng)))


class Block:
    def __init__(self, dimension):
        self.width = dimension[0]
        self.length = dimension[1]
        self.height = dimension[2]

    def get_width(self):
        return self.width

    def get_length(self):
        return self.length

    def get_height(self):
        return self.height

    def get_volume(self):
        return self.width * self.length * self.height

    def get_surface_area(self):
        return 2 * (self.width * self.length + self.length * self.height + self.height * self.width)


from operator import mul


class Block_2(object):
    def __init__(self, dimensions):
        self.dimensions = dimensions

    def get_width(self):
        return self.dimensions[0]

    def get_length(self):
        return self.dimensions[1]

    def get_height(self):
        return self.dimensions[2]

    def get_volume(self):
        return reduce(mul, self.dimensions)

    def get_surface_area(self):
        w, l, h = self.dimensions
        return 2 * (w * l + l * h + w * h)


class Block_3(object):
    def __init__(self, wlh):
        self.w, self.l, self.h = w, l, h = wlh
        self.v = w * h * l
        self.a = 2 * (w * l + w * h + l * h)

    def get_width(self):        return self.w

    def get_length(self):       return self.l

    def get_height(self):       return self.h

    def get_volume(self):       return self.v

    def get_surface_area(self): return self.a


def data_reverse(data):
    byte_chunks = [data[i:i + 8] for i in range(0, len(data), 8)]

    reversed_chunks = byte_chunks[::-1]

    return [bit for chunk in reversed_chunks for bit in chunk]


def data_reverse_2(data):
    res = []

    for i in range(len(data) - 8, -1, -8):
        res.extend(data[i:i + 8])

    return res


def data_reverse_3(data):
    return [b for a in range(len(data) - 8, -1, -8) for b in data[a:a + 8]]


def generate_custom_dict():
    alphabet = {i + 1: chr(122 - i) for i in range(26)}

    special_chars = {27: '!', 28: '?', 29: ' '}

    return {**alphabet, **special_chars}


custom_dict = generate_custom_dict()


def switcher(arr):
    return ''.join([custom_dict[int(x)] for x in arr if int(x) in custom_dict])


chars = "_zyxwvutsrqponmlkjihgfedcba!? "


def switcher_2(arr):
    return "".join(chars[int(i)] for i in arr if i != "0")


def switcher_3(arr):
    d = {str(i): chr(123 - i) for i in range(1, 27)}
    d.update({'27': '!'})
    d.update({'28': '?'})
    d.update({'29': ' '})
    d.update({'0': ''})
    return ''.join([d[str(i)] for i in arr])


def calc(x):
    total1 = ''.join(str(ord(char)) for char in x)

    total2 = total1.replace('7', '1')

    sum_total1 = sum(int(digit) for digit in total1)
    sum_total2 = sum(int(digit) for digit in total2)

    return sum_total1 - sum_total2


def calc_2(x):
    return ''.join(str(ord(ch)) for ch in x).count('7') * 6


def array_leaders(numbers):
    leaders = []

    for i in range(len(numbers)):
        right_sum = sum(numbers[i + 1:])

        if numbers[i] > right_sum:
            leaders.append(numbers[i])
    return leaders


def array_leaders_2(numbers):
    return [n for (i, n) in enumerate(numbers) if n > sum(numbers[(i + 1):])]


def greet_45(name):
    return f'Hello {name.lower().title()}!'


import re


def abbreviate(text):
    def abbreviate_word(word):
        if len(word) >= 4:
            return f"{word[0]}{len(word) - 2}{word[-1]}"
        return word

    result = []
    for part in re.split(r'([^a-zA-Z]+)', text):
        if part.isalpha():
            result.append(abbreviate_word(part))
        else:
            result.append(part)

    return ''.join(result)
