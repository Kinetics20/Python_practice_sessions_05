from Unit_tests.fn_multi_list import multiple_elements_list


def test_same_length_lists():
    assert multiple_elements_list([1, 2, 3], [4, 5, 6]) == [4, 10, 18]


def test_empty_list():
    assert multiple_elements_list([], []) == []


def test_first_list_longer():
    assert multiple_elements_list([1, 2, 3, 4], [5, 6]) == [5, 12]


def test_second_list_longer():
    assert multiple_elements_list([7, 8], [1, 2, 3, 4]) == [7, 16]


def test_negative_numbers():
    assert multiple_elements_list([-1, -2, -3], [-4, -5, -6]) == [4, 10, 18]


def test_mixed_numbers():
    assert multiple_elements_list([0, -2, 5], [-1, 3, 4]) == [0, -6, 20]
