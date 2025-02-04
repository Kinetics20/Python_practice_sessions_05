import pytest
from Unit_tests.fn_is_even import is_even


def test_positive_is_even():
    assert is_even(4) == True


def test_negative_is_even():
    assert is_even(3) == False


def test_zero_is_even():
    assert is_even(0) == True


def test_negative_number_is_even():
    assert is_even(-2) == True
    assert is_even(-3) == False


def test_float_is_even():
    with pytest.raises(ValueError):
        is_even(3.7)


def test_integer_float_is_even():
    assert is_even(4.0) == True
    assert is_even(-6.0) == True


def test_invalid_type():
    with pytest.raises(TypeError):
        is_even('Home')
    with pytest.raises(TypeError):
        is_even(None)
    with pytest.raises(TypeError):
        is_even([2])


def test_special_float_values():
    with pytest.raises(ValueError):
        is_even(float('inf'))
    with pytest.raises(ValueError):
        is_even(float('-inf'))
    with pytest.raises(ValueError):
        is_even(float('nan'))
