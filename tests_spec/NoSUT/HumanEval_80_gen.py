import unittest
from sut.problem_HumanEval_80 import is_happy

class Test_is_happy(unittest.TestCase):
    def test_normal_distinct_abcd(self):
        # Length is 4 (>=3). 'abc' are distinct, 'bcd' are distinct.
        self.assertTrue(is_happy("abcd"))

    def test_normal_distinct_abcde(self):
        # Length is 5 (>=3). 'abc', 'bcd', 'cde' are all distinct.
        self.assertTrue(is_happy("abcde"))

    def test_normal_distinct_xyzabc(self):
        # Length is 6 (>=3). All 3-consecutive substrings ('xyz', 'yza', 'zab', 'abc') have distinct characters.
        self.assertTrue(is_happy("xyzabc"))

    def test_edge_short_string_a(self):
        # Length is 1, which is less than 3.
        self.assertFalse(is_happy("a"))

    def test_edge_empty_string(self):
        # Length is 0, which is less than 3.
        self.assertFalse(is_happy(""))

    def test_edge_repeating_substring_aabb(self):
        # Length is 4 (>=3). The substring 'aab' does not have distinct characters ('a' repeats).
        self.assertFalse(is_happy("aabb"))

    def test_edge_repeating_substring_xyy(self):
        # Length is 3 (>=3). The substring 'xyy' does not have distinct characters ('y' repeats).
        self.assertFalse(is_happy("xyy"))

    def test_edge_repeating_substring_abacaba(self):
        # Length is 7 (>=3). The substring 'aba' (at index 0, 2, 4) does not have distinct characters.
        self.assertFalse(is_happy("abacaba"))

    def test_error_int_input(self):
        # Input is not a string.
        with self.assertRaises(TypeError):
            is_happy(123)

    def test_error_none_input(self):
        # Input is not a string.
        with self.assertRaises(TypeError):
            is_happy(None)

    def test_error_list_input(self):
        # Input is not a string.
        with self.assertRaises(TypeError):
            is_happy(["a", "b", "c"])