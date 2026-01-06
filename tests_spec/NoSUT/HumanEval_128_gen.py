import unittest
from sut.problem_HumanEval_128 import prod_signs

class Test_prod_signs(unittest.TestCase):

    def test_normal_mixed_signs(self):
        # Description: Mixed positive and negative numbers, non-zero result.
        self.assertEqual(prod_signs([1, 2, 2, -4]), -9)

    def test_normal_contains_zero(self):
        # Description: Contains a zero, resulting in a zero product.
        self.assertEqual(prod_signs([0, 1]), 0)

    def test_normal_all_positive(self):
        # Description: All positive numbers.
        self.assertEqual(prod_signs([1, 2, 3]), 6)

    def test_normal_all_negative(self):
        # Description: All negative numbers.
        self.assertEqual(prod_signs([-1, -2, -3]), -6)

    def test_edge_empty_array(self):
        # Description: Empty array.
        self.assertIsNone(prod_signs([]))

    def test_edge_single_zero(self):
        # Description: Array with a single zero.
        self.assertEqual(prod_signs([0]), 0)

    def test_edge_single_positive(self):
        # Description: Array with a single positive number.
        self.assertEqual(prod_signs([1]), 1)

    def test_edge_single_negative(self):
        # Description: Array with a single negative number.
        self.assertEqual(prod_signs([-1]), -1)

    def test_edge_multiple_zeros(self):
        # Description: Array with multiple zeros.
        self.assertEqual(prod_signs([0, 0, 0]), 0)

    def test_edge_large_numbers(self):
        # Description: Large numbers, resulting in a large magnitude sum.
        self.assertEqual(prod_signs([1000000, -1000000]), -2000000)

    def test_error_input_not_list_none(self):
        # Description: Input is not a list (None).
        with self.assertRaises(TypeError):
            prod_signs(None)

    def test_error_input_not_list_int(self):
        # Description: Input is an integer, not a list.
        with self.assertRaises(TypeError):
            prod_signs(123)

    def test_error_list_contains_float(self):
        # Description: Array contains non-integer (float) elements.
        with self.assertRaises(TypeError):
            prod_signs([1, 2.5, 3])

    def test_error_list_contains_string(self):
        # Description: Array contains non-integer (string) elements.
        with self.assertRaises(TypeError):
            prod_signs([1, 'a', 3])