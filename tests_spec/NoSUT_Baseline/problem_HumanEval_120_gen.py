import unittest
import sut.problem_HumanEval_120 as mod

class TestHybrid(unittest.TestCase):
    def test_example_1(self):
            # Typical input from docstring
            arr = [-3, -4, 5]
            k = 3
            expected_output = [-4, -3, 5]
            self.assertListEqual(mod.maximum(arr, k), expected_output)

    def test_example_2(self):
            # Typical input with duplicates from docstring
            arr = [4, -4, 4]
            k = 2
            expected_output = [4, 4]
            self.assertListEqual(mod.maximum(arr, k), expected_output)

    def test_k_is_zero(self):
            # Boundary condition: k = 0 (minimum allowed k)
            arr = [1, 2, 3, 4, 5]
            k = 0
            expected_output = []
            self.assertListEqual(mod.maximum(arr, k), expected_output)

    def test_k_equals_len_arr(self):
            # Boundary condition: k = len(arr) (maximum allowed k)
            arr = [5, 1, 9, 2, 7]
            k = 5
            expected_output = [1, 2, 5, 7, 9]
            self.assertListEqual(mod.maximum(arr, k), expected_output)

    def test_single_element_array(self):
            # Edge case: array with a single element (minimum len(arr))
            arr = [100]
            k = 1
            expected_output = [100]
            self.assertListEqual(mod.maximum(arr, k), expected_output)

    def test_mixed_numbers_with_zero(self):
            # Typical input: mixed positive, negative, and zero values
            arr = [-5, 0, 5, -2, 3, 1]
            k = 4
            expected_output = [0, 1, 3, 5]
            self.assertListEqual(mod.maximum(arr, k), expected_output)

    def test_duplicates_and_off_by_one_k(self):
            # Logic mutation: duplicates, and k is one less than len(arr)
            arr = [10, 1, 10, 5, 10]
            k = 4
            expected_output = [5, 10, 10, 10]
            self.assertListEqual(mod.maximum(arr, k), expected_output)

    def test_min_max_values_and_k_minus_one(self):
            # Extreme input: array with min/max possible values, k is len(arr)-1
            arr = [-1000, 0, 1000, -500, 500]
            k = 4
            expected_output = [-500, 0, 500, 1000]
            self.assertListEqual(mod.maximum(arr, k), expected_output)

    def test_all_same_values(self):
            # Edge case: array with all identical values
            arr = [7, 7, 7, 7, 7, 7]
            k = 3
            expected_output = [7, 7, 7]
            self.assertListEqual(mod.maximum(arr, k), expected_output)

    def test_normal_mixed_positive_negative_k_full_length(self):
            # Example 1: k equals array length, mixed positive/negative.
            arr = [-3, -4, 5]
            k = 3
            expected_output = [-4, -3, 5]
            self.assertEqual(mod.maximum(arr, k), expected_output)

    def test_normal_duplicate_maximums(self):
            # Example 2: k less than array length, duplicate maximums.
            arr = [4, -4, 4]
            k = 2
            expected_output = [4, 4]
            self.assertEqual(mod.maximum(arr, k), expected_output)

    def test_normal_k_is_one(self):
            # Example 3: k is 1, single maximum.
            arr = [-3, 2, 1, 2, -1, -2, 1]
            k = 1
            expected_output = [2]
            self.assertEqual(mod.maximum(arr, k), expected_output)

    def test_edge_k_is_zero(self):
            # k is 0, should return an empty list.
            arr = [1, 2, 3, 4, 5]
            k = 0
            expected_output = []
            self.assertEqual(mod.maximum(arr, k), expected_output)

    def test_edge_min_max_range_elements(self):
            # k equals array length, elements at min/max range, includes zero.
            arr = [1000, -1000, 0, 500]
            k = 4
            expected_output = [-1000, 0, 500, 1000]
            self.assertEqual(mod.maximum(arr, k), expected_output)

    def test_edge_single_element_array(self):
            # Array with minimum length 1, k is 1.
            arr = [7]
            k = 1
            expected_output = [7]
            self.assertEqual(mod.maximum(arr, k), expected_output)

    def test_edge_only_negative_numbers(self):
            # Array contains only negative numbers.
            arr = [-5, -1, -10, -2]
            k = 2
            expected_output = [-2, -1]
            self.assertEqual(mod.maximum(arr, k), expected_output)

    def test_error_arr_contains_non_integer(self):
            # Array contains non-integer elements.
            arr = [1, "a", 3]
            k = 2
            with self.assertRaises(TypeError):
                mod.maximum(arr, k)

    def test_error_k_not_integer(self):
            # k is not an integer.
            arr = [1, 2, 3]
            k = "2"
            with self.assertRaises(TypeError):
                mod.maximum(arr, k)

