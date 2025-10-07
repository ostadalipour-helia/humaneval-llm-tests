import unittest
from sut_llm.problem_HumanEval_105 import by_length

class TestByLength(unittest.TestCase):

    def test_empty_array(self):
        arr = []
        expected_output = []
        self.assertEqual(by_length(arr), expected_output)

    def test_docstring_example_1(self):
        arr = [2, 1, 1, 4, 5, 8, 2, 3]
        expected_output = ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
        self.assertEqual(by_length(arr), expected_output)

    def test_docstring_example_2_with_invalid_numbers(self):
        arr = [1, -1, 55]
        expected_output = ['One']
        self.assertEqual(by_length(arr), expected_output)

    def test_all_valid_unique_numbers_unsorted(self):
        arr = [9, 2, 7, 4, 1]
        expected_output = ["Nine", "Seven", "Four", "Two", "One"]
        self.assertEqual(by_length(arr), expected_output)

    def test_valid_numbers_with_duplicates(self):
        arr = [3, 3, 1, 5, 1, 3]
        expected_output = ["Five", "Three", "Three", "Three", "One", "One"]
        self.assertEqual(by_length(arr), expected_output)

    def test_numbers_outside_range_zero_and_ten(self):
        arr = [0, 10, 5, -2, 9]
        expected_output = ["Nine", "Five"]
        self.assertEqual(by_length(arr), expected_output)

    def test_single_valid_number(self):
        arr = [7]
        expected_output = ["Seven"]
        self.assertEqual(by_length(arr), expected_output)

    def test_single_invalid_number(self):
        arr = [100]
        expected_output = []
        self.assertEqual(by_length(arr), expected_output)

    def test_all_numbers_are_same_valid_number(self):
        arr = [6, 6, 6]
        expected_output = ["Six", "Six", "Six"]
        self.assertEqual(by_length(arr), expected_output)

    def test_mixed_valid_invalid_and_edge_range_numbers(self):
        arr = [9, 0, 1, 10, 5, -3, 2, 8]
        expected_output = ["Nine", "Eight", "Five", "Two", "One"]
        self.assertEqual(by_length(arr), expected_output)

if __name__ == '__main__':
    unittest.main()