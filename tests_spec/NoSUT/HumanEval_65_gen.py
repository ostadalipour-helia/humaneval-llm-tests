import unittest
from sut.problem_HumanEval_65 import circular_shift

class Test_circular_shift(unittest.TestCase):

    def test_normal_single_right_shift(self):
        # Normal case: Single right shift for a multi-digit number.
        x = 12345
        shift = 1
        expected_output = "51234"
        self.assertEqual(circular_shift(x, shift), expected_output)

    def test_normal_multiple_right_shifts(self):
        # Normal case: Multiple right shifts for a multi-digit number, shift < num_digits.
        x = 12345
        shift = 3
        expected_output = "34512"
        self.assertEqual(circular_shift(x, shift), expected_output)

    def test_normal_full_cycle_shift(self):
        # Normal case: Shift equals number of digits, resulting in the original number after a full cycle.
        x = 123
        shift = 3
        expected_output = "123"
        self.assertEqual(circular_shift(x, shift), expected_output)

    def test_edge_zero_shift(self):
        # Edge case: Shift is zero, no change.
        x = 123
        shift = 0
        expected_output = "123"
        self.assertEqual(circular_shift(x, shift), expected_output)

    def test_edge_shift_greater_than_digits(self):
        # Edge case: Shift is strictly greater than number of digits, result is reversed.
        x = 123
        shift = 4
        expected_output = "321"
        self.assertEqual(circular_shift(x, shift), expected_output)

    def test_edge_single_digit_number_no_change(self):
        # Edge case: Single digit number, shift <= num_digits.
        x = 5
        shift = 1
        expected_output = "5"
        self.assertEqual(circular_shift(x, shift), expected_output)

    def test_edge_single_digit_number_reversed(self):
        # Edge case: Single digit number, shift > num_digits (1), result is reversed (which is itself).
        x = 5
        shift = 2
        expected_output = "5"
        self.assertEqual(circular_shift(x, shift), expected_output)

    def test_edge_input_zero(self):
        # Edge case: Input is zero, shift <= num_digits.
        x = 0
        shift = 1
        expected_output = "0"
        self.assertEqual(circular_shift(x, shift), expected_output)

    def test_error_x_not_integer(self):
        # Error case: x is not an integer.
        x = "123"
        shift = 1
        with self.assertRaises(TypeError):
            circular_shift(x, shift)

    def test_error_shift_not_integer(self):
        # Error case: shift is not an integer.
        x = 123
        shift = "1"
        with self.assertRaises(TypeError):
            circular_shift(x, shift)

    def test_error_x_negative(self):
        # Error case: x is a negative integer, violating the precondition x >= 0.
        x = -123
        shift = 1
        with self.assertRaises(ValueError):
            circular_shift(x, shift)

    def test_error_shift_negative(self):
        # Error case: shift is a negative integer, violating the precondition shift >= 0.
        x = 123
        shift = -1
        with self.assertRaises(ValueError):
            circular_shift(x, shift)