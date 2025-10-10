import unittest
from sut.problem_HumanEval_8 import sum_product

class TestSumProduct(unittest.TestCase):

    def test_empty_list(self):
        """Test with an empty list, expecting (0, 1)."""
        self.assertEqual(sum_product([]), (0, 1))

    def test_single_positive_element(self):
        """Test with a single positive integer."""
        self.assertEqual(sum_product([5]), (5, 5))

    def test_multiple_positive_integers(self):
        """Test with multiple positive integers."""
        self.assertEqual(sum_product([1, 2, 3, 4]), (10, 24))

    def test_single_negative_element(self):
        """Test with a single negative integer."""
        self.assertEqual(sum_product([-