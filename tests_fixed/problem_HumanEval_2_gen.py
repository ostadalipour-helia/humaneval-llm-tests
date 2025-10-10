import unittest
from sut_llm.problem_HumanEval_2 import truncate_number

class TestTruncateNumber(unittest.TestCase):

    def test_docstring_example(self):
        """Test with the example provided in the docstring."""
        self.assertEqual(truncate_number(3.5), 0.5)

    def test_exact_integer(self):
        """Test a number that is an exact integer (boundary case)."""
        self.assertEqual(truncate_number(5.0), 0.0)

    def test_just_above_integer(self):
        """Test a number infinitesimally greater than an integer (boundary/off-by-one)."""
        # Due to floating-point precision, direct equality comparison can fail for very small differences.
        # Use assertAlmostEqual for comparing floating-point numbers.
        # The expected value 0.000000000000001 has 15 decimal places, so we compare up to that precision.
        self.assertAlmostEqual(truncate_number(2.000000000000001), 0.000000000000001, places=15)

    def test_just_below_integer(self):
        """Test a number infinitesimally less than an integer (boundary/off-by-one)."""
        self.assertAlmostEqual(truncate_number(4.999999999999999), 0.999999999999999, places=15)

    def test_small_positive_decimal(self):
        """Test a small positive number where the integer part is zero (edge case)."""
        self.assertEqual(truncate_number(0.1), 0.1)

    def test_very_small_decimal_input(self):
        """Test a very small positive number with a decimal part (extreme/edge case)."""
        self.assertEqual(truncate_number(0.0000000000000001), 0.0000000000000001)

    def test_large_number_with_decimal(self):
        """Test a very large number with a decimal part (extreme input)."""
        self.assertAlmostEqual(truncate_number(123456789.12345), 0.12345, places=5)

    def test_another_typical_decimal(self):
        """Test another typical floating point number."""
        self.assertEqual(truncate_number(7.25), 0.25)

    def test_number_with_large_decimal_part(self):
        """Test a number with a decimal part close to 1."""
        self.assertAlmostEqual(truncate_number(1.9), 0.9)

    def test_repeating_decimal_approximation(self):
        """Test a number that is a common repeating decimal approximation."""
        self.assertAlmostEqual(truncate_number(10.333333333333333), 0.333333333333333, places=12)

if __name__ == '__main__':
    unittest.main()