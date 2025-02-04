import pytest

from Unit_tests.fn_comprehension_2 import create_list_compr_factorial


def test_zero():
    assert create_list_compr_factorial(0) == []


def test_one():
    assert create_list_compr_factorial(1) == [0]


def test_positive():
    assert create_list_compr_factorial(5) == [0, 1, 4, 9, 16]


def test_large():
    assert len(create_list_compr_factorial(100)) == 100


def test_negative():
    with pytest.raises(ValueError):
        create_list_compr_factorial(-5)
