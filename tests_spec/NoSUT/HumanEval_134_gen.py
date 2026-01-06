import unittest
from sut.problem_HumanEval_134 import check_if_last_char_is_a_letter

class Test_check_if_last_char_is_a_letter(unittest.TestCase):

    def test_normal_valid_simple(self):
        # Normal case: Last character is a letter preceded by a space.
        self.assertTrue(check_if_last_char_is_a_letter("apple pi e"))

    def test_normal_valid_longer_string(self):
        # Normal case: Last character is a letter preceded by a space in a longer string.
        self.assertTrue(check_if_last_char_is_a_letter("hello world a"))

    def test_normal_invalid_no_preceding_space(self):
        # Normal case: Last character is a letter but not preceded by a space.
        self.assertFalse(check_if_last_char_is_a_letter("apple pie"))

    def test_normal_invalid_last_char_is_space(self):
        # Normal case: Last character is a space, not a letter.
        self.assertFalse(check_if_last_char_is_a_letter("test string "))

    def test_edge_empty_string(self):
        # Edge case: Empty string, length < 2.
        self.assertFalse(check_if_last_char_is_a_letter(""))

    def test_edge_single_character_string(self):
        # Edge case: Single character string (letter), length < 2.
        self.assertFalse(check_if_last_char_is_a_letter("a"))

    def test_edge_two_character_valid(self):
        # Edge case: Two-character string, last is letter preceded by space.
        self.assertTrue(check_if_last_char_is_a_letter(" a"))

    def test_edge_two_character_invalid_no_space(self):
        # Edge case: Two-character string, both letters, no space.
        self.assertFalse(check_if_last_char_is_a_letter("ab"))

    def test_edge_uppercase_letter_valid(self):
        # Edge case: Uppercase letter preceded by space.
        self.assertTrue(check_if_last_char_is_a_letter(" A"))

    def test_edge_invalid_last_char_is_digit(self):
        # Edge case: Last character is a digit, not a letter.
        self.assertFalse(check_if_last_char_is_a_letter(" 1"))

    def test_error_integer_input(self):
        # Error case: Input is an integer, not a string.
        with self.assertRaises(TypeError):
            check_if_last_char_is_a_letter(123)

    def test_error_none_input(self):
        # Error case: Input is None, not a string.
        with self.assertRaises(TypeError):
            check_if_last_char_is_a_letter(None)