import pytest
from Unit_tests.fn_dogs_age import dogs_age_2


def test_valid_age_with_integer():
    assert dogs_age_2(2) == 21


def test_valid_age_with_float():
    assert dogs_age_2(3.5) == 27.0


def test_boundary_cases():
    assert dogs_age_2(2) == 21
    assert dogs_age_2(0.5) == 5.25
    assert dogs_age_2(2.5) == 23


def test_very_small_positive_age():
    assert dogs_age_2(0.001) == 0.0105


def test_invalid_negative_age():
    with pytest.raises(ValueError):
        dogs_age_2(-1)


def test_invalid_zero_age():
    with pytest.raises(ValueError):
        dogs_age_2(0)


def test_invalid_type_string():
    with pytest.raises(TypeError):
        dogs_age_2("dog")


def test_invalid_type_bool():
    with pytest.raises(TypeError):
        dogs_age_2(True)


def test_invalid_type_none():
    with pytest.raises(TypeError):
        dogs_age_2(None)


def test_infinity_value():
    with pytest.raises(ValueError):
        dogs_age_2(float("inf"))
