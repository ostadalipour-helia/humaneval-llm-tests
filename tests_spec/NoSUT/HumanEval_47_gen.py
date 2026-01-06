import unittest
from sut.problem_HumanEval_47 import median

class Test_median(unittest.TestCase):

    def test_normal_odd_length_integers(self):
        # Normal case: odd length list of integers
        input_list = [3, 1, 2, 4, 5]
        original_list_copy = list(input_list) # For invariant check
        expected_output = 3
        result = median(input_list)
        self.assertEqual(result, expected_output)
        self.assertEqual(input_list, original_list_copy) # Invariant check

    def test_normal_even_length_mixed_numbers(self):
        # Normal case: even length list with mixed integers and floats, negative numbers
        input_list = [-10, 4, 6, 10, 20, 1000]
        original_list_copy = list(input_list) # For invariant check
        expected_output = 8.0
        result = median(input_list)
        self.assertEqual(result, expected_output)
        self.assertEqual(input_list, original_list_copy) # Invariant check

    def test_normal_even_length_floats(self):
        # Normal case: even length list of floats
        input_list = [1.0, 2.5, 3.0, 4.5]
        expected_output = 2.75
        result = median(input_list)
        self.assertEqual(result, expected_output)

    def test_edge_single_element_list(self):
        # Edge case: list with a single element
        input_list = [7]
        expected_output = 7
        result = median(input_list)
        self.assertEqual(result, expected_output)

    def test_edge_two_elements_list(self):
        # Edge case: list with two elements
        input_list = [10, 20]
        expected_output = 15.0
        result = median(input_list)
        self.assertEqual(result, expected_output)

    def test_edge_all_same_elements(self):
        # Edge case: list with all identical elements
        input_list = [5, 5, 5, 5]
        expected_output = 5.0
        result = median(input_list)
        self.assertEqual(result, expected_output)

    def test_edge_negative_numbers(self):
        # Edge case: list with only negative numbers
        input_list = [-1, -2, -3]
        expected_output = -2
        result = median(input_list)
        self.assertEqual(result, expected_output)

    def test_error_empty_list(self):
        # Error case: empty list
        with self.assertRaises(ValueError):
            median([])

    def test_error_non_numeric_element(self):
        # Error case: list containing a non-numeric element (string)
        with self.assertRaises(TypeError):
            median([1, 2, 'a'])

    def test_error_none_input(self):
        # Error case: input is None
        with self.assertRaises(TypeError):
            median(None)

    def test_error_string_input(self):
        # Error case: input is a string, not a list
        with self.assertRaises(TypeError):
            median("not a list")

    def test_error_list_with_none_element(self):
        # Error case: list containing None as an element
        with self.assertRaises(TypeError):
            median([1, 2, None])