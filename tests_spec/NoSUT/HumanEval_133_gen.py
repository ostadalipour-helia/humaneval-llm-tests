import unittest
from sut.problem_HumanEval_133 import sum_squares

class Test_sum_squares(unittest.TestCase):
    def test_normal_all_positive_integers(self):
        # Description: All positive integers.
        original_lst = [1, 2, 3]
        lst_to_pass = list(original_lst) # Create a copy to check invariant
        result = sum_squares(lst_to_pass)
        self.assertEqual(result, 14)
        self.assertEqual(lst_to_pass, original_lst, "Input list should not be modified.")

    def test_normal_mixed_floats_and_zero(self):
        # Description: Mixed positive floats and zero, demonstrating ceiling operation.
        original_lst = [1.4, 4.2, 0]
        lst_to_pass = list(original_lst) # Create a copy to check invariant
        result = sum_squares(lst_to_pass)
        self.assertEqual(result, 29)
        self.assertEqual(lst_to_pass, original_lst, "Input list should not be modified.")

    def test_normal_mixed_negative_float(self):
        # Description: Mixed negative float and positive integers, demonstrating ceiling operation for negative numbers.
        lst = [-2.4, 1, 1]
        result = sum_squares(lst)
        self.assertEqual(result, 6)

    def test_edge_empty_list(self):
        # Description: An empty list should return 0.
        lst = []
        result = sum_squares(lst)
        self.assertEqual(result, 0)

    def test_edge_single_positive_float(self):
        # Description: A list with a single positive float, demonstrating ceiling.
        lst = [3.1]
        result = sum_squares(lst)
        self.assertEqual(result, 16) # ceil(3.1) = 4, 4*4 = 16

    def test_edge_only_negative_floats(self):
        # Description: A list with only negative floats, demonstrating ceiling for negative numbers.
        lst = [-1.5, -3.8]
        result = sum_squares(lst)
        self.assertEqual(result, 10) # ceil(-1.5) = -1, ceil(-3.8) = -3. (-1)^2 + (-3)^2 = 1 + 9 = 10

    def test_edge_numbers_close_to_zero(self):
        # Description: Numbers close to zero, demonstrating ceiling behavior.
        lst = [0.1, -0.1]
        result = sum_squares(lst)
        self.assertEqual(result, 1) # ceil(0.1) = 1, ceil(-0.1) = 0. 1^2 + 0^2 = 1

    def test_error_input_is_none(self):
        # Description: Input is not a list (e.g., None).
        with self.assertRaises(TypeError):
            sum_squares(None)

    def test_error_input_is_string(self):
        # Description: Input is not a list (e.g., string).
        with self.assertRaises(TypeError):
            sum_squares("not_a_list")

    def test_error_list_contains_string(self):
        # Description: List contains non-numeric elements (e.g., string).
        with self.assertRaises(TypeError):
            sum_squares([1, "a", 3])

    def test_error_list_contains_nested_list(self):
        # Description: List contains non-numeric elements (e.g., nested list).
        with self.assertRaises(TypeError):
            sum_squares([1, [2, 3], 4])