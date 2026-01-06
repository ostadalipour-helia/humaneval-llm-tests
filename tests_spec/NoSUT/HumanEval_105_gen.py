import unittest
from sut.problem_HumanEval_105 import by_length

class Test_by_length(unittest.TestCase):

    def test_normal_multiple_elements(self):
        arr = [2, 1, 1, 4, 5, 8, 2, 3]
        expected_output = ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
        self.assertEqual(by_length(arr), expected_output)

    def test_normal_distinct_elements(self):
        arr = [9, 7, 3, 6]
        expected_output = ["Nine", "Seven", "Six", "Three"]
        self.assertEqual(by_length(arr), expected_output)

    def test_normal_duplicate_valid_elements(self):
        arr = [5, 5, 5]
        expected_output = ["Five", "Five", "Five"]
        self.assertEqual(by_length(arr), expected_output)

    def test_edge_empty_input_list(self):
        arr = []
        expected_output = []
        self.assertEqual(by_length(arr), expected_output)

    def test_edge_mixed_valid_and_invalid_numbers(self):
        arr = [1, -1, 55]
        expected_output = ["One"]
        self.assertEqual(by_length(arr), expected_output)

    def test_edge_all_invalid_numbers(self):
        arr = [-10, 0, 10, 100]
        expected_output = []
        self.assertEqual(by_length(arr), expected_output)

    def test_edge_min_and_max_valid_range(self):
        arr = [1, 9]
        expected_output = ["Nine", "One"]
        self.assertEqual(by_length(arr), expected_output)

    def test_edge_single_valid_number(self):
        arr = [7]
        expected_output = ["Seven"]
        self.assertEqual(by_length(arr), expected_output)

    def test_error_non_list_input(self):
        arr = "not_a_list"
        with self.assertRaises(TypeError):
            by_length(arr)

    def test_error_list_with_non_integer_elements(self):
        arr = [1, 2.5, "three"]
        with self.assertRaises(TypeError): # Expecting TypeError if comparison or other int-specific ops fail
            by_length(arr)