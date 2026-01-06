import unittest
from sut.problem_HumanEval_54 import same_chars

class Test_same_chars(unittest.TestCase):
    def test_normal_same_chars_different_order_frequency(self):
        # Normal case: Strings with same unique characters, different order and frequency.
        s0 = "eabcdzzzz"
        s1 = "dddzzzzzzzddeddabc"
        self.assertEqual(same_chars(s0, s1), True)

    def test_normal_s0_extra_char(self):
        # Normal case: s0 contains an extra unique character 'e' not in s1.
        s0 = "eabcd"
        s1 = "dddddddabc"
        self.assertEqual(same_chars(s0, s1), False)

    def test_normal_s1_extra_char(self):
        # Normal case: s1 contains an extra unique character 'e' not in s0.
        s0 = "abcd"
        s1 = "dddddddabce"
        self.assertEqual(same_chars(s0, s1), False)

    def test_edge_both_empty(self):
        # Edge case: Both strings are empty.
        s0 = ""
        s1 = ""
        self.assertEqual(same_chars(s0, s1), True)

    def test_edge_single_char_same(self):
        # Edge case: Both strings have a single, identical character.
        s0 = "a"
        s1 = "a"
        self.assertEqual(same_chars(s0, s1), True)

    def test_edge_one_empty_other_not(self):
        # Edge case: One string is empty, the other is not.
        s0 = "abc"
        s1 = ""
        self.assertEqual(same_chars(s0, s1), False)

    def test_edge_case_sensitive_difference(self):
        # Edge case: Strings differ only by case (case-sensitive comparison).
        s0 = "aBc"
        s1 = "AbC"
        self.assertEqual(same_chars(s0, s1), False)

    def test_edge_digits_and_symbols(self):
        # Edge case: Strings containing digits and special characters.
        s0 = "123!@"
        s1 = "!@321"
        self.assertEqual(same_chars(s0, s1), True)

    def test_error_s0_is_none(self):
        # Error case: s0 is not a string (None).
        s0 = None
        s1 = "abc"
        with self.assertRaises(TypeError):
            same_chars(s0, s1)

    def test_error_s1_is_integer(self):
        # Error case: s1 is not a string (integer).
        s0 = "abc"
        s1 = 123
        with self.assertRaises(TypeError):
            same_chars(s0, s1)

    def test_error_s0_is_list(self):
        # Error case: s0 is a list, not a string.
        s0 = ["a", "b"]
        s1 = "abc"
        with self.assertRaises(TypeError):
            same_chars(s0, s1)