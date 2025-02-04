import pytest

from Unit_tests.fn_comprehension import create_lst_


def test_positive_fn_comprehension():
    assert create_lst_(5) == [0, 1, 2, 3, 4]


def test_negative_fn_comprehension():
    assert create_lst_(-1) != [-1]


def test_zero_fn_comprehension():
    assert create_lst_(0) == []


def test_non_integer_fn_comprehension():
    with pytest.raises(TypeError):
        create_lst_('Home')


@pytest.mark.parametrize(
    "invalid_input", [3.14, (1, 2, 3), [1, 2, 3], {"key": "value"}, None, True]
)
def test_invalid_type_fn_comprehension(invalid_input):
    with pytest.raises(TypeError):
        create_lst_(invalid_input)

