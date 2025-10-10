import unittest
from sut_llm.problem_HumanEval_156 import int_to_mini_roman

class TestIntToMiniRoman(unittest.TestCase):

    def test_lower_boundary_one(self):
        # Test the absolute lower boundary of the input range (1)
        self.assertEqual(int_to_mini_roman(1), 'i')

    def test_upper_boundary_thousand(self):
        # Test the absolute upper boundary of the input range (1000)
        self.assertEqual(int_to_mini_roman(1000), 'm')

    def test_example_nineteen(self):
        # Test an example from the docstring, involving subtractive notation (IX)
        self.assertEqual(int_to_mini_roman(19), 'xix')

    def test_example_one_fifty_two(self):
        # Test an example from the docstring, involving hundreds, tens, and units
        self.assertEqual(int_to_mini_roman(152), 'clii')

    def test_example_four_twenty_six(self):
        # Test an example from the docstring, involving subtractive notation (CD) and other values
        self.assertEqual(int_to_mini_roman(426), 'cdxxvi')

    def test_subtractive_four(self):
        # Test a common subtractive case (IV) to catch off-by-one or logic errors around 4/5
        self.assertEqual(int_to_mini_roman(4), 'iv')

    def test_subtractive_nine_hundred(self):
        # Test a large subtractive case (CM) to ensure correct handling of hundreds
        self.assertEqual(int_to_mini_roman(900), 'cm')

    def test_just_below_upper_boundary_nine_ninety_nine(self):
        # Test a number just below the upper boundary, involving multiple subtractive forms (CM, XC, IX)
        self.assertEqual(int_to_mini_roman(999), 'cmxcix')

    def test_mid_range_additive_seventy_three(self):
        # Test a typical mid-range number using additive notation (LXXIII)
        self.assertEqual(int_to_mini_roman(73), 'lxxiii')

    def test_mid_range_complex_three_eighty_eight(self):
        # Test a complex mid-range number with many repeated characters and mixed values (CCCLXXXVIII)
        self.assertEqual(int_to_mini_roman(388), 'ccclxxxviii')

    def test_raises_value_error_for_zero(self):
        with self.assertRaises(ValueError) as cm:
            int_to_mini_roman(0)
        self.assertEqual(str(cm.exception), "Number must be between 1 and 1000 (inclusive).")

    def test_raises_value_error_for_negative_number(self):
        with self.assertRaises(ValueError) as cm:
            int_to_mini_roman(-5)
        self.assertEqual(str(cm.exception), "Number must be between 1 and 1000 (inclusive).")

    def test_raises_value_error_for_number_too_large(self):
        with self.assertRaises(ValueError) as cm:
            int_to_mini_roman(1001)
        self.assertEqual(str(cm.exception), "Number must be between 1 and 1000 (inclusive).")

