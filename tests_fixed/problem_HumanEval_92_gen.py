import unittest
from sut_llm.problem_HumanEval_92 import any_int

class TestAnyInt(unittest.TestCase):

    def test_positive_sum_x_y_eq_z(self):
        # Example case: 5 + 2 = 7
        self.assertTrue(any_int(5, 2, 7))

    def test_positive_sum_y_z_eq_x(self):
        # Permutation: 2 + 7 = 9, but 7 + 2 = 9, so 9, 2, 7
        self.assertTrue(any_int(9, 2, 7))

    def test_positive_sum_x_z_eq_y(self):
        # Permutation: 5 + 7 = 12, so 5, 12, 7
        self.assertTrue(any_int(5, 12, 7))

    def test_negative_and_positive_sum(self):
        # Example case: 3 + (-2) = 1
        self.assertTrue(any_int(3, -2, 1))

    def test_sum_with_zero(self):
        # One number is zero, sum of others equals a third
        self.assertTrue(any_int(0, 5, 5))

    def test_no_sum_match_all_integers(self):
        # Example case: 3, 2, 2 -> no sum matches
        self.assertFalse(any_int(3, 2, 2))

    def test_no_sum_match_all_integers_different_values(self):
        # All integers, but no sum matches
        self.assertFalse(any_int(1, 2, 4))

    def test_float_present_sum_would_match(self):
        # Example case: 3.6, -2.2, 2 -> float present, sum would be 1.4 != 2
        # The docstring example implies that if any number is not an integer, it's false.
        self.assertFalse(any_int(3.6, -2.2, 2))

    def test_one_float_sum_would_match(self):
        # One float, even if it's a whole number like 2.0, it's not an int
        self.assertFalse(any_int(5, 2.0, 7))

    def test_another_float_sum_would_match(self):
        # Another float case, sum would match if all were integers
        self.assertFalse(any_int(1, 2, 3.0))

if __name__ == '__main__':
    unittest.main()