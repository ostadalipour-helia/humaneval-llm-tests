import unittest
from sut.problem_HumanEval_8 import sum_product

class TestSumProduct(unittest.TestCase):

    def test_empty_list(self):
        """
        Test case for an empty list.
        Verifies the specified behavior for empty sum (0) and empty product (1).
        This is a critical boundary and edge case.
        """
        self.assertEqual(sum_product([]), (0, 1))

    def test_single_positive_element(self):
        """
        Test case for a list with a single positive integer.
        Covers an edge case and a boundary condition (list length 1).
        """
        self.assertEqual(sum_product([5]), (5, 5))

    def test_single_zero_element(self):
        """
        Test case for a list with a single zero.
        Covers an edge case, boundary condition, and sign/zero testing.
        Ensures product correctly becomes zero.
        """
        self.assertEqual(sum_product([0]), (0, 0))

    def test_single_negative_element(self):
        """
        Test case for a list with a single negative integer.
        Covers an edge case, boundary condition, and sign testing.
        """
        self.assertEqual(sum_product([-3]), (-3, -3))

    def test_typical_positive_list(self):
        """
        Test case for a typical list of positive integers.
        Matches one of the examples from the docstring.
        """
        self.assertEqual(sum_product([1, 2, 3, 4]), (10, 24))

    def test_list_with_zeros(self):
        """
        Test case for a list containing zero.
        Ensures the product correctly becomes zero when a zero is present.
        Covers an extreme/unusual input.
        """
        self.assertEqual(sum_product([1, 0, 3, 5]), (9, 0))

    def test_list_with_negative_numbers(self):
        """
        Test case for a list containing only negative numbers.
        Checks correct sum and product behavior with multiple negatives.
        Covers an extreme/unusual input and sign testing.
        """
        self.assertEqual(sum_product([-1, -2, -3]), (-6, -6))

    def test_list_with_mixed_signs(self):
        """
        Test case for a list with a mix of positive and negative numbers.
        Checks sum and product logic under mixed sign conditions.
        Covers an extreme/unusual input and sign testing.
        """
        self.assertEqual(sum_product([-1, 2, -3, 4]), (2, 24))

    def test_list_with_duplicates_and_same_values(self):
        """
        Test case for a list with duplicate values, all being the same.
        Covers an edge case for collection content.
        """
        self.assertEqual(sum_product([2, 2, 2, 2]), (8, 16))

    def test_larger_list_mixed_values_and_zero(self):
        """
        Test case for a larger list with a mix of positive, negative, and zero values.
        Covers a more complex, extreme/unusual input scenario.
        """
        self.assertEqual(sum_product([10, -5, 2, 0, 1, -2]), (6, 0))

if __name__ == '__main__':
    unittest.main()