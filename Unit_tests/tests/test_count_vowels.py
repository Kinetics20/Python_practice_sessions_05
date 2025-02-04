from Unit_tests.fn_500_bonus import count_vowels


def test_count_vowels():
    assert count_vowels('Home') == 2
    assert count_vowels('') == 0
    assert count_vowels('1') == 0


def test_all_vowels():
    assert count_vowels("aeiouAEIOU") == 10


def test_no_vowels():
    assert count_vowels("bcdfg") == 0


def test_with_other_characters():
    assert count_vowels("H3ll0 W0rld!") == 0


def test_long_text():
    assert count_vowels("a" * 1000) == 1000
