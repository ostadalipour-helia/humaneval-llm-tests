import unittest
from sut.problem_HumanEval_99 import closest_integer

class TestClosestInteger(unittest.TestCase):

    def test_exact_positive_integer(self):
        self.assertEqual(closest_integer("10"), 10)

    def test_positive_float_rounds_down(self):
        self.assertEqual(closest_integer("15.3"), 15)

    def test_positive_float_equidistant_rounds_away_from_zero(self):
        self.assertEqual(closest_integer("14.5"), 15)

    def test_negative_float_equidistant_rounds_away_from_zero(self):
        self.assertEqual(closest_integer("-14.5"), -15)

    def test_negative_float_rounds_up_towards_zero(self):
        self.assertEqual(closest_integer("-15.3"), -15)

    def test_zero_input(self):
        self.assertEqual(closest_integer("0"), 0)

    def test_small_positive_float_rounds_down_to_zero(self):
        self.assertEqual(closest_integer("0.1"), 0)

    def test_small_negative_float_rounds_up_to_zero(self):
        self.assertEqual(closest_integer("-0.1"), 0)

    def test_large_positive_float_rounds_up(self):
        self.assertEqual(closest_integer("99.9"), 100)

    def test_large_negative_float_rounds_up_towards_zero(self):
        self.assertEqual(closest_integer("-99.1"), -99)

if __name__ == '__main__':
    unittest.main()