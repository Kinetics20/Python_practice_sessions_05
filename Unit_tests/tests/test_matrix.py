import pytest

from Unit_tests.matrix import create_matrix


def test_matrix_size_1():
    assert create_matrix(1) == [[1]]


def test_matrix_size_2():
    assert create_matrix(2) == [[1, 2], [3, 4]]


def test_matrix_size_3():
    assert create_matrix(3) == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def test_matrix_size_0():
    assert create_matrix(0) == []


def test_matrix_negative_size():
    assert create_matrix(-1) == []


def test_matrix_invalid_type_string():
    with pytest.raises(TypeError):
        create_matrix("5")


def test_matrix_invalid_type_float():
    with pytest.raises(TypeError):
        create_matrix(5.5)


def test_matrix_invalid_type_list():
    with pytest.raises(TypeError):
        create_matrix([1, 2, 3])
