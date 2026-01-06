import unittest
from sut.problem_HumanEval_122 import add_elements

class Test_add_elements(unittest.TestCase):

    def test_normal_example_docstring(self):
        # Example from docstring: sum of 21 and 3 from the first 4 elements.
        arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9]
        k = 4
        arr_copy = list(arr) # For invariant check
        result = add_elements(arr, k)
        self.assertEqual(result, 24)
        self.assertEqual(arr, arr_copy) # Invariant check

    def test_normal_none_first_k_valid(self):
        # None of the first k elements have at most two digits.
        arr = [1000, 200, 300, 400, 500]
        k = 5
        arr_copy = list(arr)
        result = add_elements(arr, k)
        self.assertEqual(result, 0)
        self.assertEqual(arr, arr_copy)

    def test_normal_includes_negative(self):
        # Includes negative numbers with at most two digits.
        arr = [10, -20, 30, 100, 50]
        k = 4
        arr_copy = list(arr)
        result = add_elements(arr, k)
        self.assertEqual(result, 20) # 10 + (-20) + 30 = 20
        self.assertEqual(arr, arr_copy)

    def test_edge_k_is_one(self):
        # k is 1, only the first element is considered.
        arr = [5, 100, 200]
        k = 1
        arr_copy = list(arr)
        result = add_elements(arr, k)
        self.assertEqual(result, 5)
        self.assertEqual(arr, arr_copy)

    def test_edge_k_equals_len_arr(self):
        # k is equal to len(arr), all elements are considered.
        arr = [10, 20, 30]
        k = 3
        arr_copy = list(arr)
        result = add_elements(arr, k)
        self.assertEqual(result, 60) # 10 + 20 + 30 = 60
        self.assertEqual(arr, arr_copy)

    def test_edge_contains_zero(self):
        # Array contains zero, which has at most two digits.
        arr = [0, 10, 100]
        k = 2
        arr_copy = list(arr)
        result = add_elements(arr, k)
        self.assertEqual(result, 10) # 0 + 10 = 10
        self.assertEqual(arr, arr_copy)

    def test_edge_boundary_values(self):
        # Boundary values for 'at most two digits' (99, -99 included; 100, -100 excluded).
        arr = [99, -99, 100, -100]
        k = 4
        arr_copy = list(arr)
        result = add_elements(arr, k)
        self.assertEqual(result, 0) # 99 + (-99) = 0
        self.assertEqual(arr, arr_copy)

    def test_edge_max_len_arr_k_max(self):
        # Maximum length array and k is 100, all elements are included (sum of 1 to 99).
        arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
        k = 100
        arr_copy = list(arr)
        result = add_elements(arr, k)
        # The sum of numbers from 1 to 99 is (99 * 100) / 2 = 4950.
        # The given array contains 10, 20, ..., 90 (sum 450) and 1, 2, ..., 99 (sum 4950).
        # All elements are within [-99, 99] range.
        self.assertEqual(result, 4950)
        self.assertEqual(arr, arr_copy)

    def test_error_arr_empty(self):
        # arr is empty (violates 1 <= len(arr)).
        arr = []
        k = 0
        with self.assertRaises(ValueError):
            add_elements(arr, k)

    def test_error_k_less_than_one(self):
        # k is less than 1 (violates 1 <= k).
        arr = [1, 2, 3]
        k = 0
        with self.assertRaises(ValueError):
            add_elements(arr, k)

    def test_error_k_greater_than_len_arr(self):
        # k is greater than len(arr) (violates k <= len(arr)).
        arr = [1, 2, 3]
        k = 4
        with self.assertRaises(IndexError):
            add_elements(arr, k)

    def test_error_arr_non_integer(self):
        # arr contains non-integer elements.
        arr = [1, "a", 3]
        k = 2
        with self.assertRaises(TypeError):
            add_elements(arr, k)