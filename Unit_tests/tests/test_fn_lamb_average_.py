import pytest
# import sys
# sys.path.append('/home/lipov/projects/Python_practice_sessions')

from Unit_tests.fn_lamb_average_ import calc_average


def test_valid_averages():
    assert calc_average([1, 2, 3, 4, 5]) == 3.0
    assert calc_average([10, 20, 30]) == 20.0
    assert calc_average([5.5, 4.5, 6.0]) == 5.333333333333333
    assert calc_average([-1, -2, -3]) == -2.0
    assert calc_average([100]) == 100.0

def test_invalid_input():
    with pytest.raises(ValueError, match="List cannot be empty"):
        calc_average([])


def test_edge_cases():
    assert calc_average([0, 0, 0]) == 0.0
    assert calc_average([1e6, 1e6, 1e6]) == 1e6
    assert calc_average([0.0001, 0.0002, 0.0003]) == pytest.approx(0.0002, rel=1e-9)
