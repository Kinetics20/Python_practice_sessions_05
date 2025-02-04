import pytest

from Unit_tests.fn_1 import add_up
from functions_500_ import count_square_root


def test_positive_numbers():
    assert add_up(1, 2, 3) == 1.0


def test_negative_numbers():
    assert add_up(1, 2, 3) != 5.0


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        add_up(1, 2, 0)


def test_divide_floats():
    assert add_up(0, 1, 3) == pytest.approx(0.3333333333333333
                                            , rel=1e-4)


def test_square_positive():
    assert count_square_root(4) == 2.0


def test_square_negative():
    assert count_square_root(4) != 3.0


def test_square_complex():
    assert count_square_root(-1) == 6.123233995736766e-17 + 1j