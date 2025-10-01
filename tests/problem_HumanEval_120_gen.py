import unittest
from sut.problem_HumanEval_120 import maximum

class TestMaximum(unittest.TestCase):

    def test_example_1(self):
        arr = [-3, -4, 5]
        k = 3
        expected_output = [-4, -3, 5]
        self.assertEqual(maximum(arr, k), expected_output)

    def test_example_2(self):
        arr = [4, -4, 4]
        k = 2
        expected_output = [4, 4]
        self.assertEqual(maximum(arr, k), expected_output)

    def test_example_3(self):
        arr = [-3, 2, 1, 2, -1, -2, 1]
        k = 1
        expected_output = [2]
        self.assertEqual(maximum(arr, k), expected_output)

    def test_k_is_zero(self):
        arr = [1, 2, 3, 4, 5]
        k = 0
        expected_output = []
        self.assertEqual(maximum(arr, k), expected_output)

    def test_all_negative_numbers(self):
        arr = [-10, -5, -1, -20, -15]
        k = 3
        expected_output = [-15, -10, -5]
        self.assertEqual(maximum(arr, k), expected_output)

    def test_all_positive_numbers(self):
        arr = [1, 5, 10, 2, 8]
        k = 4
        expected_output = [2, 5, 8, 10]
        self.assertEqual(maximum(arr, k), expected_output)

    def test_mixed_numbers_unsorted_input(self):
        arr = [10, -1, 5, 20, -5, 0]
        k = 3
        expected_output = [5, 10, 20]
        self.assertEqual(maximum(arr, k), expected_output)

    def test_single_element_array(self):
        arr = [42]
        k = 1
        expected_output = [42]
        self.assertEqual(maximum(arr, k), expected_output)

    def test_array_with_duplicates_selecting_duplicates(self):
        arr = [1, 5, 2, 5, 3, 5]
        k = 4
        expected_output = [3, 5, 5, 5]
        self.assertEqual(maximum(arr, k), expected_output)

    def test_larger_array_k_in_middle(self):
        arr = [100, 1, 50, 10, 200, 5, 75, 150]
        k = 5
        expected_output = [75, 100, 150, 200, 50] # Sorted: [50, 75, 100, 150, 200]
        self.assertEqual(maximum(arr, k), sorted([50, 75, 100, 150, 200]))

if __name__ == '__main__':
    unittest.main()