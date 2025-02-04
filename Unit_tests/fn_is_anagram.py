import re


def is_anagram(str_1: str, str_2: str) -> bool:
    """
    Function checks if two strings are anagrams
    :param str_1: The first string
    :type str_1: str
    :param str_2: The second string
    :type str_2: str
    :return: True if both strings are anagram, False otherwise
    :rtype: bool
    :raises TypeError: if str_1, str_2 are not strings
    """
    if not isinstance(str_1, str) or not isinstance(str_2, str):
        raise TypeError("str_1 and str_2 is not of type str")

    str_1_cleaned = re.sub(r"[^a-zA-Z]", "", str_1).lower()
    str_2_cleaned = re.sub(r"[^a-zA-Z]", "", str_2).lower()

    return sorted(str_1_cleaned) == sorted(str_2_cleaned)
