import unittest
from sut_llm.problem_HumanEval_122 import add_elements

class TestAddElements(unittest.TestCase):

    def test_example_from_docstring(self):
        arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9]
        k = 4
        self.assertEqual(add_elements(arr, k), 24)

    def test_all_valid_elements_within_k(self):
        arr = [10, 20, 30, 40, 50]
        k = 4
        self.assertEqual(add_elements(arr, k), 100)

    def test_mixed_valid_and_invalid_elements_within_k(self):
        arr = [1, 100, 2, 200, 3, 300]
        k = 6
        self.assertEqual(add_elements(arr, k), 6)

    def test_no_valid_elements_within_k(self):
        arr = [1000, 2000, 3000, 4000]
        k = 4
        self.assertEqual(add_elements(arr, k), 0)

    def test_k_is_one_with_valid_element(self):
        arr = [50, 100, 200]
        k = 1
        self.assertEqual(add_elements(arr, k), 50)

    def test_k_is_one_with_invalid_element(self):
        arr = [500, 10, 20]
        k = 1
        self.assertEqual(add_elements(arr, k), 0)

    def test_negative_two_digit_numbers(self):
        arr = [-10, -20, 5, 100, -50]
        k = 4
        self.assertEqual(add_elements(arr, k), -25) # -10 + -20 + 5

    def test_mixed_positive_negative_and_zero_two_digit_numbers(self):
        arr = [99, -99, 0, 100, -1]
        k = 5
        self.assertEqual(add_elements(arr, k), -1) # 99 + -99 + 0 + -1

    def test_only_one_valid_element_within_k(self):
        arr = [1000, 2000, 30, 4000, 5000]
        k = 5
        self.assertEqual(add_elements(arr, k), 30)

    def test_valid_elements_outside_k_range_are_ignored(self):
        arr = [10, 100, 20, 200, 30, 300]
        k = 3
        self.assertEqual(add_elements(arr, k), 30) # 10 + 20

if __name__ == '__main__':
    unittest.main()