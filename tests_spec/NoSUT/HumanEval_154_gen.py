import unittest
from sut.problem_HumanEval_154 import cycpattern_check

class Test_cycpattern_check(unittest.TestCase):
    def test_normal_no_rotation_substring(self):
        # Normal case: Second word is not a substring, nor are its rotations.
        self.assertFalse(cycpattern_check("abcd", "abd"))

    def test_normal_direct_substring(self):
        # Normal case: Second word is a direct substring.
        self.assertTrue(cycpattern_check("hello", "ell"))

    def test_normal_rotation_is_substring(self):
        # Normal case: A rotation of the second word ('aab') is a substring of the first word.
        self.assertTrue(cycpattern_check("abab", "baa"))

    def test_normal_rotation_is_substring_complex(self):
        # Normal case: A rotation of the second word ('imens') is a substring of the first word.
        self.assertTrue(cycpattern_check("himenss", "simen"))

    def test_edge_b_longer_than_a(self):
        # Edge case: Second word is longer than the first word.
        self.assertFalse(cycpattern_check("abc", "abcd"))

    def test_edge_b_is_empty_string(self):
        # Edge case: Second word is an empty string (empty string is a substring of any string).
        self.assertTrue(cycpattern_check("test", ""))

    def test_edge_a_is_empty_string(self):
        # Edge case: First word is an empty string, second word is not empty.
        self.assertFalse(cycpattern_check("", "abc"))

    def test_edge_both_empty_strings(self):
        # Edge case: Both words are empty strings.
        self.assertTrue(cycpattern_check("", ""))

    def test_edge_b_is_rotation_of_a_same_length(self):
        # Edge case: Second word is a rotation of the first word, and they have the same length.
        self.assertTrue(cycpattern_check("abc", "bca"))

    def test_edge_repeating_characters(self):
        # Edge case: Both words consist of repeating characters.
        self.assertTrue(cycpattern_check("aaaaa", "aa"))

    def test_error_first_input_not_string(self):
        # Error case: First input is not a string.
        with self.assertRaises(TypeError):
            cycpattern_check(123, "test")

    def test_error_second_input_not_string(self):
        # Error case: Second input is not a string.
        with self.assertRaises(TypeError):
            cycpattern_check("test", None)