import unittest
from sut.problem_HumanEval_99 import closest_integer

class Test_closest_integer(unittest.TestCase):
    def test_positive_integer_no_rounding(self):
        # Normal case: Integer string, no rounding needed.
        self.assertEqual(closest_integer("10"), 10)

    def test_positive_float_round_up(self):
        # Normal case: Positive float, rounds up to the closest integer.
        self.assertEqual(closest_integer("15.7"), 16)

    def test_negative_float_equidistant_away_from_zero(self):
        # Normal case: Negative float, equidistant, rounds away from zero.
        self.assertEqual(closest_integer("-14.5"), -15)

    def test_zero_float(self):
        # Edge case: Input is zero as a float string.
        self.assertEqual(closest_integer("0.0"), 0)

    def test_equidistant_positive_to_one(self):
        # Edge case: Equidistant positive, rounds away from zero.
        self.assertEqual(closest_integer("0.5"), 1)

    def test_large_negative_number(self):
        # Edge case: Large negative number, rounds down (away from zero).
        self.assertEqual(closest_integer("-987654321.876"), -987654322)

    def test_error_non_string_int(self):
        # Error case: Input is an integer, not a string.
        with self.assertRaises(TypeError):
            closest_integer(123)

    def test_error_empty_string(self):
        # Error case: Input string is empty, cannot be converted to a number.
        with self.assertRaises(ValueError):
            closest_integer("")

    def test_error_invalid_string(self):
        # Error case: Input string is not a valid numerical representation.
        with self.assertRaises(ValueError):
            closest_integer("abc")

    def test_error_infinity_string(self):
        # Error case: Input string represents infinity.
        with self.assertRaises(ValueError):
            closest_integer("inf")