import unittest
from sut.problem_HumanEval_8 import sum_product

class Test_sum_product(unittest.TestCase):
    def test_normal_positive_integers(self):
        # A typical list of positive integers.
        numbers = [1, 2, 3, 4]
        expected_output = (10, 24)
        self.assertEqual(sum_product(numbers), expected_output)

    def test_normal_mixed_integers(self):
        # A list containing positive, negative, and zero integers.
        numbers = [5, -2, 0]
        expected_output = (3, 0)
        self.assertEqual(sum_product(numbers), expected_output)

    def test_normal_larger_integers(self):
        # A list of larger positive integers.
        numbers = [10, 20, 30]
        expected_output = (60, 6000)
        self.assertEqual(sum_product(numbers), expected_output)

    def test_edge_empty_list(self):
        # An empty list, as specified for empty sum and product.
        numbers = []
        expected_output = (0, 1)
        self.assertEqual(sum_product(numbers), expected_output)

    def test_edge_single_element_list(self):
        # A list with a single integer.
        numbers = [7]
        expected_output = (7, 7)
        self.assertEqual(sum_product(numbers), expected_output)

    def test_edge_negative_integers(self):
        # A list containing only negative integers.
        numbers = [-1, -2, -3]
        expected_output = (-6, -6)
        self.assertEqual(sum_product(numbers), expected_output)

    def test_edge_only_zeros(self):
        # A list containing only zeros.
        numbers = [0, 0, 0]
        expected_output = (0, 0)
        self.assertEqual(sum_product(numbers), expected_output)

    def test_error_input_none(self):
        # Input is not a list.
        numbers = None
        with self.assertRaises(TypeError):
            sum_product(numbers)

    def test_error_list_with_float(self):
        # Input list contains non-integer elements (float).
        numbers = [1, 2.5, 3]
        with self.assertRaises(TypeError):
            sum_product(numbers)

    def test_error_list_with_string(self):
        # Input list contains non-integer elements (string).
        numbers = [1, 'a', 3]
        with self.assertRaises(TypeError):
            sum_product(numbers)