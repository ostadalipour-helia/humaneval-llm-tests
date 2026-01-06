import unittest
from sut.problem_HumanEval_122 import add_elements

class Test_add_elements(unittest.TestCase):

    def test_docstring_example(self):
        arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9]
        k = 4
        self.assertEqual(add_elements(arr, k), 24)

    def test_all_first_k_valid(self):
        arr = [1, 2, 3, 100, 5]
        k = 3
        self.assertEqual(add_elements(arr, k), 6)

    def test_none_first_k_valid(self):
        arr = [1000, 200, 300, 400, 500]
        k = 5
        self.assertEqual(add_elements(arr, k), 0)

    def test_with_negative_numbers(self):
        arr = [10, -20, 30, 100, 50]
        k = 4
        self.assertEqual(add_elements(arr, k), 40)

    def test_k_is_one(self):
        arr = [5, 100, 200]
        k = 1
        self.assertEqual(add_elements(arr, k), 5)

    def test_k_equals_len_arr(self):
        arr = [10, 20, 30]
        k = 3
        self.assertEqual(add_elements(arr, k), 60)

    def test_with_zero(self):
        arr = [0, 10, 100]
        k = 2
        self.assertEqual(add_elements(arr, k), 10)

    def test_boundary_values(self):
        arr = [99, -99, 100, -100]
        k = 4
        self.assertEqual(add_elements(arr, k), 99)

    def test_min_length_array(self):
        arr = [1]
        k = 1
        self.assertEqual(add_elements(arr, k), 1)

    def test_max_length_array(self):
        arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
        k = 100
        self.assertEqual(add_elements(arr, k), 4636)