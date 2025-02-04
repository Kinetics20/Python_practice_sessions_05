import pytest

from Unit_tests.fn_s import reverse_str


def test_positive_str():
    assert reverse_str('Where is my wallet ?') == '? tellaw ym si erehW'


def test_empty_str():
    assert reverse_str('') == ''


def test_non_str():
    with pytest.raises(TypeError):
        reverse_str([1, 2, 3])
