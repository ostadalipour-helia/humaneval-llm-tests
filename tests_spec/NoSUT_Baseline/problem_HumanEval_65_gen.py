import unittest
import sut.problem_HumanEval_65 as mod

class TestHybrid(unittest.TestCase):
    def test_docstring_example_1(self):
            # Boundary: shift < number of digits (typical case)
            self.assertEqual(mod.circular_shift(12, 1), "21")

    def test_docstring_example_2(self):
            # Boundary: shift == number of digits (full rotation)
            self.assertEqual(mod.circular_shift(12, 2), "12")

    def test_no_shift(self):
            # Edge case: shift is zero
            self.assertEqual(mod.circular_shift(12345, 0), "12345")

    def test_shift_greater_than_digits(self):
            # Boundary: shift > number of digits (reversed case)
            self.assertEqual(mod.circular_shift(123, 4), "321")

    def test_single_digit_number(self):
            # Edge case: x is a single digit, shift > number of digits
            self.assertEqual(mod.circular_shift(7, 5), "7")

    def test_multiple_shifts_typical(self):
            # Typical input: multiple shifts, shift < number of digits
            self.assertEqual(mod.circular_shift(12345, 2), "45123")

    def test_shift_one_less_than_digits(self):
            # Boundary: shift = number of digits - 1
            self.assertEqual(mod.circular_shift(123, 2), "231")

    def test_large_number_reversed(self):
            # Extreme input: large number, shift > number of digits (reversed)
            self.assertEqual(mod.circular_shift(987654321, 10), "123456789")

    def test_zero_input(self):
            # Edge case: x is zero, shift == number of digits
            self.assertEqual(mod.circular_shift(0, 1), "0")

    def test_all_same_digits(self):
            # Unusual input: number with all identical digits
            self.assertEqual(mod.circular_shift(11111, 3), "11111")

    def test_normal_single_right_shift(self):
            # Normal case: Single right shift for a multi-digit number.
            x = 12345
            shift = 1
            expected_output = "51234"
            self.assertEqual(mod.circular_shift(x, shift), expected_output)

    def test_normal_multiple_right_shifts(self):
            # Normal case: Multiple right shifts for a multi-digit number, shift < num_digits.
            x = 12345
            shift = 3
            expected_output = "34512"
            self.assertEqual(mod.circular_shift(x, shift), expected_output)

    def test_normal_full_cycle_shift(self):
            # Normal case: Shift equals number of digits, resulting in the original number after a full cycle.
            x = 123
            shift = 3
            expected_output = "123"
            self.assertEqual(mod.circular_shift(x, shift), expected_output)

    def test_edge_zero_shift(self):
            # Edge case: Shift is zero, no change.
            x = 123
            shift = 0
            expected_output = "123"
            self.assertEqual(mod.circular_shift(x, shift), expected_output)

    def test_edge_shift_greater_than_digits(self):
            # Edge case: Shift is strictly greater than number of digits, result is reversed.
            x = 123
            shift = 4
            expected_output = "321"
            self.assertEqual(mod.circular_shift(x, shift), expected_output)

    def test_edge_single_digit_number_no_change(self):
            # Edge case: Single digit number, shift <= num_digits.
            x = 5
            shift = 1
            expected_output = "5"
            self.assertEqual(mod.circular_shift(x, shift), expected_output)

    def test_edge_single_digit_number_reversed(self):
            # Edge case: Single digit number, shift > num_digits (1), result is reversed (which is itself).
            x = 5
            shift = 2
            expected_output = "5"
            self.assertEqual(mod.circular_shift(x, shift), expected_output)

    def test_edge_input_zero(self):
            # Edge case: Input is zero, shift <= num_digits.
            x = 0
            shift = 1
            expected_output = "0"
            self.assertEqual(mod.circular_shift(x, shift), expected_output)

    def test_error_shift_not_integer(self):
            # Error case: shift is not an integer.
            x = 123
            shift = "1"
            with self.assertRaises(TypeError):
                mod.circular_shift(x, shift)

