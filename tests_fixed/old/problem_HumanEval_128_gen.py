import unittest
from sut_llm.problem_HumanEval_128 import prod_signs

class TestProdSigns(unittest.TestCase):

    def test_empty_array(self):
        self.assertIsNone(prod_signs([]))

    def test_all_positive_numbers(self):
        # sum_mag = 1+2+3 = 6, prod_signs = 1*1*1 = 1. Result = 6 * 1 = 6
        self.assertEqual(prod_signs([1, 2, 3]), 6)

    def test_one_negative_number(self):
        # sum_mag = 1+2+3 = 6, prod_signs = 1*1*(-1) = -1. Result = 6 * (-1) = -6
        self.assertEqual(prod_signs([1, 2, -3]), -6)

    def test_even_number_of_negatives(self):
        # sum_mag = 1+2+3 = 6, prod_signs = 1*(-1)*(-1) = 1. Result = 6 * 1 = 6
        self.assertEqual(prod_signs([1, -2, -3]), 6)

    def test_odd_number_of_negatives(self):
        # sum_mag = 1+2+3+4 = 10, prod_signs = 1*(-1)*(-1)*(-1) = -1. Result = 10 * (-1) = -10
        self.assertEqual(prod_signs([1, -2, -3, -4]), -10)

    def test_array_with_zero(self):
        # sum_mag = 0+1+2 = 3, prod_signs = 0*1*1 = 0. Result = 3 * 0 = 0
        self.assertEqual(prod_signs([0, 1, 2]), 0)

    def test_array_with_zero_and_negatives(self):
        # sum_mag = 0+1+2 = 3, prod_signs = 0*(-1)*1 = 0. Result = 3 * 0 = 0
        self.assertEqual(prod_signs([0, -1, 2]), 0)

    def test_single_positive_element(self):
        # sum_mag = 5, prod_signs = 1. Result = 5 * 1 = 5
        self.assertEqual(prod_signs([5]), 5)

    def test_single_negative_element(self):
        # sum_mag = 5, prod_signs = -1. Result = 5 * (-1) = -5
        self.assertEqual(prod_signs([-5]), -5)

    def test_docstring_example_one(self):
        # sum_mag = 1+2+2+4 = 9, prod_signs = 1*1*1*(-1) = -1. Result = 9 * (-1) = -9
        self.assertEqual(prod_signs([1, 2, 2, -4]), -9)

if __name__ == '__main__':
    unittest.main()