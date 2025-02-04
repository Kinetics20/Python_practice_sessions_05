from Unit_tests.fn_map_string_len import add_string_lengths_with_map


def test_positive_case():
    assert add_string_lengths_with_map(["Python", "is", "fun"], [1, 2, 3]) == [7, 4, 6]


def test_empty_list():
    assert add_string_lengths_with_map([], []) == []


def test_zero_increments():
    assert add_string_lengths_with_map(["test", "map"], [0, 0]) == [4, 3]


def test_negative_increments():
    assert add_string_lengths_with_map(["abc", "de"], [-1, -2]) == [2, 0]


def test_unequal_lengths():
    try:
        add_string_lengths_with_map(["short"], [1, 2])
    except ValueError as e:
        assert str(e) == "function takes exactly 2 arguments (2 given)"
