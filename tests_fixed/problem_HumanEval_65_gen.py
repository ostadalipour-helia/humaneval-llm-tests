import unittest
from sut_llm.problem_HumanEval_65 import circular_shift

class TestCircularShift(unittest.TestCase):

    def test_docstring_example_1(self):
        # Boundary: shift < number of digits (typical case)
        self.assertEqual(circular_shift(12, 1), "21")

    def test_docstring_example_2(self):
        # Boundary: shift == number of digits (full rotation)
        self.assertEqual(circular_shift(12, 2), "12")

    def test_no_shift(self):
        # Edge case: shift is zero
        self.assertEqual(circular_shift(12345, 0), "12345")

    def test_shift_greater_than_digits(self):
        # Boundary: shift > number of digits (reversed case)
        self.assertEqual(circular_shift(123, 4), "321")

    def test_single_digit_number(self):
        # Edge case: x is a single digit, shift > number of digits
        self.assertEqual(circular_shift(7, 5), "7")

    def test_multiple_shifts_typical(self):
        # Typical input: multiple shifts, shift < number of digits
        self.assertEqual(circular_shift(12345, 2), "45123")

    def test_shift_one_less_than_digits(self):
        # Boundary: shift = number of digits - 1
        self.assertEqual(circular_shift(123, 2), "231")

    def test_large_number_reversed(self):
        # Extreme input: large number, shift > number of digits (reversed)
        self.assertEqual(circular_shift(987654321, 10), "123456789")

    def test_zero_input(self):
        # Edge case: x is zero, shift == number of digits
        self.assertEqual(circular_shift(0, 1), "0")

    def test_all_same_digits(self):
        # Unusual input: number with all identical digits
        self.assertEqual(circular_shift(11111, 3), "11111")