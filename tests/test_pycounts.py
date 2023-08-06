"""Tests for the pycounts module."""
from src.pycounts.pycounts import count_words
from collections import Counter

def test_count_words():
    """Test counting word from a file."""
    expected = Counter({'over': 2, 'and': 2, 'insanity': 1, 'is': 1, 'doing': 1, 'the': 1, 'same': 1, 'thing': 1, 'again': 1, 'expecting': 1, 'different': 1, 'results': 1})
    actual = count_words("./tests/einstein.txt")
    assert actual == expected, "Error : expected {}, but got {}".format(expected, actual)
