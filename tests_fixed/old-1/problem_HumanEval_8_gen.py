import unittest
from sut_llm.problem_HumanEval_8 import sum_product

class TestSumProduct(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sum_product([]), (0, 1))

    def test_positive_integers(self):
        self.assertEqual(sum_product([1, 2, 3, 4]), (10, 24))

    def test_single_positive_integer(self):
        self.assertEqual(sum_product([5]), (5, 5))

    def test_single_negative_integer(self):
        self.assertEqual(sum_product([-5]), (-5, -5))

    def test_mixed_positive_and_negative_integers(self):
        self.assertEqual(sum_product([1, -2, 3]), (2, -6))

    def test_list_with_zero(self):
        self.assertEqual(sum_product([0]), (0, 0))

    def test_list_with_zero_and_other_numbers(self):
        self.assertEqual(sum_product([1, 0, 3]), (4, 0))

    def test_all_negative_integers(self):
        self.assertEqual(sum_product([-1, -2, -3]), (-6, -6))

    def test_larger_positive_numbers(self):
        self.assertEqual(sum_product([10, 20]), (30, 200))

    def test_duplicate_numbers(self):
        self.assertEqual(sum_product([2, 2, 2]), (6, 8))

if __name__ == '__main__':
    unittest.main()