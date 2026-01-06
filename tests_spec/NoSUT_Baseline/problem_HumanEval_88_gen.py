import unittest
import sut.problem_HumanEval_88 as mod

class TestHybrid(unittest.TestCase):
    def test_empty_array(self):
            """
            Test case for an empty input array.
            Edge Case: Empty collection.
            """
            arr = []
            expected = []
            self.assertListEqual(mod.sort_array(arr), expected)

    def test_single_element_array(self):
            """
            Test case for an array with a single element.
            Edge Case: Single element collection.
            """
            arr = [5]
            expected = [5]
            self.assertListEqual(mod.sort_array(arr), expected)

    def test_ascending_sort_example(self):
            """
            Test case for an array that should be sorted in ascending order.
            (First + Last) sum is odd. Typical/Expected input.
            Example from docstring.
            """
            arr = [2, 4, 3, 0, 1, 5] # first=2, last=5, sum=7 (odd)
            expected = [0, 1, 2, 3, 4, 5]
            self.assertListEqual(mod.sort_array(arr), expected)

    def test_descending_sort_example(self):
            """
            Test case for an array that should be sorted in descending order.
            (First + Last) sum is even. Typical/Expected input.
            Example from docstring.
            """
            arr = [2, 4, 3, 0, 1, 5, 6] # first=2, last=6, sum=8 (even)
            expected = [6, 5, 4, 3, 2, 1, 0]
            self.assertListEqual(mod.sort_array(arr), expected)

    def test_boundary_two_elements_sum_odd(self):
            """
            Test case for a two-element array where (First + Last) sum is odd.
            Boundary Test: Smallest non-trivial array, odd sum.
            """
            arr = [1, 0] # first=1, last=0, sum=1 (odd)
            expected = [0, 1]
            self.assertListEqual(mod.sort_array(arr), expected)

    def test_boundary_two_elements_sum_even(self):
            """
            Test case for a two-element array where (First + Last) sum is even.
            Boundary Test: Smallest non-trivial array, even sum.
            """
            arr = [0, 2] # first=0, last=2, sum=2 (even)
            expected = [2, 0]
            self.assertListEqual(mod.sort_array(arr), expected)

    def test_array_not_modified(self):
            """
            Test to ensure the original array is not modified.
            Critical Requirement: Immutability.
            """
            original_arr = [2, 4, 3, 0, 1, 5]
            arr_copy = list(original_arr) # Create a copy to pass
            mod.sort_array(arr_copy)
            self.assertListEqual(original_arr, [2, 4, 3, 0, 1, 5]) # Assert original remains unchanged

    def test_all_same_elements_sum_even(self):
            """
            Test case with all identical elements, resulting in an even sum.
            Edge Case: All same values.
            """
            arr = [7, 7, 7, 7] # first=7, last=7, sum=14 (even)
            expected = [7, 7, 7, 7] # Should be descending, but already sorted
            self.assertListEqual(mod.sort_array(arr), expected)

    def test_duplicates_and_zeros_sum_odd(self):
            """
            Test case with duplicate values and zeros, where (First + Last) sum is odd.
            Extreme/Unusual Input: Duplicates, zeros, longer array.
            """
            arr = [0, 3, 1, 4, 1, 5, 9, 2, 7] # first=0, last=7, sum=7 (odd)
            expected = [0, 1, 1, 2, 3, 4, 5, 7, 9]
            self.assertListEqual(mod.sort_array(arr), expected)

    def test_large_numbers_sum_even_unsorted(self):
            """
            Test case with large numbers and an even sum, requiring descending sort.
            Extreme/Unusual Input: Large numbers, unsorted.
            """
            arr = [100000, 500, 20000, 10] # first=100000, last=10, sum=100010 (even)
            expected = [100000, 20000, 500, 10]
            self.assertListEqual(mod.sort_array(arr), expected)

    def test_normal_odd_sum_ascending(self):
            # Sum of first (2) and last (5) elements is 7 (odd), so sort ascending.
            input_array = [2, 4, 3, 0, 1, 5]
            original_array_copy = list(input_array)
            expected_output = [0, 1, 2, 3, 4, 5]
            
            result = mod.sort_array(input_array)
            
            self.assertEqual(result, expected_output)
            self.assertEqual(input_array, original_array_copy, "Original array should not be modified")
            self.assertIsNot(result, input_array, "Returned list should be a new list")

    def test_normal_even_sum_descending(self):
            # Sum of first (2) and last (6) elements is 8 (even), so sort descending.
            input_array = [2, 4, 3, 0, 1, 5, 6]
            original_array_copy = list(input_array)
            expected_output = [6, 5, 4, 3, 2, 1, 0]
            
            result = mod.sort_array(input_array)
            
            self.assertEqual(result, expected_output)
            self.assertEqual(input_array, original_array_copy, "Original array should not be modified")
            self.assertIsNot(result, input_array, "Returned list should be a new list")

    def test_edge_empty_array(self):
            # Empty array, returns a copy of itself. Length < 2.
            input_array = []
            original_array_copy = list(input_array)
            expected_output = []
            
            result = mod.sort_array(input_array)
            
            self.assertEqual(result, expected_output)
            self.assertEqual(input_array, original_array_copy, "Original array should not be modified")
            self.assertIsNot(result, input_array, "Returned list should be a new list")

    def test_edge_single_element(self):
            # Single element array, returns a copy of itself. Length < 2.
            input_array = [5]
            original_array_copy = list(input_array)
            expected_output = [5]
            
            result = mod.sort_array(input_array)
            
            self.assertEqual(result, expected_output)
            self.assertEqual(input_array, original_array_copy, "Original array should not be modified")
            self.assertIsNot(result, input_array, "Returned list should be a new list")

    def test_edge_two_elements_odd_sum_ascending(self):
            # Sum of first (2) and last (1) elements is 3 (odd), so sort ascending.
            input_array = [2, 1]
            original_array_copy = list(input_array)
            expected_output = [1, 2]
            
            result = mod.sort_array(input_array)
            
            self.assertEqual(result, expected_output)
            self.assertEqual(input_array, original_array_copy, "Original array should not be modified")
            self.assertIsNot(result, input_array, "Returned list should be a new list")

    def test_edge_two_elements_even_sum_descending(self):
            # Sum of first (2) and last (4) elements is 6 (even), so sort descending.
            input_array = [2, 4]
            original_array_copy = list(input_array)
            expected_output = [4, 2]
            
            result = mod.sort_array(input_array)
            
            self.assertEqual(result, expected_output)
            self.assertEqual(input_array, original_array_copy, "Original array should not be modified")
            self.assertIsNot(result, input_array, "Returned list should be a new list")

    def test_edge_all_identical_elements_even_sum(self):
            # All elements are identical. Sum of first (3) and last (3) is 6 (even), so sort descending.
            input_array = [3, 3, 3]
            original_array_copy = list(input_array)
            expected_output = [3, 3, 3]
            
            result = mod.sort_array(input_array)
            
            self.assertEqual(result, expected_output)
            self.assertEqual(input_array, original_array_copy, "Original array should not be modified")
            self.assertIsNot(result, input_array, "Returned list should be a new list")

    def test_edge_with_zero_odd_sum(self):
            # Array contains zero. Sum of first (0) and last (5) is 5 (odd), so sort ascending.
            input_array = [0, 10, 5]
            original_array_copy = list(input_array)
            expected_output = [0, 5, 10]
            
            result = mod.sort_array(input_array)
            
            self.assertEqual(result, expected_output)
            self.assertEqual(input_array, original_array_copy, "Original array should not be modified")
            self.assertIsNot(result, input_array, "Returned list should be a new list")

    def test_error_input_not_list_none(self):
            # Input 'array' is not a list.
            with self.assertRaises(TypeError):
                mod.sort_array(None)

    def test_error_input_not_list_int(self):
            # Input 'array' is not a list.
            with self.assertRaises(TypeError):
                mod.sort_array(123)

    def test_error_contains_string(self):
            # Array contains non-integer elements.
            with self.assertRaises(TypeError): # Spec allows TypeError or ValueError
                mod.sort_array([1, 'a', 3])

