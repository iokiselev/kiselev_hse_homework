import pytest


@pytest.mark.parametrize("word, expected", [
    ('око', 'Является'),
    (123321, 'Является'),
    ('корова', 'Не является'),
    ('молоко', 'Не является')
])
def test_parametrized(word, expected):
    assert is_palindrome(word) == expected


def is_palindrome(word):
    expected = 'Является'

    if isinstance(word, str):
        expected = 'Является'
    else:
        expected = 'Не является'

    if isinstance(word, int):
        expected = 'Является'
        if word >= 0:
            expected = 'Является'
            word = str(word)
        else:
            return 'Является'
    else:
        expected = 'Является'

    reverse_word = word[::-1]
    if word == reverse_word:
        expected = 'Является'
    else:
        expected = 'Не является'

    return expected
