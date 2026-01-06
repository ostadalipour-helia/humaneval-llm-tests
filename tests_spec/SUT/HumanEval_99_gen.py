import unittest
from sut.problem_HumanEval_99 import closest_integer

class Test_closest_integer(unittest.TestCase):

    def test_integer_string(self):
        self.assertEqual(closest_integer("10"), 10)

    def test_positive_rounding(self):
        self.assertEqual(closest_integer("15.3"), 15)
        self.assertEqual(closest_integer("15.7"), 16)

    def test_negative_rounding(self):
        self.assertEqual(closest_integer("-15.3"), -15)
        self.assertEqual(closest_integer("-15.7"), -16)

    def test_positive_equidistant(self):
        self.assertEqual(closest_integer("14.5"), 15)

    def test_negative_equidistant(self):
        self.assertEqual(closest_integer("-14.5"), -15)

    def test_zero_and_near_zero(self):
        self.assertEqual(closest_integer("0"), 0)
        self.assertEqual(closest_integer("0.0"), 0)
        self.assertEqual(closest_integer("0.1"), 0)
        self.assertEqual(closest_integer("-0.1"), 0)

    def test_equidistant_around_zero(self):
        self.assertEqual(closest_integer("0.5"), 1)
        self.assertEqual(closest_integer("-0.5"), -1)

    def test_large_numbers(self):
        self.assertEqual(closest_integer("1234567890.123"), 1234567890)
        self.assertEqual(closest_integer("-987654321.876"), -987654322)

    def test_precision_just_above_integer(self):
        self.assertEqual(closest_integer("3.000000000000001"), 3)

    def test_precision_just_below_integer(self):
        self.assertEqual(closest_integer("2.999999999999999"), 3)