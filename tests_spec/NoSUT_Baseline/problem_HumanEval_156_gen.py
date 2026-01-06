import unittest
import sut.problem_HumanEval_156 as mod

class TestHybrid(unittest.TestCase):
    def test_lower_boundary_one(self):
            # Test the absolute lower boundary of the input range (1)
            self.assertEqual(mod.int_to_mini_roman(1), 'i')

    def test_upper_boundary_thousand(self):
            # Test the absolute upper boundary of the input range (1000)
            self.assertEqual(mod.int_to_mini_roman(1000), 'm')

    def test_example_nineteen(self):
            # Test an example from the docstring, involving subtractive notation (IX)
            self.assertEqual(mod.int_to_mini_roman(19), 'xix')

    def test_example_one_fifty_two(self):
            # Test an example from the docstring, involving hundreds, tens, and units
            self.assertEqual(mod.int_to_mini_roman(152), 'clii')

    def test_example_four_twenty_six(self):
            # Test an example from the docstring, involving subtractive notation (CD) and other values
            self.assertEqual(mod.int_to_mini_roman(426), 'cdxxvi')

    def test_subtractive_four(self):
            # Test a common subtractive case (IV) to catch off-by-one or logic errors around 4/5
            self.assertEqual(mod.int_to_mini_roman(4), 'iv')

    def test_subtractive_nine_hundred(self):
            # Test a large subtractive case (CM) to ensure correct handling of hundreds
            self.assertEqual(mod.int_to_mini_roman(900), 'cm')

    def test_just_below_upper_boundary_nine_ninety_nine(self):
            # Test a number just below the upper boundary, involving multiple subtractive forms (CM, XC, IX)
            self.assertEqual(mod.int_to_mini_roman(999), 'cmxcix')

    def test_mid_range_additive_seventy_three(self):
            # Test a typical mid-range number using additive notation (LXXIII)
            self.assertEqual(mod.int_to_mini_roman(73), 'lxxiii')

    def test_mid_range_complex_three_eighty_eight(self):
            # Test a complex mid-range number with many repeated characters and mixed values (CCCLXXXVIII)
            self.assertEqual(mod.int_to_mini_roman(388), 'ccclxxxviii')

    def test_normal_nineteen(self):
            # A typical number requiring subtractive notation and multiple symbols.
            self.assertEqual(mod.int_to_mini_roman(19), "xix")

    def test_normal_one_fifty_two(self):
            # A number with hundreds, tens, and units.
            self.assertEqual(mod.int_to_mini_roman(152), "clii")

    def test_normal_four_twenty_six(self):
            # A number requiring subtractive notation for hundreds and standard notation for tens and units.
            self.assertEqual(mod.int_to_mini_roman(426), "cdxxvi")

    def test_edge_min_value(self):
            # The minimum allowed input value.
            self.assertEqual(mod.int_to_mini_roman(1), "i")

    def test_edge_max_value(self):
            # The maximum allowed input value.
            self.assertEqual(mod.int_to_mini_roman(1000), "m")

    def test_edge_subtractive_four(self):
            # A number demonstrating subtractive notation for units.
            self.assertEqual(mod.int_to_mini_roman(4), "iv")

    def test_edge_subtractive_ninety_nine(self):
            # A number demonstrating subtractive notation for tens and units.
            self.assertEqual(mod.int_to_mini_roman(99), "xcix")

    def test_error_string_input(self):
            # Input is a string instead of an integer.
            with self.assertRaises(TypeError):
                mod.int_to_mini_roman("19")

