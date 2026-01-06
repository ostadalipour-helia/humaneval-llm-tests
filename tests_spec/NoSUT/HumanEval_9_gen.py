import unittest
from sut.problem_HumanEval_9 import rolling_max

class Test_rolling_max(unittest.TestCase):
    def test_normal_increasing_decreasing(self):
        numbers = [1, 2, 3, 2, 3, 4, 2]
        expected = [1, 2, 3, 3, 3, 4, 4]
        self.assertEqual(rolling_max(numbers), expected)

    def test_normal_mixed_pattern(self):
        numbers = [5, 1, 8, 2, 9]
        expected = [5, 5, 8, 8, 9]
        self.assertEqual(rolling_max(numbers), expected)

    def test_normal_strictly_decreasing(self):
        numbers = [10, 9, 8, 7, 6]
        expected = [10, 10, 10, 10, 10]
        self.assertEqual(rolling_max(numbers), expected)

    def test_normal_negative_and_zero(self):
        numbers = [-5, -1, -8, 0, -2]
        expected = [-5, -1, -1, 0, 0]
        self.assertEqual(rolling_max(numbers), expected)

    def test_edge_empty_list(self):
        numbers = []
        expected = []
        self.assertEqual(rolling_max(numbers), expected)

    def test_edge_single_element(self):
        numbers = [7]
        expected = [7]
        self.assertEqual(rolling_max(numbers), expected)

    def test_edge_all_identical_elements(self):
        numbers = [3, 3, 3, 3]
        expected = [3, 3, 3, 3]
        self.assertEqual(rolling_max(numbers), expected)

    def test_edge_all_zeros(self):
        numbers = [0, 0, 0]
        expected = [0, 0, 0]
        self.assertEqual(rolling_max(numbers), expected)

    def test_error_input_none(self):
        numbers = None
        with self.assertRaises(TypeError):
            rolling_max(numbers)

    def test_error_input_string(self):
        numbers = "not a list"
        with self.assertRaises(TypeError):
            rolling_max(numbers)

    def test_error_list_contains_string(self):
        numbers = [1, 2, "a", 4]
        with self.assertRaises(TypeError):
            rolling_max(numbers)

    def test_error_list_contains_float(self):
        numbers = [1, 2.5, 3]
        with self.assertRaises(TypeError):
            rolling_max(numbers)