import unittest
from sut_llm.problem_HumanEval_131 import digits

class TestDigitsFunction(unittest.TestCase):

    def test_single_odd_digit(self):
        # Boundary Test: Smallest positive odd integer.
        # Edge Case: Single digit number.
        # Expected: Product of 1 is 1.
        self.assertEqual(digits(1), 1)

    def test_single_even_digit(self):
        # Boundary Test: Smallest positive even integer (excluding 0, as n is positive).
        # Edge Case: Single digit number, all even.
        # Expected: Returns 0 as per docstring.
        self.assertEqual(digits(4), 0)

    def test_mixed_digits_example(self):
        # Typical Input: Example from docstring.
        # Logic Mutation: Mixed odd and even digits.
        # Expected: Product of odd digits (3*5=15).
        self.assertEqual(digits(235), 15)

    def test_all_odd_digits_multi_digit(self):
        # Extreme Input: All digits are odd.
        # Logic Mutation: Ensures all odd digits are multiplied.
        # Expected: 1 * 3 * 5 * 7 * 9 = 945.
        self.assertEqual(digits(13579), 945)

    def test_all_even_digits_multi_digit(self):
        # Extreme Input: All digits are even.
        # Return Value Test: Ensures the "return 0 if all digits are even" condition is met for multi-digit numbers.
        # Expected: 0.
        self.assertEqual(digits(24680), 0)

    def test_mixed_digits_even_first(self):
        # Off-by-One Error Test: Even digit at the beginning.
        # Logic Mutation: Checks if the first digit is correctly identified as even and skipped.
        # Expected: Product of 1 * 3 = 3.
        self.assertEqual(digits(213), 3)

    def test_mixed_digits_even_last(self):
        # Off-by-One Error Test: Even digit at the end.
        # Logic Mutation: Checks if the last digit is correctly identified as even and skipped.
        # Expected: Product of 1 * 3 = 3.
        self.assertEqual(digits(132), 3)

    def test_mixed_digits_even_middle(self):
        # Off-by-One Error Test: Even digit in the middle.
        # Logic Mutation: Checks if middle digits are correctly handled.
        # Expected: Product of 1 * 3 = 3.
        self.assertEqual(digits(123), 3)

    def test_number_with_zero_digit(self):
        # Edge Case: Number contains a zero digit (which is even).
        # Sign and Zero Testing: Ensures zero is treated as an even digit and doesn't affect product of odd digits.
        # Expected: Product of 1 * 3 = 3.
        self.assertEqual(digits(103), 3)

    def test_large_number_with_one_odd_digit(self):
        # Extreme Input: A large number with many even digits and only one odd digit.
        # Return Value Test: Verifies that only the odd digit contributes to the product.
        # Expected: Product of 1 = 1.
        self.assertEqual(digits(246810), 1)