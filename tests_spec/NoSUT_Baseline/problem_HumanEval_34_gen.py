import unittest
import sut.problem_HumanEval_34 as mod

class TestHybrid(unittest.TestCase):
    def test_01_docstring_example(self):
            # Test with the example provided in the docstring
            self.assertListEqual(mod.unique([5, 3, 5, 2, 3, 3, 9, 0, 123]), [0, 2, 3, 5, 9, 123])

    def test_02_empty_list(self):
            # Edge case: Test with an empty list
            self.assertListEqual(mod.unique([]), [])

    def test_03_single_element_list(self):
            # Edge case: Test with a list containing a single element
            self.assertListEqual(mod.unique([7]), [7])

    def test_04_all_identical_elements(self):
            # Edge case: Test with a list where all elements are identical
            self.assertListEqual(mod.unique([4, 4, 4, 4]), [4])

    def test_05_already_sorted_no_duplicates(self):
            # Boundary condition: Test with an already sorted list with no duplicates
            self.assertListEqual(mod.unique([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_06_reverse_sorted_no_duplicates(self):
            # Boundary condition: Test with a reverse sorted list with no duplicates
            self.assertListEqual(mod.unique([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_07_mixed_positive_negative_zero_duplicates(self):
            # Typical input: Test with a mix of positive, negative, and zero values, with duplicates
            self.assertListEqual(mod.unique([-3, 0, 5, -3, 2, 0, 1]), [-3, 0, 1, 2, 5])

    def test_08_large_numbers_and_many_duplicates(self):
            # Extreme input: Test with larger numbers and multiple duplicates
            self.assertListEqual(mod.unique([1000, 500, 1000, 200, 500, 1000, 100]), [100, 200, 500, 1000])

    def test_09_all_negative_numbers_duplicates(self):
            # Boundary condition: Test with only negative numbers and duplicates
            self.assertListEqual(mod.unique([-5, -1, -5, -3, -1, -2]), [-5, -3, -2, -1])

    def test_10_two_elements_one_duplicate(self):
            # Off-by-one error check: Test with a small list containing two identical elements
            self.assertListEqual(mod.unique([2, 2]), [2])

    def test_normal_duplicates_unsorted(self):
            # A list with multiple duplicate elements and unsorted order.
            input_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
            expected_output = [0, 2, 3, 5, 9, 123]
            self.assertEqual(mod.unique(input_list), expected_output)

    def test_normal_no_duplicates_sorted(self):
            # A list with no duplicate elements, already sorted.
            input_list = [1, 2, 3, 4]
            expected_output = [1, 2, 3, 4]
            self.assertEqual(mod.unique(input_list), expected_output)

    def test_normal_negative_zero_positive(self):
            # A list with negative numbers, zero, and positive numbers, with duplicates.
            input_list = [10, -5, 0, 7, -5]
            expected_output = [-5, 0, 7, 10]
            self.assertEqual(mod.unique(input_list), expected_output)

    def test_edge_empty_list(self):
            # An empty list.
            input_list = []
            expected_output = []
            self.assertEqual(mod.unique(input_list), expected_output)

    def test_edge_single_element(self):
            # A list with a single element.
            input_list = [7]
            expected_output = [7]
            self.assertEqual(mod.unique(input_list), expected_output)

    def test_edge_all_identical_elements(self):
            # A list with all identical elements.
            input_list = [4, 4, 4, 4]
            expected_output = [4]
            self.assertEqual(mod.unique(input_list), expected_output)

    def test_edge_strings_with_duplicates(self):
            # A list of strings with duplicates.
            input_list = ["b", "a", "c", "b"]
            expected_output = ["a", "b", "c"]
            self.assertEqual(mod.unique(input_list), expected_output)

    def test_error_input_none(self):
            # Input is not a list (e.g., None).
            with self.assertRaises(TypeError):
                mod.unique(None)

    def test_error_input_integer(self):
            # Input is not a list (e.g., an integer).
            with self.assertRaises(TypeError):
                mod.unique(123)

    def test_error_non_comparable_elements(self):
            # Input list contains non-comparable elements, leading to a TypeError during sorting.
            with self.assertRaises(TypeError):
                mod.unique([1, "a", {}])

