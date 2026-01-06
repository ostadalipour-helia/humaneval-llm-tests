import unittest
from sut.problem_HumanEval_2 import truncate_number

class Test_truncate_number(unittest.TestCase):
    def test_normal_positive_decimal(self):
        # Normal case: positive number with a clear fractional part
        number = 3.5
        expected_output = 0.5
        result = truncate_number(number)
        self.assertIsInstance(result, float)
        self.assertAlmostEqual(result, expected_output)
        self.assertTrue(0 <= result < 1)
        self.assertAlmostEqual(number - result, round(number - result)) # Check if difference is an integer

    def test_normal_another_decimal(self):
        # Normal case: another positive number with a fractional part
        number = 1.234
        expected_output = 0.234
        result = truncate_number(number)
        self.assertIsInstance(result, float)
        self.assertAlmostEqual(result, expected_output)
        self.assertTrue(0 <= result < 1)
        self.assertAlmostEqual(number - result, round(number - result))

    def test_normal_integer_input(self):
        # Normal case: input is an exact integer (as a float)
        number = 10.0
        expected_output = 0.0
        result = truncate_number(number)
        self.assertIsInstance(result, float)
        self.assertAlmostEqual(result, expected_output)
        self.assertTrue(0 <= result < 1)
        self.assertAlmostEqual(number - result, round(number - result))

    def test_normal_less_than_one(self):
        # Normal case: input is less than 1 but positive
        number = 0.999
        expected_output = 0.999
        result = truncate_number(number)
        self.assertIsInstance(result, float)
        self.assertAlmostEqual(result, expected_output)
        self.assertTrue(0 <= result < 1)
        self.assertAlmostEqual(number - result, round(number - result))

    def test_edge_very_small_positive(self):
        # Edge case: very small positive number
        number = 1e-06
        expected_output = 1e-06
        result = truncate_number(number)
        self.assertIsInstance(result, float)
        self.assertAlmostEqual(result, expected_output)
        self.assertTrue(0 <= result < 1)
        self.assertAlmostEqual(number - result, round(number - result))

    def test_edge_one_point_zero(self):
        # Edge case: input is exactly 1.0. Spec expects 1e-16 due to float precision.
        number = 1.0
        expected_output = 1e-16 # This implies a very small positive number, not exactly 0.0
        result = truncate_number(number)
        self.assertIsInstance(result, float)
        self.assertAlmostEqual(result, expected_output, delta=1e-15) # Use delta for very small numbers
        self.assertTrue(0 <= result < 1)
        self.assertAlmostEqual(number - result, round(number - result))

    def test_edge_large_number_with_decimal(self):
        # Edge case: large number with a fractional part
        number = 123456789.12345679
        expected_output = 0.123456789
        result = truncate_number(number)
        self.assertIsInstance(result, float)
        self.assertAlmostEqual(result, expected_output, places=7) # Adjust precision for large numbers
        self.assertTrue(0 <= result < 1)
        self.assertAlmostEqual(number - result, round(number - result))

    def test_error_negative_number(self):
        # Error case: input number is negative
        number = -3.5
        with self.assertRaises(ValueError):
            truncate_number(number)

    def test_error_zero_input(self):
        # Error case: input number is zero
        number = 0.0
        with self.assertRaises(ValueError):
            truncate_number(number)

    def test_error_non_float_string(self):
        # Error case: input is not a float (string)
        number = "not_a_float"
        with self.assertRaises(TypeError):
            truncate_number(number)

    def test_error_non_float_null(self):
        # Error case: input is not a float (None)
        number = None
        with self.assertRaises(TypeError):
            truncate_number(number)