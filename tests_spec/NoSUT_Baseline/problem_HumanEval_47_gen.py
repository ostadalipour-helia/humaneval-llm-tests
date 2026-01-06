import unittest
import sut.problem_HumanEval_47 as mod

class TestHybrid(unittest.TestCase):
    def test_docstring_example_1_odd_length(self):
            """Test with the first example from the docstring (odd length list)."""
            self.assertEqual(mod.median([3, 1, 2, 4, 5]), 3)

    def test_single_element_list_boundary(self):
            """Test with a list containing a single element (smallest odd length)."""
            self.assertEqual(mod.median([7]), 7)

    def test_two_element_list_boundary(self):
            """Test with a list containing two elements (smallest even length)."""
            self.assertEqual(mod.median([10, 20]), 15.0)

    def test_odd_length_negative_numbers(self):
            """Test with an odd length list containing only negative numbers."""
            self.assertEqual(mod.median([-5, -1, -3]), -3)

    def test_even_length_negative_numbers(self):
            """Test with an even length list containing only negative numbers."""
            self.assertEqual(mod.median([-10, -20, -30, -40]), -25.0)

    def test_list_with_zero_and_mixed_signs(self):
            """Test with a list containing zero and mixed positive/negative numbers."""
            self.assertEqual(mod.median([-5, 0, 5]), 0)

    def test_list_with_duplicates(self):
            """Test with a list containing duplicate values."""
            self.assertEqual(mod.median([1, 5, 2, 5, 3]), 3)

    def test_list_all_same_values(self):
            """Test with a list where all elements are the same."""
            self.assertEqual(mod.median([7, 7, 7, 7]), 7.0)

    def test_larger_even_list_mixed_values(self):
            """Test with a larger even length list with mixed values to check index calculation."""
            # Sorted: [0, 1, 2, 3, 4, 50, 99, 100]
            # Middle elements: 3, 4. Median: (3+4)/2 = 3.5
            self.assertEqual(mod.median([100, 1, 50, 2, 99, 3, 4, 0]), 3.5)
    
    if __name__ == '__main__':
        unittest.main()

    def test_normal_odd_length_integers(self):
            # Normal case: odd length list of integers
            input_list = [3, 1, 2, 4, 5]
            original_list_copy = list(input_list) # For invariant check
            expected_output = 3
            result = mod.median(input_list)
            self.assertEqual(result, expected_output)
            self.assertEqual(input_list, original_list_copy) # Invariant check

    def test_normal_even_length_mixed_numbers(self):
            # Normal case: even length list with mixed integers and floats, negative numbers
            input_list = [-10, 4, 6, 10, 20, 1000]
            original_list_copy = list(input_list) # For invariant check
            expected_output = 8.0
            result = mod.median(input_list)
            self.assertEqual(result, expected_output)
            self.assertEqual(input_list, original_list_copy) # Invariant check

    def test_normal_even_length_floats(self):
            # Normal case: even length list of floats
            input_list = [1.0, 2.5, 3.0, 4.5]
            expected_output = 2.75
            result = mod.median(input_list)
            self.assertEqual(result, expected_output)

    def test_edge_single_element_list(self):
            # Edge case: list with a single element
            input_list = [7]
            expected_output = 7
            result = mod.median(input_list)
            self.assertEqual(result, expected_output)

    def test_edge_two_elements_list(self):
            # Edge case: list with two elements
            input_list = [10, 20]
            expected_output = 15.0
            result = mod.median(input_list)
            self.assertEqual(result, expected_output)

    def test_edge_all_same_elements(self):
            # Edge case: list with all identical elements
            input_list = [5, 5, 5, 5]
            expected_output = 5.0
            result = mod.median(input_list)
            self.assertEqual(result, expected_output)

    def test_edge_negative_numbers(self):
            # Edge case: list with only negative numbers
            input_list = [-1, -2, -3]
            expected_output = -2
            result = mod.median(input_list)
            self.assertEqual(result, expected_output)

    def test_error_non_numeric_element(self):
            # Error case: list containing a non-numeric element (string)
            with self.assertRaises(TypeError):
                mod.median([1, 2, 'a'])

    def test_error_none_input(self):
            # Error case: input is None
            with self.assertRaises(TypeError):
                mod.median(None)

    def test_error_string_input(self):
            # Error case: input is a string, not a list
            with self.assertRaises(TypeError):
                mod.median("not a list")

    def test_error_list_with_none_element(self):
            # Error case: list containing None as an element
            with self.assertRaises(TypeError):
                mod.median([1, 2, None])

