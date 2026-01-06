import unittest
import sut.problem_HumanEval_84 as mod

class TestHybrid(unittest.TestCase):
    def test_min_boundary_N_zero(self):
            # Boundary test: N = 0 (minimum allowed value)
            # Digits: 0, Sum: 0, Binary: "0"
            self.assertEqual(mod.solve(0), "0")

    def test_max_boundary_N_ten_thousand(self):
            # Boundary test: N = 10000 (maximum allowed value)
            # Digits: 1, 0, 0, 0, 0, Sum: 1, Binary: "1"
            self.assertEqual(mod.solve(10000), "1")

    def test_single_digit_N_one(self):
            # Edge case / Off-by-one: Smallest non-zero N
            # Digits: 1, Sum: 1, Binary: "1"
            self.assertEqual(mod.solve(1), "1")

    def test_single_digit_N_nine(self):
            # Off-by-one: Largest single digit N, results in a multi-digit binary sum
            # Digits: 9, Sum: 9, Binary: "1001"
            self.assertEqual(mod.solve(9), "1001")

    def test_example_N_one_hundred_fifty(self):
            # Typical input, from docstring example
            # Digits: 1, 5, 0, Sum: 6, Binary: "110"
            self.assertEqual(mod.solve(150), "110")

    def test_example_N_one_hundred_forty_seven(self):
            # Typical input, from docstring example
            # Digits: 1, 4, 7, Sum: 12, Binary: "1100"
            self.assertEqual(mod.solve(147), "1100")

    def test_all_nines_N_nine_nine_nine_nine(self):
            # Extreme input: N just below max, largest possible sum of digits
            # Digits: 9, 9, 9, 9, Sum: 36, Binary: "100100"
            self.assertEqual(mod.solve(9999), "100100")

    def test_two_digits_N_eleven(self):
            # Edge case: Two identical digits, small sum
            # Digits: 1, 1, Sum: 2, Binary: "10"
            self.assertEqual(mod.solve(11), "10")

    def test_two_digits_N_ten(self):
            # Edge case: Two digits, one is zero, small sum
            # Digits: 1, 0, Sum: 1, Binary: "1"
            self.assertEqual(mod.solve(10), "1")

    def test_mid_range_N_five_five_five_five(self):
            # Unusual input: All same digits, non-trivial sum
            # Digits: 5, 5, 5, 5, Sum: 20, Binary: "10100"
            self.assertEqual(mod.solve(5555), "10100")

    def test_normal_sum_1(self):
            # N=1000, sum of digits is 1, binary is '1'.
            self.assertEqual(mod.solve(1000), "1")

    def test_normal_sum_6(self):
            # N=150, sum of digits is 6, binary is '110'.
            self.assertEqual(mod.solve(150), "110")

    def test_normal_sum_12(self):
            # N=147, sum of digits is 12, binary is '1100'.
            self.assertEqual(mod.solve(147), "1100")

    def test_normal_sum_15(self):
            # N=12345, sum of digits is 1+2+3+4+5=15, binary is '1111'.
            # Note: The JSON output for this case was "10101" (binary for 21),
            # but the description clearly states sum=15, binary='1111'.
            # Adhering to the description and postconditions.
            self.assertEqual(mod.solve(12345), "1111")

    def test_edge_zero_n(self):
            # Minimum N, sum of digits is 0, binary is '0'.
            self.assertEqual(mod.solve(0), "0")

    def test_edge_max_n(self):
            # Maximum N, sum of digits is 1, binary is '1'.
            self.assertEqual(mod.solve(10000), "1")

    def test_edge_single_digit_n(self):
            # Single digit N, sum is 9, binary is '1001'.
            self.assertEqual(mod.solve(9), "1001")

    def test_edge_max_sum_digits(self):
            # Largest sum of digits (36 for N=9999), binary is '100100'.
            self.assertEqual(mod.solve(9999), "100100")

    def test_edge_n_is_one(self):
            # N is 1, sum is 1, binary is '1'.
            self.assertEqual(mod.solve(1), "1")

    def test_error_n_less_than_zero(self):
            # N is less than 0, violating the constraint.
            with self.assertRaises(ValueError):
                mod.solve(-1)

