import unittest
from sut.problem_HumanEval_73 import smallest_change

class Test_smallest_change(unittest.TestCase):

    def test_normal_multiple_changes(self):
        # Array requiring multiple changes to become palindromic.
        arr = [1, 2, 3, 5, 4, 7, 9, 6]
        expected_output = 4
        self.assertEqual(smallest_change(arr), expected_output)

    def test_normal_single_change(self):
        # Array requiring a single change to become palindromic.
        arr = [1, 2, 3, 4, 3, 2, 2]
        expected_output = 1
        self.assertEqual(smallest_change(arr), expected_output)

    def test_normal_already_palindromic(self):
        # Array that is already palindromic.
        arr = [1, 2, 3, 2, 1]
        expected_output = 0
        self.assertEqual(smallest_change(arr), expected_output)

    def test_edge_empty_array(self):
        # Empty array (already palindromic).
        arr = []
        expected_output = 0
        self.assertEqual(smallest_change(arr), expected_output)

    def test_edge_single_element_array(self):
        # Single-element array (already palindromic).
        arr = [5]
        expected_output = 0
        self.assertEqual(smallest_change(arr), expected_output)

    def test_edge_even_length_all_different(self):
        # Even length array, all different elements.
        arr = [1, 2, 3, 4]
        expected_output = 2
        self.assertEqual(smallest_change(arr), expected_output)

    def test_edge_negative_and_zero_elements(self):
        # Array with negative and zero integers (already palindromic).
        arr = [-1, 0, 1, 0, -1]
        expected_output = 0
        self.assertEqual(smallest_change(arr), expected_output)

    def test_error_arr_is_none(self):
        # Input `arr` is not a list (None).
        arr = None
        with self.assertRaises(TypeError):
            smallest_change(arr)

    def test_error_arr_is_string(self):
        # Input `arr` is not a list (string).
        arr = "not_a_list"
        with self.assertRaises(TypeError):
            smallest_change(arr)

    def test_error_arr_contains_float(self):
        # Array contains non-integer elements (float).
        arr = [1, 2.5, 3]
        with self.assertRaises(TypeError):
            smallest_change(arr)

    def test_error_arr_contains_string(self):
        # Array contains non-integer elements (string).
        arr = [1, "a", 3]
        with self.assertRaises(TypeError):
            smallest_change(arr)