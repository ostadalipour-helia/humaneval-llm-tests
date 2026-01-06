import unittest
from sut.problem_HumanEval_120 import maximum

class Test_maximum(unittest.TestCase):

    def test_normal_mixed_positive_negative_k_full_length(self):
        # Example 1: k equals array length, mixed positive/negative.
        arr = [-3, -4, 5]
        k = 3
        expected_output = [-4, -3, 5]
        self.assertEqual(maximum(arr, k), expected_output)

    def test_normal_duplicate_maximums(self):
        # Example 2: k less than array length, duplicate maximums.
        arr = [4, -4, 4]
        k = 2
        expected_output = [4, 4]
        self.assertEqual(maximum(arr, k), expected_output)

    def test_normal_k_is_one(self):
        # Example 3: k is 1, single maximum.
        arr = [-3, 2, 1, 2, -1, -2, 1]
        k = 1
        expected_output = [2]
        self.assertEqual(maximum(arr, k), expected_output)

    def test_edge_k_is_zero(self):
        # k is 0, should return an empty list.
        arr = [1, 2, 3, 4, 5]
        k = 0
        expected_output = []
        self.assertEqual(maximum(arr, k), expected_output)

    def test_edge_min_max_range_elements(self):
        # k equals array length, elements at min/max range, includes zero.
        arr = [1000, -1000, 0, 500]
        k = 4
        expected_output = [-1000, 0, 500, 1000]
        self.assertEqual(maximum(arr, k), expected_output)

    def test_edge_single_element_array(self):
        # Array with minimum length 1, k is 1.
        arr = [7]
        k = 1
        expected_output = [7]
        self.assertEqual(maximum(arr, k), expected_output)

    def test_edge_only_negative_numbers(self):
        # Array contains only negative numbers.
        arr = [-5, -1, -10, -2]
        k = 2
        expected_output = [-2, -1]
        self.assertEqual(maximum(arr, k), expected_output)

    def test_error_empty_array(self):
        # Input array is empty (violates len(arr) >= 1).
        arr = []
        k = 0
        with self.assertRaises(ValueError):
            maximum(arr, k)

    def test_error_k_negative(self):
        # k is negative (violates k >= 0).
        arr = [1, 2, 3]
        k = -1
        with self.assertRaises(ValueError):
            maximum(arr, k)

    def test_error_k_greater_than_len_arr(self):
        # k is greater than len(arr) (violates k <= len(arr)).
        arr = [1, 2, 3]
        k = 4
        with self.assertRaises(ValueError):
            maximum(arr, k)

    def test_error_arr_contains_non_integer(self):
        # Array contains non-integer elements.
        arr = [1, "a", 3]
        k = 2
        with self.assertRaises(TypeError):
            maximum(arr, k)

    def test_error_k_not_integer(self):
        # k is not an integer.
        arr = [1, 2, 3]
        k = "2"
        with self.assertRaises(TypeError):
            maximum(arr, k)