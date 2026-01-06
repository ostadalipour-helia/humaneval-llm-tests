import unittest
import sut.problem_HumanEval_131 as mod

class TestHybrid(unittest.TestCase):
    def test_single_odd_digit(self):
            # Boundary Test: Smallest positive odd integer.
            # Edge Case: Single digit number.
            # Expected: Product of 1 is 1.
            self.assertEqual(mod.digits(1), 1)

    def test_single_even_digit(self):
            # Boundary Test: Smallest positive even integer (excluding 0, as n is positive).
            # Edge Case: Single digit number, all even.
            # Expected: Returns 0 as per docstring.
            self.assertEqual(mod.digits(4), 0)

    def test_mixed_digits_example(self):
            # Typical Input: Example from docstring.
            # Logic Mutation: Mixed odd and even digits.
            # Expected: Product of odd digits (3*5=15).
            self.assertEqual(mod.digits(235), 15)

    def test_all_odd_digits_multi_digit(self):
            # Extreme Input: All digits are odd.
            # Logic Mutation: Ensures all odd digits are multiplied.
            # Expected: 1 * 3 * 5 * 7 * 9 = 945.
            self.assertEqual(mod.digits(13579), 945)

    def test_all_even_digits_multi_digit(self):
            # Extreme Input: All digits are even.
            # Return Value Test: Ensures the "return 0 if all digits are even" condition is met for multi-digit numbers.
            # Expected: 0.
            self.assertEqual(mod.digits(24680), 0)

    def test_mixed_digits_even_first(self):
            # Off-by-One Error Test: Even digit at the beginning.
            # Logic Mutation: Checks if the first digit is correctly identified as even and skipped.
            # Expected: Product of 1 * 3 = 3.
            self.assertEqual(mod.digits(213), 3)

    def test_mixed_digits_even_last(self):
            # Off-by-One Error Test: Even digit at the end.
            # Logic Mutation: Checks if the last digit is correctly identified as even and skipped.
            # Expected: Product of 1 * 3 = 3.
            self.assertEqual(mod.digits(132), 3)

    def test_mixed_digits_even_middle(self):
            # Off-by-One Error Test: Even digit in the middle.
            # Logic Mutation: Checks if middle digits are correctly handled.
            # Expected: Product of 1 * 3 = 3.
            self.assertEqual(mod.digits(123), 3)

    def test_number_with_zero_digit(self):
            # Edge Case: Number contains a zero digit (which is even).
            # Sign and Zero Testing: Ensures zero is treated as an even digit and doesn't affect product of odd digits.
            # Expected: Product of 1 * 3 = 3.
            self.assertEqual(mod.digits(103), 3)

    def test_large_number_with_one_odd_digit(self):
            # Extreme Input: A large number with many even digits and only one odd digit.
            # Return Value Test: Verifies that only the odd digit contributes to the product.
            # Expected: Product of 1 = 1.
            self.assertEqual(mod.digits(246810), 1)

    def test_multiple_odd_mixed_even(self):
            # Normal case: Multiple odd digits, mixed with even digits.
            self.assertEqual(mod.digits(235), 15)

    def test_mixed_odd_zero(self):
            # Edge case: Contains an odd digit (1) and an even digit (0).
            self.assertEqual(mod.digits(10), 1)

    def test_large_number_one_odd(self):
            # Edge case: Very large number with only one odd digit.
            self.assertEqual(mod.digits(1000000000000000000), 1)

    def test_input_negative(self):
            # Error case: n is a negative integer.
            with self.assertRaises(ValueError):
                mod.digits(-5)

    def test_largest_single_odd_digit(self):
            # Edge case: Largest single odd digit.
            self.assertEqual(mod.digits(9), 9)

    def test_smallest_single_even_digit_positive(self):
            # Edge case: Smallest single even digit (positive).
            self.assertEqual(mod.digits(2), 0)

