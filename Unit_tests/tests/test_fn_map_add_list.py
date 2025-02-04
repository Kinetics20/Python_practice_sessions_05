from Unit_tests.fn_map_add_list import add_elements_list


def test_same_length_lists():
    assert add_elements_list([1, 2, 3], [4, 5, 6]) == [5, 7, 9]


def test_empty_list():
    assert add_elements_list([], []) == []


def test_first_list_longer():
    assert add_elements_list([1, 3, 5], [1, 2]) == [2, 5]


def test_second_list_longer():
    assert add_elements_list([1, 3], [1, 2, 6]) == [2, 5]


def test_negative_numbers():
    assert add_elements_list([-1, -2, -3], [-1, -2, -5]) == [-2, -4, -8]


def test_mixed_numbers():
    assert add_elements_list([0, -2, 5], [-1, 3, 4]) == [-1, 1, 9]
