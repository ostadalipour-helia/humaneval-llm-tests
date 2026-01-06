import unittest
from sut.problem_HumanEval_111 import histogram

class Test_histogram(unittest.TestCase):

    def test_normal_basic_unique_letters(self):
        # Normal case: multiple unique letters, all with frequency 1
        self.assertEqual(histogram("a b c"), {"a": 1, "b": 1, "c": 1})

    def test_normal_multiple_max_frequency(self):
        # Normal case: two letters with the same maximum frequency
        self.assertEqual(histogram("a b b a"), {"a": 2, "b": 2})

    def test_normal_single_max_frequency(self):
        # Normal case: one letter with the highest frequency
        self.assertEqual(histogram("b b b b a"), {"b": 4})

    def test_normal_complex_multiple_max(self):
        # Normal case: more complex input with multiple letters at max frequency
        self.assertEqual(histogram("m n o p m n o m"), {"m": 3})

    def test_edge_empty_string(self):
        # Edge case: empty input string
        self.assertEqual(histogram(""), {})

    def test_edge_single_letter(self):
        # Edge case: single letter input
        self.assertEqual(histogram("a"), {"a": 1})

    def test_edge_all_same_letter(self):
        # Edge case: all letters are the same
        self.assertEqual(histogram("a a a a a"), {"a": 5})

    def test_edge_alternating_multiple_max(self):
        # Edge case: alternating letters, both at max frequency
        self.assertEqual(histogram("a b a b a b"), {"a": 3, "b": 3})

    def test_error_non_string_int_input(self):
        # Error case: input is an integer, not a string
        with self.assertRaises(TypeError):
            histogram(123)

    def test_error_non_string_none_input(self):
        # Error case: input is None, not a string
        with self.assertRaises(TypeError):
            histogram(None)