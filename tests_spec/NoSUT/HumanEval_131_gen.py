import unittest
from sut.problem_HumanEval_131 import digits

class Test_digits(unittest.TestCase):
    def test_single_odd_digit(self):
        # Normal case: Single odd digit.
        self.assertEqual(digits(1), 1)

    def test_multiple_odd_mixed_even(self):
        # Normal case: Multiple odd digits, mixed with even digits.
        self.assertEqual(digits(235), 15)

    def test_all_odd_digits(self):
        # Normal case: All digits are odd.
        self.assertEqual(digits(137), 21)

    def test_single_even_digit(self):
        # Edge case: Single even digit.
        self.assertEqual(digits(4), 0)

    def test_all_even_digits(self):
        # Edge case: All digits are even.
        self.assertEqual(digits(246), 0)

    def test_mixed_odd_zero(self):
        # Edge case: Contains an odd digit (1) and an even digit (0).
        self.assertEqual(digits(10), 1)

    def test_large_number_one_odd(self):
        # Edge case: Very large number with only one odd digit.
        self.assertEqual(digits(1000000000000000000), 1)

    def test_input_zero(self):
        # Error case: n is not positive (n = 0).
        with self.assertRaises(ValueError):
            digits(0)

    def test_input_negative(self):
        # Error case: n is a negative integer.
        with self.assertRaises(ValueError):
            digits(-5)

    def test_input_float(self):
        # Error case: n is a float.
        with self.assertRaises(TypeError):
            digits(3.14)

    def test_input_string(self):
        # Error case: n is a string.
        with self.assertRaises(TypeError):
            digits("abc")

    def test_largest_single_odd_digit(self):
        # Edge case: Largest single odd digit.
        self.assertEqual(digits(9), 9)

    def test_smallest_single_even_digit_positive(self):
        # Edge case: Smallest single even digit (positive).
        self.assertEqual(digits(2), 0)