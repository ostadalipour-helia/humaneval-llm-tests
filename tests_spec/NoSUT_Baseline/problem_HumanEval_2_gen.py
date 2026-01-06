import unittest
import sut.problem_HumanEval_2 as mod

class TestHybrid(unittest.TestCase):
    def test_docstring_example(self):
            """Test with the example provided in the docstring."""
            self.assertEqual(mod.truncate_number(3.5), 0.5)

    def test_exact_integer(self):
            """Test a number that is an exact integer (boundary case)."""
            self.assertEqual(mod.truncate_number(5.0), 0.0)

    def test_small_positive_decimal(self):
            """Test a small positive number where the integer part is zero (edge case)."""
            self.assertEqual(mod.truncate_number(0.1), 0.1)

    def test_very_small_decimal_input(self):
            """Test a very small positive number with a decimal part (extreme/edge case)."""
            self.assertEqual(mod.truncate_number(0.0000000000000001), 0.0000000000000001)

    def test_another_typical_decimal(self):
            """Test another typical floating point number."""
            self.assertEqual(mod.truncate_number(7.25), 0.25)

    def test_normal_positive_decimal(self):
            # Normal case: positive number with a clear fractional part
            number = 3.5
            expected_output = 0.5
            result = mod.truncate_number(number)
            self.assertIsInstance(result, float)
            self.assertAlmostEqual(result, expected_output)
            self.assertTrue(0 <= result < 1)
            self.assertAlmostEqual(number - result, round(number - result)) # Check if difference is an integer

    def test_normal_another_decimal(self):
            # Normal case: another positive number with a fractional part
            number = 1.234
            expected_output = 0.234
            result = mod.truncate_number(number)
            self.assertIsInstance(result, float)
            self.assertAlmostEqual(result, expected_output)
            self.assertTrue(0 <= result < 1)
            self.assertAlmostEqual(number - result, round(number - result))

    def test_normal_integer_input(self):
            # Normal case: input is an exact integer (as a float)
            number = 10.0
            expected_output = 0.0
            result = mod.truncate_number(number)
            self.assertIsInstance(result, float)
            self.assertAlmostEqual(result, expected_output)
            self.assertTrue(0 <= result < 1)
            self.assertAlmostEqual(number - result, round(number - result))

    def test_normal_less_than_one(self):
            # Normal case: input is less than 1 but positive
            number = 0.999
            expected_output = 0.999
            result = mod.truncate_number(number)
            self.assertIsInstance(result, float)
            self.assertAlmostEqual(result, expected_output)
            self.assertTrue(0 <= result < 1)
            self.assertAlmostEqual(number - result, round(number - result))

    def test_edge_very_small_positive(self):
            # Edge case: very small positive number
            number = 1e-06
            expected_output = 1e-06
            result = mod.truncate_number(number)
            self.assertIsInstance(result, float)
            self.assertAlmostEqual(result, expected_output)
            self.assertTrue(0 <= result < 1)
            self.assertAlmostEqual(number - result, round(number - result))

    def test_edge_one_point_zero(self):
            # Edge case: input is exactly 1.0. Spec expects 1e-16 due to float precision.
            number = 1.0
            expected_output = 1e-16 # This implies a very small positive number, not exactly 0.0
            result = mod.truncate_number(number)
            self.assertIsInstance(result, float)
            self.assertAlmostEqual(result, expected_output, delta=1e-15) # Use delta for very small numbers
            self.assertTrue(0 <= result < 1)
            self.assertAlmostEqual(number - result, round(number - result))

    def test_edge_large_number_with_decimal(self):
            # Edge case: large number with a fractional part
            number = 123456789.12345679
            expected_output = 0.123456789
            result = mod.truncate_number(number)
            self.assertIsInstance(result, float)
            self.assertAlmostEqual(result, expected_output, places=7) # Adjust precision for large numbers
            self.assertTrue(0 <= result < 1)
            self.assertAlmostEqual(number - result, round(number - result))

    def test_error_non_float_string(self):
            # Error case: input is not a float (string)
            number = "not_a_float"
            with self.assertRaises(TypeError):
                mod.truncate_number(number)

    def test_error_non_float_null(self):
            # Error case: input is not a float (None)
            number = None
            with self.assertRaises(TypeError):
                mod.truncate_number(number)

