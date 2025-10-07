import unittest
from sut_llm.problem_HumanEval_101 import words_string

class TestWordsString(unittest.TestCase):

    def test_example_mixed_separators(self):
        # Test case from docstring with mixed spaces and commas
        self.assertEqual(words_string("Hi, my name is John"), ["Hi", "my", "name", "is", "John"])

    def test_example_comma_only(self):
        # Test case from docstring with only commas
        self.assertEqual(words_string("One, two, three, four, five, six"), ["One", "two", "three", "four", "five", "six"])

    def test_only_spaces(self):
        # Test case with only spaces as separators
        self.assertEqual(words_string("apple banana cherry"), ["apple", "banana", "cherry"])

    def test_only_commas(self):
        # Test case with only commas as separators
        self.assertEqual(words_string("red,green,blue"), ["red", "green", "blue"])

    def test_mixed_separators_complex(self):
        # Test case with a more complex mix of spaces and commas
        self.assertEqual(words_string("alpha, beta gamma, delta"), ["alpha", "beta", "gamma", "delta"])

    def test_leading_trailing_spaces(self):
        # Test case with leading and trailing spaces
        self.assertEqual(words_string("  first second third  "), ["first", "second", "third"])

    def test_multiple_consecutive_spaces(self):
        # Test case with multiple consecutive spaces between words
        self.assertEqual(words_string("word1   word2    word3"), ["word1", "word2", "word3"])

    def test_multiple_consecutive_commas(self):
        # Test case with multiple consecutive commas between words
        self.assertEqual(words_string("itemA,,itemB,,,itemC"), ["itemA", "itemB", "itemC"])

    def test_empty_string(self):
        # Test case with an empty input string
        self.assertEqual(words_string(""), [])

    def test_single_word_no_separator(self):
        # Test case with a single word and no separators
        self.assertEqual(words_string("hello"), ["hello"])

if __name__ == '__main__':
    unittest.main()