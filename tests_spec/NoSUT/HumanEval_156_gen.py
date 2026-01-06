import unittest
from sut.problem_HumanEval_156 import int_to_mini_roman

class Test_int_to_mini_roman(unittest.TestCase):
    def test_normal_nineteen(self):
        # A typical number requiring subtractive notation and multiple symbols.
        self.assertEqual(int_to_mini_roman(19), "xix")

    def test_normal_one_fifty_two(self):
        # A number with hundreds, tens, and units.
        self.assertEqual(int_to_mini_roman(152), "clii")

    def test_normal_four_twenty_six(self):
        # A number requiring subtractive notation for hundreds and standard notation for tens and units.
        self.assertEqual(int_to_mini_roman(426), "cdxxvi")

    def test_edge_min_value(self):
        # The minimum allowed input value.
        self.assertEqual(int_to_mini_roman(1), "i")

    def test_edge_max_value(self):
        # The maximum allowed input value.
        self.assertEqual(int_to_mini_roman(1000), "m")

    def test_edge_subtractive_four(self):
        # A number demonstrating subtractive notation for units.
        self.assertEqual(int_to_mini_roman(4), "iv")

    def test_edge_subtractive_ninety_nine(self):
        # A number demonstrating subtractive notation for tens and units.
        self.assertEqual(int_to_mini_roman(99), "xcix")

    def test_error_zero_input(self):
        # Input number is less than 1.
        with self.assertRaises(ValueError):
            int_to_mini_roman(0)

    def test_error_negative_input(self):
        # Input number is negative.
        with self.assertRaises(ValueError):
            int_to_mini_roman(-5)

    def test_error_too_large_input(self):
        # Input number is greater than 1000.
        with self.assertRaises(ValueError):
            int_to_mini_roman(1001)

    def test_error_float_input(self):
        # Input is a float instead of an integer.
        with self.assertRaises(TypeError):
            int_to_mini_roman(19.5)

    def test_error_string_input(self):
        # Input is a string instead of an integer.
        with self.assertRaises(TypeError):
            int_to_mini_roman("19")