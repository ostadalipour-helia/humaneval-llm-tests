import unittest
from sut.problem_HumanEval_2 import truncate_number

class TestTruncateNumber(unittest.TestCase):

    def test_docstring_example(self):
        """Test with the example provided in the docstring."""
        self.assertEqual(truncate_number(3.5), 0.5)

    def test_exact_integer(self):
        """Test a number that is an exact integer (boundary case)."""
        self.assertEqual(truncate_number(5.0), 0.0)

    def test_just_above_integer(self):
        """Test a number infinitesimally greater than an integer (boundary/off-by-one)."""
        self.assertEqual(truncate_number(2.000000000000001), 0.000000000000001)

    def test_just_below_integer(self):
        """Test a number infinitesimally less than an integer (boundary/off-by-one)."""
        self.assertEqual(truncate_number(4.999999999999999), 0.999999999999999)

    def test_small_positive_decimal(self):
        """Test a small positive number where the integer part is zero (edge case)."""
        self.assertEqual(truncate_number(0.1), 0.1)

    def test_very_small_decimal_input(self):
        """Test a very small positive number with a decimal part (extreme/edge case)."""
        self.assertEqual(truncate_number(0.0000000000000001), 0.0000000000000001)

    def test_large_number_with_decimal(self):
        """Test a very large number with a decimal part (extreme input)."""
        self.assertEqual(truncate_number(123456789.12345), 0.12345)

    def test_another_typical_decimal(self):
        """Test another typical floating point number."""
        self.assertEqual(truncate_number(7.25), 0.25)

    def test_number_with_large_decimal_part(self):
        """Test a number with a decimal part close to 1."""
        self.assertEqual(truncate_number(1.9), 0.9)

    def test_repeating_decimal_approximation(self):
        """Test a number that is a common repeating decimal approximation."""
        self.assertEqual(truncate_number(10.333333333333333), 0.333333333333333)

if __name__ == '__main__':
    unittest.main()