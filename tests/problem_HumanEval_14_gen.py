import unittest
from sut.problem_HumanEval_14 import all_prefixes

class TestAllPrefixes(unittest.TestCase):

    def test_empty_string(self):
        # Boundary: empty string, edge case
        self.assertListEqual(all_prefixes(""), [])

    def test_single_character_string(self):
        # Boundary: single character string, edge case, off-by-one (loop for 1 iteration)
        self.assertListEqual(all_prefixes("a"), ["a"])

    def test_two_character_string(self):
        # Off-by-one: loop for 2 iterations
        self.assertListEqual(all_prefixes("ab"), ["a", "ab"])

    def test_docstring_example(self):
        # Typical input, verifies example from docstring
        self.assertListEqual(all_prefixes("abc"), ["a", "ab", "abc"])

    def test_medium_length_string(self):
        # Typical input, general case
        self.assertListEqual(all_prefixes("hello"), ["h", "he", "hel", "hell", "hello"])

    def test_string_with_spaces(self):
        # Extreme/unusual input: string containing spaces
        self.assertListEqual(all_prefixes("hi there"), ["h", "hi", "hi ", "hi t", "hi th", "hi the", "hi ther", "hi there"])

    def test_string_with_digits_and_symbols(self):
        # Extreme/unusual input: string with numbers and special characters
        self.assertListEqual(all_prefixes("123!"), ["1", "12", "123", "123!"])

    def test_string_with_all_same_characters(self):
        # Edge case: string with all identical characters, duplicate values
        self.assertListEqual(all_prefixes("aaaa"), ["a", "aa", "aaa", "aaaa"])

    def test_string_with_mixed_case(self):
        # Typical input: string with mixed upper and lower case characters
        self.assertListEqual(all_prefixes("PyThOn"), ["P", "Py", "PyT", "PyTh", "PyThO", "PyThOn"])

    def test_string_with_unicode_characters(self):
        # Extreme/unusual input: string with multi-byte unicode characters
        self.assertListEqual(all_prefixes("你好世界"), ["你", "你好", "你好世", "你好世界"])