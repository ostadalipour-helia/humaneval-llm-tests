import unittest
import sut.problem_HumanEval_99 as mod

class TestHybrid(unittest.TestCase):
    def test_typical_positive_decimal_rounds_down(self):
            # Test a typical positive decimal that rounds down
            self.assertEqual(mod.closest_integer("15.3"), 15)

    def test_typical_positive_decimal_rounds_up(self):
            # Test a typical positive decimal that rounds up
            self.assertEqual(mod.closest_integer("15.7"), 16)

    def test_positive_equidistant_away_from_zero(self):
            # Boundary test: positive number equidistant from two integers, rounds away from zero
            # This specifically targets the "away from zero" rule for X.5
            self.assertEqual(mod.closest_integer("14.5"), 15)

    def test_negative_equidistant_away_from_zero(self):
            # Boundary test: negative number equidistant from two integers, rounds away from zero
            # This specifically targets the "away from zero" rule for -X.5
            self.assertEqual(mod.closest_integer("-14.5"), -15)

    def test_positive_integer_string(self):
            # Edge case: input is already a positive integer string
            self.assertEqual(mod.closest_integer("10"), 10)

    def test_negative_integer_string(self):
            # Edge case: input is already a negative integer string
            self.assertEqual(mod.closest_integer("-7"), -7)

    def test_zero_decimal_input(self):
            # Edge case: zero represented as a decimal string
            self.assertEqual(mod.closest_integer("0.0"), 0)

    def test_zero_integer_input(self):
            # Edge case: zero represented as an integer string
            self.assertEqual(mod.closest_integer("0"), 0)

    def test_very_close_to_integer_rounds_up(self):
            # Extreme input: a number very slightly less than an integer, should round up
            # Catches off-by-one errors around integer boundaries (e.g., 9.999999 -> 10)
            self.assertEqual(mod.closest_integer("9.999999"), 10)

    def test_large_negative_decimal_rounds_towards_zero(self):
            # Extreme input: a large negative decimal that rounds towards zero
            self.assertEqual(mod.closest_integer("-12345.3"), -12345)

    def test_positive_integer_no_rounding(self):
            # Normal case: Integer string, no rounding needed.
            self.assertEqual(mod.closest_integer("10"), 10)

    def test_positive_float_round_up(self):
            # Normal case: Positive float, rounds up to the closest integer.
            self.assertEqual(mod.closest_integer("15.7"), 16)

    def test_negative_float_equidistant_away_from_zero(self):
            # Normal case: Negative float, equidistant, rounds away from zero.
            self.assertEqual(mod.closest_integer("-14.5"), -15)

    def test_zero_float(self):
            # Edge case: Input is zero as a float string.
            self.assertEqual(mod.closest_integer("0.0"), 0)

    def test_equidistant_positive_to_one(self):
            # Edge case: Equidistant positive, rounds away from zero.
            self.assertEqual(mod.closest_integer("0.5"), 1)

    def test_large_negative_number(self):
            # Edge case: Large negative number, rounds down (away from zero).
            self.assertEqual(mod.closest_integer("-987654321.876"), -987654322)

    def test_error_empty_string(self):
            # Error case: Input string is empty, cannot be converted to a number.
            with self.assertRaises(ValueError):
                mod.closest_integer("")

    def test_error_invalid_string(self):
            # Error case: Input string is not a valid numerical representation.
            with self.assertRaises(ValueError):
                mod.closest_integer("abc")

