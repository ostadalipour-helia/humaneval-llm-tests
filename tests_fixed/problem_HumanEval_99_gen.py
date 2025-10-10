import unittest
from sut_llm.problem_HumanEval_99 import closest_integer

class TestClosestInteger(unittest.TestCase):

    def test_typical_positive_decimal_rounds_down(self):
        # Test a typical positive decimal that rounds down
        self.assertEqual(closest_integer("15.3"), 15)

    def test_typical_positive_decimal_rounds_up(self):
        # Test a typical positive decimal that rounds up
        self.assertEqual(closest_integer("15.7"), 16)

    def test_positive_equidistant_away_from_zero(self):
        # Boundary test: positive number equidistant from two integers, rounds away from zero
        # This specifically targets the "away from zero" rule for X.5
        self.assertEqual(closest_integer("14.5"), 15)

    def test_negative_equidistant_away_from_zero(self):
        # Boundary test: negative number equidistant from two integers, rounds away from zero
        # This specifically targets the "away from zero" rule for -X.5
        self.assertEqual(closest_integer("-14.5"), -15)

    def test_positive_integer_string(self):
        # Edge case: input is already a positive integer string
        self.assertEqual(closest_integer("10"), 10)

    def test_negative_integer_string(self):
        # Edge case: input is already a negative integer string
        self.assertEqual(closest_integer("-7"), -7)

    def test_zero_decimal_input(self):
        # Edge case: zero represented as a decimal string
        self.assertEqual(closest_integer("0.0"), 0)

    def test_zero_integer_input(self):
        # Edge case: zero represented as an integer string
        self.assertEqual(closest_integer("0"), 0)

    def test_very_close_to_integer_rounds_up(self):
        # Extreme input: a number very slightly less than an integer, should round up
        # Catches off-by-one errors around integer boundaries (e.g., 9.999999 -> 10)
        self.assertEqual(closest_integer("9.999999"), 10)

    def test_large_negative_decimal_rounds_towards_zero(self):
        # Extreme input: a large negative decimal that rounds towards zero
        self.assertEqual(closest_integer("-12345.3"), -12345)