import unittest
from sut.problem_HumanEval_70 import strange_sort_list

class Test_strange_sort_list(unittest.TestCase):

    def test_normal_sorted_list(self):
        # Description: Alternating min/max for a sorted list.
        lst = [1, 2, 3, 4]
        expected_output = [1, 4, 2, 3]
        self.assertEqual(strange_sort_list(lst), expected_output)

    def test_normal_identical_elements(self):
        # Description: List with all identical elements.
        lst = [5, 5, 5, 5]
        expected_output = [5, 5, 5, 5]
        self.assertEqual(strange_sort_list(lst), expected_output)

    def test_normal_unsorted_odd_length(self):
        # Description: Unsorted list with odd number of elements.
        lst = [10, 1, 8, 3, 6]
        expected_output = [1, 10, 3, 8, 6]
        self.assertEqual(strange_sort_list(lst), expected_output)

    def test_normal_mixed_signs(self):
        # Description: List with negative, zero, and positive integers.
        lst = [-5, 0, 5, -10]
        expected_output = [-10, 5, -5, 0]
        self.assertEqual(strange_sort_list(lst), expected_output)

    def test_edge_empty_list(self):
        # Description: Empty list.
        lst = []
        expected_output = []
        self.assertEqual(strange_sort_list(lst), expected_output)

    def test_edge_single_element(self):
        # Description: Single element list.
        lst = [7]
        expected_output = [7]
        self.assertEqual(strange_sort_list(lst), expected_output)

    def test_edge_two_elements_sorted(self):
        # Description: Two element list.
        lst = [10, 20]
        expected_output = [10, 20]
        self.assertEqual(strange_sort_list(lst), expected_output)

    def test_edge_two_elements_reverse_sorted(self):
        # Description: Two element list, reverse sorted.
        lst = [20, 10]
        expected_output = [10, 20]
        self.assertEqual(strange_sort_list(lst), expected_output)

    def test_error_input_none(self):
        # Description: Input is not a list (None).
        lst = None
        with self.assertRaises(TypeError):
            strange_sort_list(lst)

    def test_error_input_string(self):
        # Description: Input is a string, not a list.
        lst = "not a list"
        with self.assertRaises(TypeError):
            strange_sort_list(lst)

    def test_error_list_with_string(self):
        # Description: List contains non-integer elements (string).
        lst = [1, 2, "three", 4]
        with self.assertRaises(TypeError): # Expecting TypeError due to comparison of int and str
            strange_sort_list(lst)

    def test_error_list_with_float(self):
        # Description: List contains non-integer elements (float).
        lst = [1, 2.5, 3]
        with self.assertRaises(TypeError): # Expecting TypeError due to comparison of int and float
            strange_sort_list(lst)