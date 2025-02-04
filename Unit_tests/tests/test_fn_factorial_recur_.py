import pytest

from Unit_tests.fn_500_bonus import factorial


def test_positive_factorial():
    from Unit_tests.fn_500_bonus import factorial
    assert factorial(2) == 2
    assert factorial(20) == 2432902008176640000


def test_negative_factorial():
    with pytest.raises(ValueError, match="n must be positive"):
        factorial(-1)
    with pytest.raises(ValueError, match="n must be positive"):
        factorial(-100)


def test_zero_factorial():
    assert factorial(0) == 1


def test_call_stack_overflow():
    with pytest.raises(RecursionError, match="n must be smaller than 999"):
        factorial(999)
    with pytest.raises(RecursionError, match="n must be smaller than 999"):
        factorial(999)
