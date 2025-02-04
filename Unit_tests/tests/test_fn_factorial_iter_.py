import pytest

from Unit_tests.fn_500_bonus import factorial_iterative


def test_positive_factorial_iterative():
    from Unit_tests.fn_500_bonus import factorial_iterative
    assert factorial_iterative(2) == 2
    assert factorial_iterative(20) == 2432902008176640000


def test_negative_factorial_iterative():
    with pytest.raises(ValueError, match="n must be positive"):
        factorial_iterative(-1)
    with pytest.raises(ValueError, match="n must be positive"):
        factorial_iterative(-100)


def test_zero_factorial_iterative():
    assert factorial_iterative(0) == 1
