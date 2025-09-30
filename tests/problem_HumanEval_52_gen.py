import unittest
from sut.problem_HumanEval_52 import below_threshold

class TestBelowThreshold(unittest.TestCase):

    def test_all_elements_below_threshold(self):
        self.assertTrue(below_threshold([1, 2, 3, 4], 5))

    def test_one_element_at_threshold(self):
        self.assertFalse(below_threshold([1, 2, 5, 4], 5))

    def test_one_element_above_threshold(self):
        self.assertFalse(below_threshold([1, 6, 3, 4], 5))

    def test_empty_list(self):
        self.assertTrue(below_threshold([], 10))

    def test_list_with_negative_numbers_all_below(self):
        self.assertTrue(below_threshold([-1, -5, 0], 1))

    def test_list_with_negative_numbers_one_at_threshold(self):
        self.assertFalse(below_threshold([-10, -5, -4], -4))

    def test_list_with_negative_numbers_one_above_threshold(self):
        self.assertFalse(below_threshold([-10, -3, -7], -4))

    def test_single_element_below_threshold(self):
        self.assertTrue(below_threshold([0], 1))

    def test_single_element_at_threshold(self):
        self.assertFalse(below_threshold([0], 0))

    def test_large_list_all_below(self):
        self.assertTrue(below_threshold(list(range(100)), 100))