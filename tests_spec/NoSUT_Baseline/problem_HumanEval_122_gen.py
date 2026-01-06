import unittest
import sut.problem_HumanEval_122 as mod

class TestHybrid(unittest.TestCase):
    def test_example_from_docstring(self):
            # Typical case, includes elements >2 digits and elements outside k
            arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9]
            k = 4
            self.assertEqual(mod.add_elements(arr, k), 24) # 21 + 3

    def test_k_is_one_boundary(self):
            # Boundary condition: k is the minimum possible value (1)
            arr = [12, 123, 4, 5]
            k = 1
            self.assertEqual(mod.add_elements(arr, k), 12)

    def test_k_is_len_arr_boundary(self):
            # Boundary condition: k is the maximum possible value (len(arr))
            arr = [1, 20, 300, 40]
            k = 4
            self.assertEqual(mod.add_elements(arr, k), 61) # 1 + 20 + 40

    def test_all_elements_within_k_and_two_digits(self):
            # Edge case: All elements considered within k satisfy the digit condition
            arr = [1, 2, 3, 4, 5]
            k = 3
            self.assertEqual(mod.add_elements(arr, k), 6) # 1 + 2 + 3

    def test_no_elements_within_k_satisfy_two_digits(self):
            # Edge case: No elements within the first k have at most two digits
            arr = [100, 200, 300, 400, 500]
            k = 3
            self.assertEqual(mod.add_elements(arr, k), 0)

    def test_k_just_before_large_number_off_by_one(self):
            # Boundary/Off-by-one: k ends right before an element that would be excluded by digit count
            arr = [10, 20, 100, 30, 40]
            k = 2
            self.assertEqual(mod.add_elements(arr, k), 30) # 10 + 20

    def test_large_array_and_k_with_mixed_elements(self):
            # Extreme input: Large array, large k, many elements to process
            arr = [1] * 50 + [100] * 50 + [2] * 50
            k = 75 # First 50 '1's, then 25 '100's
            self.assertEqual(mod.add_elements(arr, k), 50) # Sum of first 50 '1's

    def test_single_element_array_k_is_one(self):
            # Edge case: Smallest possible valid input (single element array, k=1)
            arr = [42]
            k = 1
            self.assertEqual(mod.add_elements(arr, k), 42)

    def test_normal_example_docstring(self):
            # Example from docstring: sum of 21 and 3 from the first 4 elements.
            arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9]
            k = 4
            arr_copy = list(arr) # For invariant check
            result = mod.add_elements(arr, k)
            self.assertEqual(result, 24)
            self.assertEqual(arr, arr_copy) # Invariant check

    def test_normal_none_first_k_valid(self):
            # None of the first k elements have at most two digits.
            arr = [1000, 200, 300, 400, 500]
            k = 5
            arr_copy = list(arr)
            result = mod.add_elements(arr, k)
            self.assertEqual(result, 0)
            self.assertEqual(arr, arr_copy)

    def test_edge_k_is_one(self):
            # k is 1, only the first element is considered.
            arr = [5, 100, 200]
            k = 1
            arr_copy = list(arr)
            result = mod.add_elements(arr, k)
            self.assertEqual(result, 5)
            self.assertEqual(arr, arr_copy)

    def test_edge_k_equals_len_arr(self):
            # k is equal to len(arr), all elements are considered.
            arr = [10, 20, 30]
            k = 3
            arr_copy = list(arr)
            result = mod.add_elements(arr, k)
            self.assertEqual(result, 60) # 10 + 20 + 30 = 60
            self.assertEqual(arr, arr_copy)

    def test_edge_contains_zero(self):
            # Array contains zero, which has at most two digits.
            arr = [0, 10, 100]
            k = 2
            arr_copy = list(arr)
            result = mod.add_elements(arr, k)
            self.assertEqual(result, 10) # 0 + 10 = 10
            self.assertEqual(arr, arr_copy)

    def test_error_arr_non_integer(self):
            # arr contains non-integer elements.
            arr = [1, "a", 3]
            k = 2
            with self.assertRaises(TypeError):
                mod.add_elements(arr, k)

