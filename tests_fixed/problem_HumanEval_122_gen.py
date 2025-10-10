import unittest
from sut_llm.problem_HumanEval_122 import add_elements

class TestAddElements(unittest.TestCase):

    def test_example_from_docstring(self):
        # Typical case, includes elements >2 digits and elements outside k
        arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9]
        k = 4
        self.assertEqual(add_elements(arr, k), 24) # 21 + 3

    def test_k_is_one_boundary(self):
        # Boundary condition: k is the minimum possible value (1)
        arr = [12, 123, 4, 5]
        k = 1
        self.assertEqual(add_elements(arr, k), 12)

    def test_k_is_len_arr_boundary(self):
        # Boundary condition: k is the maximum possible value (len(arr))
        arr = [1, 20, 300, 40]
        k = 4
        self.assertEqual(add_elements(arr, k), 61) # 1 + 20 + 40

    def test_all_elements_within_k_and_two_digits(self):
        # Edge case: All elements considered within k satisfy the digit condition
        arr = [1, 2, 3, 4, 5]
        k = 3
        self.assertEqual(add_elements(arr, k), 6) # 1 + 2 + 3

    def test_no_elements_within_k_satisfy_two_digits(self):
        # Edge case: No elements within the first k have at most two digits
        arr = [100, 200, 300, 400, 500]
        k = 3
        self.assertEqual(add_elements(arr, k), 0)

    def test_k_just_before_large_number_off_by_one(self):
        # Boundary/Off-by-one: k ends right before an element that would be excluded by digit count
        arr = [10, 20, 100, 30, 40]
        k = 2
        self.assertEqual(add_elements(arr, k), 30) # 10 + 20

    def test_sign_and_zero_with_two_digit_boundary(self):
        # Sign and Zero Testing: Includes negative numbers, zero, and numbers at the two-digit boundary
        arr = [-10, 0, 99, -100, 5, 101]
        k = 5
        self.assertEqual(add_elements(arr, k), 94) # -10 + 0 + 99 + 5 (100 and -100 are excluded)

    def test_digit_count_exact_boundary_mutation_catch(self):
        # Logic Mutation: Tests numbers exactly at the 2-digit boundary (99, 100, -99, -100)
        arr = [99, 100, -99, -100, 1, 2]
        k = 6
        self.assertEqual(add_elements(arr, k), 3) # 99 + (-99) + 1 + 2 (100 and -100 are excluded)

    def test_large_array_and_k_with_mixed_elements(self):
        # Extreme input: Large array, large k, many elements to process
        arr = [1] * 50 + [100] * 50 + [2] * 50
        k = 75 # First 50 '1's, then 25 '100's
        self.assertEqual(add_elements(arr, k), 50) # Sum of first 50 '1's

    def test_single_element_array_k_is_one(self):
        # Edge case: Smallest possible valid input (single element array, k=1)
        arr = [42]
        k = 1
        self.assertEqual(add_elements(arr, k), 42)