import unittest
import sut.problem_HumanEval_8 as mod

class TestHybrid(unittest.TestCase):
    def test_empty_list(self):
            """
            Test case for an empty list.
            Verifies the specified behavior for empty sum (0) and empty product (1).
            This is a critical boundary and edge case.
            """
            self.assertEqual(mod.sum_product([]), (0, 1))

    def test_single_positive_element(self):
            """
            Test case for a list with a single positive integer.
            Covers an edge case and a boundary condition (list length 1).
            """
            self.assertEqual(mod.sum_product([5]), (5, 5))

    def test_single_zero_element(self):
            """
            Test case for a list with a single zero.
            Covers an edge case, boundary condition, and sign/zero testing.
            Ensures product correctly becomes zero.
            """
            self.assertEqual(mod.sum_product([0]), (0, 0))

    def test_single_negative_element(self):
            """
            Test case for a list with a single negative integer.
            Covers an edge case, boundary condition, and sign testing.
            """
            self.assertEqual(mod.sum_product([-3]), (-3, -3))

    def test_typical_positive_list(self):
            """
            Test case for a typical list of positive integers.
            Matches one of the examples from the docstring.
            """
            self.assertEqual(mod.sum_product([1, 2, 3, 4]), (10, 24))

    def test_list_with_zeros(self):
            """
            Test case for a list containing zero.
            Ensures the product correctly becomes zero when a zero is present.
            Covers an extreme/unusual input.
            """
            self.assertEqual(mod.sum_product([1, 0, 3, 5]), (9, 0))

    def test_list_with_negative_numbers(self):
            """
            Test case for a list containing only negative numbers.
            Checks correct sum and product behavior with multiple negatives.
            Covers an extreme/unusual input and sign testing.
            """
            self.assertEqual(mod.sum_product([-1, -2, -3]), (-6, -6))

    def test_list_with_mixed_signs(self):
            """
            Test case for a list with a mix of positive and negative numbers.
            Checks sum and product logic under mixed sign conditions.
            Covers an extreme/unusual input and sign testing.
            """
            self.assertEqual(mod.sum_product([-1, 2, -3, 4]), (2, 24))

    def test_list_with_duplicates_and_same_values(self):
            """
            Test case for a list with duplicate values, all being the same.
            Covers an edge case for collection content.
            """
            self.assertEqual(mod.sum_product([2, 2, 2, 2]), (8, 16))

    def test_larger_list_mixed_values_and_zero(self):
            """
            Test case for a larger list with a mix of positive, negative, and zero values.
            Covers a more complex, extreme/unusual input scenario.
            """
            self.assertEqual(mod.sum_product([10, -5, 2, 0, 1, -2]), (6, 0))
    
    if __name__ == '__main__':
        unittest.main()

    def test_normal_positive_integers(self):
            # A typical list of positive integers.
            numbers = [1, 2, 3, 4]
            expected_output = (10, 24)
            self.assertEqual(mod.sum_product(numbers), expected_output)

    def test_normal_mixed_integers(self):
            # A list containing positive, negative, and zero integers.
            numbers = [5, -2, 0]
            expected_output = (3, 0)
            self.assertEqual(mod.sum_product(numbers), expected_output)

    def test_normal_larger_integers(self):
            # A list of larger positive integers.
            numbers = [10, 20, 30]
            expected_output = (60, 6000)
            self.assertEqual(mod.sum_product(numbers), expected_output)

    def test_edge_empty_list(self):
            # An empty list, as specified for empty sum and product.
            numbers = []
            expected_output = (0, 1)
            self.assertEqual(mod.sum_product(numbers), expected_output)

    def test_edge_single_element_list(self):
            # A list with a single integer.
            numbers = [7]
            expected_output = (7, 7)
            self.assertEqual(mod.sum_product(numbers), expected_output)

    def test_edge_negative_integers(self):
            # A list containing only negative integers.
            numbers = [-1, -2, -3]
            expected_output = (-6, -6)
            self.assertEqual(mod.sum_product(numbers), expected_output)

    def test_edge_only_zeros(self):
            # A list containing only zeros.
            numbers = [0, 0, 0]
            expected_output = (0, 0)
            self.assertEqual(mod.sum_product(numbers), expected_output)

    def test_error_input_none(self):
            # Input is not a list.
            numbers = None
            with self.assertRaises(TypeError):
                mod.sum_product(numbers)

    def test_error_list_with_string(self):
            # Input list contains non-integer elements (string).
            numbers = [1, 'a', 3]
            with self.assertRaises(TypeError):
                mod.sum_product(numbers)

