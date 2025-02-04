from Unit_tests.common_word import most_common_word


def test_most_common_word_basic():
    assert most_common_word("Home is where I feel safe, but the house I grew up in will always be home to me.") == (
        'home', 2)


def test_most_common_word_case_insensitivity():
    assert most_common_word(
        "In a small city, life is quieter, but in the City of Angels, everyone dreams big, "
        "and no one can ignore the city’s vibrant energy.") == ('city', 3)


def test_most_common_word_empty_text():
    assert most_common_word("") == ('', 0)


def test_most_common_word_special_characters():
    assert most_common_word(
        "@ The sun rises in the east, # and when&@ the $sun is$ high in the sky, "
        "^I love to si$t outside_ an&d* feel the warmth^ of the sun =on my skin.") == ('the', 6)


def test_most_common_word_tie():
    assert most_common_word("Birds fly high, and fish swim deep while birds and fish explore nature.") == ('birds', 2)


def test_most_common_word_single_word():
    assert most_common_word("Home") == ('home', 1)
