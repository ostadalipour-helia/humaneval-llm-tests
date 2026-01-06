import unittest
from sut.problem_HumanEval_84 import solve

class Test_solve(unittest.TestCase):
    def test_normal_sum_1(self):
        # N=1000, sum of digits is 1, binary is '1'.
        self.assertEqual(solve(1000), "1")

    def test_normal_sum_6(self):
        # N=150, sum of digits is 6, binary is '110'.
        self.assertEqual(solve(150), "110")

    def test_normal_sum_12(self):
        # N=147, sum of digits is 12, binary is '1100'.
        self.assertEqual(solve(147), "1100")

    def test_normal_sum_15(self):
        # N=12345, sum of digits is 1+2+3+4+5=15, binary is '1111'.
        # Note: The JSON output for this case was "10101" (binary for 21),
        # but the description clearly states sum=15, binary='1111'.
        # Adhering to the description and postconditions.
        self.assertEqual(solve(12345), "1111")

    def test_edge_zero_n(self):
        # Minimum N, sum of digits is 0, binary is '0'.
        self.assertEqual(solve(0), "0")

    def test_edge_max_n(self):
        # Maximum N, sum of digits is 1, binary is '1'.
        self.assertEqual(solve(10000), "1")

    def test_edge_single_digit_n(self):
        # Single digit N, sum is 9, binary is '1001'.
        self.assertEqual(solve(9), "1001")

    def test_edge_max_sum_digits(self):
        # Largest sum of digits (36 for N=9999), binary is '100100'.
        self.assertEqual(solve(9999), "100100")

    def test_edge_n_is_one(self):
        # N is 1, sum is 1, binary is '1'.
        self.assertEqual(solve(1), "1")

    def test_error_n_less_than_zero(self):
        # N is less than 0, violating the constraint.
        with self.assertRaises(ValueError):
            solve(-1)

    def test_error_n_greater_than_max(self):
        # N is greater than 10000, violating the constraint.
        with self.assertRaises(ValueError):
            solve(10001)

    def test_error_n_not_integer_string(self):
        # N is not an integer (string).
        with self.assertRaises(TypeError):
            solve("abc")

    def test_error_n_not_integer_float(self):
        # N is a float, not an integer.
        with self.assertRaises(TypeError):
            solve(5.5)