from Unit_tests.fn_map_conc_list import repeat_strings_with_map


def test_positive_list():
    assert repeat_strings_with_map(["A", "B", "C", "D"], [1, 2, 3, 4]) == ['A', 'BB', 'CCC', 'DDDD']


def test_empty_list():
    assert repeat_strings_with_map([], []) == []


def test_varied_string_lengths():
    assert repeat_strings_with_map(["Hello", "World", "Python"], [1, 2, 0]) == ['Hello', 'WorldWorld', '']


def test_repetition_with_zero():
    assert repeat_strings_with_map(["X", "Y", "Z"], [0, 0, 0]) == ['', '', '']


def test_large_numbers():
    assert repeat_strings_with_map(["a", "b"], [10, 20]) == ['aaaaaaaaaa', 'bbbbbbbbbbbbbbbbbbbb']


def test_negative_numbers():
    assert repeat_strings_with_map(["A", "B", "C"], [-1, -2, 3]) == ['', '', 'CCC']


def test_numeric_strings():
    assert repeat_strings_with_map(["1", "2", "3"], [3, 2, 1]) == ['111', '22', '3']


def test_unequal_list_lengths():
    try:
        repeat_strings_with_map(["Short", "List"], [2])
    except ValueError as e:
        assert str(e) == "function takes exactly 2 arguments (2 given)"
