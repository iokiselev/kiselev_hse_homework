import pytest


@pytest.mark.parametrize("word, expected", [
    ('око', 'Является'),
    (123321, 'Является'),
    (123231, 'Не является'),
    ('корова', 'Не является'),
    ('молоко', 'Не является')
])
def test_parametrized(word, expected):
    assert is_palindrome(word) == expected


def is_palindrome(word):
    word = str(word)
    reverse_word = word[::-1]
    if word == reverse_word:
        expected = 'Является'
    else:
        expected = 'Не является'

    return expected
