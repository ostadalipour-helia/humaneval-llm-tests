import unittest
from sut.problem_HumanEval_3 import below_zero

class TestBelowZero(unittest.TestCase):

    def test_all_positive_operations(self):
        self.assertFalse(below_zero([1, 2, 3]))

    def test_positive_then_negative_stays_non_negative(self):
        self.assertFalse(below_zero([10, -5, 3]))

    def test_positive_then_negative_goes_below_zero_middle(self):
        self.assertTrue(below_zero([1, 2, -4, 5]))

    def test_starts_with_negative_operation(self):
        self.assertTrue(below_zero([-10]))

    def test_multiple_operations_goes_below_zero_later(self):
        self.assertTrue(below_zero([5, -3, -4, 2]))

    def test_empty_operations_list(self):
        self.assertFalse(below_zero([]))

    def test_balance_reaches_zero_then_goes_negative(self):
        self.assertTrue(below_zero([5, -5, -1]))

    def test_balance_reaches_zero_then_positive(self):
        self.assertFalse(below_zero([5, -5, 1]))

    def test_long_fluctuating_but_never_below_zero(self):
        self.assertFalse(below_zero([10, -5, 3, -2, 4, -1, 0, 7]))

    def test_single_positive_operation(self):
        self.assertFalse(below_zero([100]))