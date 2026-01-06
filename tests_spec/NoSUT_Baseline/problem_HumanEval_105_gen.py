import unittest
import sut.problem_HumanEval_105 as mod

class TestHybrid(unittest.TestCase):
    def test_example_from_docstring_1(self):
            # Typical input with duplicates and mixed order, covering multiple steps
            arr = [2, 1, 1, 4, 5, 8, 2, 3]
            expected = ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
            self.assertListEqual(mod.by_length(arr), expected)

    def test_example_from_docstring_2_mixed_invalid(self):
            # Input with valid, negative, and large invalid numbers.
            # Tests filtering logic and handling of non-relevant numbers.
            arr = [1, -1, 55]
            expected = ['One']
            self.assertListEqual(mod.by_length(arr), expected)

    def test_empty_array(self):
            # Edge case: empty input array.
            arr = []
            expected = []
            self.assertListEqual(mod.by_length(arr), expected)

    def test_single_valid_element(self):
            # Edge case: single valid element.
            arr = [5]
            expected = ['Five']
            self.assertListEqual(mod.by_length(arr), expected)

    def test_single_invalid_element_below_boundary(self):
            # Boundary test: single element just below the valid range (0).
            # Catches off-by-one errors like '<=' instead of '<' for lower bound.
            arr = [0]
            expected = []
            self.assertListEqual(mod.by_length(arr), expected)

    def test_single_invalid_element_above_boundary(self):
            # Boundary test: single element just above the valid range (10).
            # Catches off-by-one errors like '>=' instead of '>' for upper bound.
            arr = [10]
            expected = []
            self.assertListEqual(mod.by_length(arr), expected)

    def test_all_valid_boundary_values(self):
            # Boundary test: array containing only the exact boundary values (1 and 9).
            arr = [1, 9]
            expected = ['Nine', 'One']
            self.assertListEqual(mod.by_length(arr), expected)

    def test_all_invalid_values_mixed(self):
            # Extreme input: array with only invalid numbers, including negative, zero, and large.
            # Tests robust filtering and ensures an empty list is returned.
            arr = [0, -5, 10, 100, -100]
            expected = []
            self.assertListEqual(mod.by_length(arr), expected)

    def test_duplicates_and_boundary_values(self):
            # Input with duplicates and boundary values, testing sorting and mapping.
            arr = [1, 1, 9, 9, 5, 2]
            expected = ['Nine', 'Nine', 'Five', 'Two', 'One', 'One']
            self.assertListEqual(mod.by_length(arr), expected)

    def test_sorted_input_all_valid(self):
            # Typical input that is already sorted, primarily testing the reverse and mapping steps.
            arr = [3, 4, 5]
            expected = ['Five', 'Four', 'Three']
            self.assertListEqual(mod.by_length(arr), expected)

    def test_normal_multiple_elements(self):
            arr = [2, 1, 1, 4, 5, 8, 2, 3]
            expected_output = ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
            self.assertEqual(mod.by_length(arr), expected_output)

    def test_normal_distinct_elements(self):
            arr = [9, 7, 3, 6]
            expected_output = ["Nine", "Seven", "Six", "Three"]
            self.assertEqual(mod.by_length(arr), expected_output)

    def test_normal_duplicate_valid_elements(self):
            arr = [5, 5, 5]
            expected_output = ["Five", "Five", "Five"]
            self.assertEqual(mod.by_length(arr), expected_output)

    def test_edge_empty_input_list(self):
            arr = []
            expected_output = []
            self.assertEqual(mod.by_length(arr), expected_output)

    def test_edge_mixed_valid_and_invalid_numbers(self):
            arr = [1, -1, 55]
            expected_output = ["One"]
            self.assertEqual(mod.by_length(arr), expected_output)

    def test_edge_all_invalid_numbers(self):
            arr = [-10, 0, 10, 100]
            expected_output = []
            self.assertEqual(mod.by_length(arr), expected_output)

    def test_edge_min_and_max_valid_range(self):
            arr = [1, 9]
            expected_output = ["Nine", "One"]
            self.assertEqual(mod.by_length(arr), expected_output)

    def test_edge_single_valid_number(self):
            arr = [7]
            expected_output = ["Seven"]
            self.assertEqual(mod.by_length(arr), expected_output)

    def test_error_list_with_non_integer_elements(self):
            arr = [1, 2.5, "three"]
            with self.assertRaises(TypeError): # Expecting TypeError if comparison or other int-specific ops fail
                mod.by_length(arr)

