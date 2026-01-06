import unittest
from sut.problem_HumanEval_88 import sort_array

class Test_sort_array(unittest.TestCase):

    def test_normal_odd_sum_ascending(self):
        # Sum of first (2) and last (5) elements is 7 (odd), so sort ascending.
        input_array = [2, 4, 3, 0, 1, 5]
        original_array_copy = list(input_array)
        expected_output = [0, 1, 2, 3, 4, 5]
        
        result = sort_array(input_array)
        
        self.assertEqual(result, expected_output)
        self.assertEqual(input_array, original_array_copy, "Original array should not be modified")
        self.assertIsNot(result, input_array, "Returned list should be a new list")

    def test_normal_even_sum_descending(self):
        # Sum of first (2) and last (6) elements is 8 (even), so sort descending.
        input_array = [2, 4, 3, 0, 1, 5, 6]
        original_array_copy = list(input_array)
        expected_output = [6, 5, 4, 3, 2, 1, 0]
        
        result = sort_array(input_array)
        
        self.assertEqual(result, expected_output)
        self.assertEqual(input_array, original_array_copy, "Original array should not be modified")
        self.assertIsNot(result, input_array, "Returned list should be a new list")

    def test_edge_empty_array(self):
        # Empty array, returns a copy of itself. Length < 2.
        input_array = []
        original_array_copy = list(input_array)
        expected_output = []
        
        result = sort_array(input_array)
        
        self.assertEqual(result, expected_output)
        self.assertEqual(input_array, original_array_copy, "Original array should not be modified")
        self.assertIsNot(result, input_array, "Returned list should be a new list")

    def test_edge_single_element(self):
        # Single element array, returns a copy of itself. Length < 2.
        input_array = [5]
        original_array_copy = list(input_array)
        expected_output = [5]
        
        result = sort_array(input_array)
        
        self.assertEqual(result, expected_output)
        self.assertEqual(input_array, original_array_copy, "Original array should not be modified")
        self.assertIsNot(result, input_array, "Returned list should be a new list")

    def test_edge_two_elements_odd_sum_ascending(self):
        # Sum of first (2) and last (1) elements is 3 (odd), so sort ascending.
        input_array = [2, 1]
        original_array_copy = list(input_array)
        expected_output = [1, 2]
        
        result = sort_array(input_array)
        
        self.assertEqual(result, expected_output)
        self.assertEqual(input_array, original_array_copy, "Original array should not be modified")
        self.assertIsNot(result, input_array, "Returned list should be a new list")

    def test_edge_two_elements_even_sum_descending(self):
        # Sum of first (2) and last (4) elements is 6 (even), so sort descending.
        input_array = [2, 4]
        original_array_copy = list(input_array)
        expected_output = [4, 2]
        
        result = sort_array(input_array)
        
        self.assertEqual(result, expected_output)
        self.assertEqual(input_array, original_array_copy, "Original array should not be modified")
        self.assertIsNot(result, input_array, "Returned list should be a new list")

    def test_edge_all_identical_elements_even_sum(self):
        # All elements are identical. Sum of first (3) and last (3) is 6 (even), so sort descending.
        input_array = [3, 3, 3]
        original_array_copy = list(input_array)
        expected_output = [3, 3, 3]
        
        result = sort_array(input_array)
        
        self.assertEqual(result, expected_output)
        self.assertEqual(input_array, original_array_copy, "Original array should not be modified")
        self.assertIsNot(result, input_array, "Returned list should be a new list")

    def test_edge_with_zero_odd_sum(self):
        # Array contains zero. Sum of first (0) and last (5) is 5 (odd), so sort ascending.
        input_array = [0, 10, 5]
        original_array_copy = list(input_array)
        expected_output = [0, 5, 10]
        
        result = sort_array(input_array)
        
        self.assertEqual(result, expected_output)
        self.assertEqual(input_array, original_array_copy, "Original array should not be modified")
        self.assertIsNot(result, input_array, "Returned list should be a new list")

    def test_error_input_not_list_none(self):
        # Input 'array' is not a list.
        with self.assertRaises(TypeError):
            sort_array(None)

    def test_error_input_not_list_int(self):
        # Input 'array' is not a list.
        with self.assertRaises(TypeError):
            sort_array(123)

    def test_error_contains_float(self):
        # Array contains non-integer elements.
        with self.assertRaises(TypeError): # Spec allows TypeError or ValueError
            sort_array([1, 2.5, 3])

    def test_error_contains_string(self):
        # Array contains non-integer elements.
        with self.assertRaises(TypeError): # Spec allows TypeError or ValueError
            sort_array([1, 'a', 3])

    def test_error_contains_negative(self):
        # Array contains negative integers.
        with self.assertRaises(ValueError):
            sort_array([1, -2, 3])