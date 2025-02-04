from Unit_tests.gen_example import get_first_element, get_elements_by_type


def test_get_txt_object():
    data = ['a', 'b', 'c']
    assert get_first_element(data) == 'a'


def test_get_int_object():
    data = (1, 2, 3)
    assert get_first_element(data) == 1


def test_empty_collection():
    data = []
    assert get_first_element(data) is None


def test_mixed_collection():
    data = [1, 'a', []]
    data_int = get_elements_by_type(data, int)
    assert get_first_element(data_int) == 1