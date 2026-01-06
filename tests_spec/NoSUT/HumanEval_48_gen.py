import unittest
from sut.problem_HumanEval_48 import is_palindrome

class Test_is_palindrome(unittest.TestCase):
    def test_normal_odd_length_palindrome(self):
        # A typical palindrome string.
        self.assertTrue(is_palindrome("aba"))

    def test_normal_repeating_chars_palindrome(self):
        # A palindrome string with repeating characters.
        self.assertTrue(is_palindrome("aaaaa"))

    def test_normal_non_palindrome(self):
        # A typical non-palindrome string.
        self.assertFalse(is_palindrome("zbcd"))

    def test_normal_common_palindrome(self):
        # Another common palindrome example.
        self.assertTrue(is_palindrome("racecar"))

    def test_normal_common_non_palindrome(self):
        # Another common non-palindrome example.
        self.assertFalse(is_palindrome("hello"))

    def test_edge_empty_string(self):
        # An empty string is considered a palindrome.
        self.assertTrue(is_palindrome(""))

    def test_edge_single_character(self):
        # A single-character string is considered a palindrome.
        self.assertTrue(is_palindrome("a"))

    def test_edge_two_char_palindrome(self):
        # A two-character palindrome string.
        self.assertTrue(is_palindrome("aa"))

    def test_edge_two_char_non_palindrome(self):
        # A two-character non-palindrome string.
        self.assertFalse(is_palindrome("ab"))

    def test_edge_case_sensitive_non_palindrome(self):
        # A string that would be a palindrome if case-insensitive, but is not due to case-sensitivity.
        self.assertFalse(is_palindrome("Madam"))

    def test_error_int_input(self):
        # Input is an integer instead of a string.
        with self.assertRaises(TypeError):
            is_palindrome(123)

    def test_error_none_input(self):
        # Input is None instead of a string.
        with self.assertRaises(TypeError):
            is_palindrome(None)

    def test_error_list_input(self):
        # Input is a list instead of a string.
        with self.assertRaises(TypeError):
            is_palindrome(["a", "b", "a"])