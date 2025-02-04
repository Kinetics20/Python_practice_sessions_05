from Unit_tests.fn_is_anagram import is_anagram


def test_valid_anagram():
    assert is_anagram("listen", "silent") == True
    assert is_anagram("triangle", "integral") == True
    assert is_anagram("anagram", "nagaram") == True


def test_invalid_anagrams():
    assert is_anagram("hello", "world") == False
    assert is_anagram("python", "java") == False
    assert is_anagram("test", "best") == False


def test_anagrams_with_spaces_and_cases():
    assert is_anagram("Listen", "Silent") == True
    assert is_anagram("Clint Eastwood", "Old West Action") == True
    assert is_anagram("Astronomer", "Moon starer") == True


def test_anagrams_with_numbers_and_special_chars():
    assert is_anagram("123 listen!", "silent 123") == True
    assert is_anagram("An@agr@am!", "Nag a ram!!") == True


def test_empty_and_single_char_strings():
    assert is_anagram("", "") == True
    assert is_anagram("a", "a") == True
    assert is_anagram("a", "b") == False
