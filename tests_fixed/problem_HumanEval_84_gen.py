import unittest
from sut_llm.problem_HumanEval_84 import solve

class TestSolve(unittest.TestCase):

    def test_min_boundary_N_zero(self):
        # Boundary test: N = 0 (minimum allowed value)
        # Digits: 0, Sum: 0, Binary: "0"
        self.assertEqual(solve(0), "0")

    def test_max_boundary_N_ten_thousand(self):
        # Boundary test: N = 10000 (maximum allowed value)
        # Digits: 1, 0, 0, 0, 0, Sum: 1, Binary: "1"
        self.assertEqual(solve(10000), "1")

    def test_single_digit_N_one(self):
        # Edge case / Off-by-one: Smallest non-zero N
        # Digits: 1, Sum: 1, Binary: "1"
        self.assertEqual(solve(1), "1")

    def test_single_digit_N_nine(self):
        # Off-by-one: Largest single digit N, results in a multi-digit binary sum
        # Digits: 9, Sum: 9, Binary: "1001"
        self.assertEqual(solve(9), "1001")

    def test_example_N_one_hundred_fifty(self):
        # Typical input, from docstring example
        # Digits: 1, 5, 0, Sum: 6, Binary: "110"
        self.assertEqual(solve(150), "110")

    def test_example_N_one_hundred_forty_seven(self):
        # Typical input, from docstring example
        # Digits: 1, 4, 7, Sum: 12, Binary: "1100"
        self.assertEqual(solve(147), "1100")

    def test_all_nines_N_nine_nine_nine_nine(self):
        # Extreme input: N just below max, largest possible sum of digits
        # Digits: 9, 9, 9, 9, Sum: 36, Binary: "100100"
        self.assertEqual(solve(9999), "100100")

    def test_two_digits_N_eleven(self):
        # Edge case: Two identical digits, small sum
        # Digits: 1, 1, Sum: 2, Binary: "10"
        self.assertEqual(solve(11), "10")

    def test_two_digits_N_ten(self):
        # Edge case: Two digits, one is zero, small sum
        # Digits: 1, 0, Sum: 1, Binary: "1"
        self.assertEqual(solve(10), "1")

    def test_mid_range_N_five_five_five_five(self):
        # Unusual input: All same digits, non-trivial sum
        # Digits: 5, 5, 5, 5, Sum: 20, Binary: "10100"
        self.assertEqual(solve(5555), "10100")