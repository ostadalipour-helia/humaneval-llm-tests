import unittest
from sut.problem_HumanEval_101 import words_string

class Test_words_string(unittest.TestCase):

    def test_normal_basic_sentence(self):
        # Normal case: sentence with mixed spaces and commas
        s = "Hi, my name is John"
        expected_output = ["Hi", "my", "name", "is", "John"]
        self.assertEqual(words_string(s), expected_output)

    def test_normal_comma_separated_list(self):
        # Normal case: words separated only by commas
        s = "apple,banana,cherry"
        expected_output = ["apple", "banana", "cherry"]
        self.assertEqual(words_string(s), expected_output)

    def test_normal_space_separated_words(self):
        # Normal case: words separated only by spaces
        s = "hello world"
        expected_output = ["hello", "world"]
        self.assertEqual(words_string(s), expected_output)

    def test_edge_empty_string(self):
        # Edge case: empty input string
        s = ""
        expected_output = []
        self.assertEqual(words_string(s), expected_output)

    def test_edge_only_separators(self):
        # Edge case: string containing only spaces and commas
        s = " , ,   ,, "
        expected_output = []
        self.assertEqual(words_string(s), expected_output)

    def test_edge_single_word_with_padding(self):
        # Edge case: single word with leading/trailing separators
        s = "  singleword  "
        expected_output = ["singleword"]
        self.assertEqual(words_string(s), expected_output)

    def test_edge_multiple_consecutive_separators(self):
        # Edge case: multiple consecutive separators
        s = "word1,,word2   word3"
        expected_output = ["word1", "word2", "word3"]
        self.assertEqual(words_string(s), expected_output)

    def test_edge_complex_leading_trailing_and_multiple_separators(self):
        # Edge case: complex mix of leading/trailing and multiple separators
        s = "  word1,  word2 ,word3  "
        expected_output = ["word1", "word2", "word3"]
        self.assertEqual(words_string(s), expected_output)

    def test_error_integer_input(self):
        # Error case: input is an integer
        s = 123
        with self.assertRaises(TypeError):
            words_string(s)

    def test_error_none_input(self):
        # Error case: input is None
        s = None
        with self.assertRaises(TypeError):
            words_string(s)

    def test_error_list_input(self):
        # Error case: input is a list
        s = ["list", "of", "strings"]
        with self.assertRaises(TypeError):
            words_string(s)