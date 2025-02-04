import pytest

from Unit_tests.fn_average_ import calc_average


def test_positive_numbers():
    assert calc_average([1, 2, 3, 4, 5]) == 3.0


def test_negative_numbers():
    assert calc_average([-1, -2, -3, -4, -5]) == -3.0


def test_mixed_numbers():
    assert calc_average([-1, 0, 1]) == 0.0


def test_single_element():
    assert calc_average([42]) == 42.0


def test_empty_list():
    with pytest.raises(ValueError, match="List cannot be empty"):
        calc_average([])
