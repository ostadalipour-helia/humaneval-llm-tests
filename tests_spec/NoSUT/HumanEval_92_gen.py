import unittest
from sut.problem_HumanEval_92 import any_int

class Test_any_int(unittest.TestCase):
    def test_normal_positive_sum(self):
        # Normal case: All integers, one is sum of others (7 == 5 + 2)
        self.assertTrue(any_int(5, 2, 7))

    def test_normal_negative_sum(self):
        # Normal case: All integers, one is sum of others (1 == 3 + (-2))
        self.assertTrue(any_int(3, -2, 1))

    def test_normal_no_sum(self):
        # Normal case: All integers, but no sum matches (3 != 2+2)
        self.assertFalse(any_int(3, 2, 2))

    def test_edge_zero_sum(self):
        # Edge case: All zeros, sum matches (0 == 0 + 0)
        self.assertTrue(any_int(0, 0, 0))

    def test_edge_mixed_zero_sum(self):
        # Edge case: Zero and positive integers, sum matches (5 == 0 + 5)
        self.assertTrue(any_int(0, 5, 5))

    def test_edge_negative_all_sum(self):
        # Edge case: All negative integers, sum matches (-7 == -5 + (-2))
        self.assertTrue(any_int(-5, -2, -7))

    def test_edge_float_one_arg(self):
        # Edge case: Not all integers (3.6 and -2.2 are floats)
        self.assertFalse(any_int(3.6, -2.2, 2))

    def test_edge_float_integer_value(self):
        # Edge case: 3.0 is a float, not an integer type, even if its value is an integer.
        self.assertFalse(any_int(3.0, 2, 5))

    def test_edge_all_floats_integer_value(self):
        # Edge case: All numbers are floats, not integers, even if values are integers.
        self.assertFalse(any_int(1.0, 2.0, 3.0))

    def test_edge_all_floats_zero_value(self):
        # Edge case: All numbers are floats, not integers, even if values are zero.
        self.assertFalse(any_int(0.0, 0.0, 0.0))

    def test_error_string_arg(self):
        # Error case: Non-numeric argument ('a')
        with self.assertRaises(TypeError):
            any_int('a', 2, 3)

    def test_error_none_arg(self):
        # Error case: Non-numeric argument (None)
        with self.assertRaises(TypeError):
            any_int(None, 2, 3)