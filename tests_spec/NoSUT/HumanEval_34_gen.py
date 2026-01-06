import unittest
from sut.problem_HumanEval_34 import unique

class Test_unique(unittest.TestCase):

    def test_normal_duplicates_unsorted(self):
        # A list with multiple duplicate elements and unsorted order.
        input_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
        expected_output = [0, 2, 3, 5, 9, 123]
        self.assertEqual(unique(input_list), expected_output)

    def test_normal_no_duplicates_sorted(self):
        # A list with no duplicate elements, already sorted.
        input_list = [1, 2, 3, 4]
        expected_output = [1, 2, 3, 4]
        self.assertEqual(unique(input_list), expected_output)

    def test_normal_negative_zero_positive(self):
        # A list with negative numbers, zero, and positive numbers, with duplicates.
        input_list = [10, -5, 0, 7, -5]
        expected_output = [-5, 0, 7, 10]
        self.assertEqual(unique(input_list), expected_output)

    def test_edge_empty_list(self):
        # An empty list.
        input_list = []
        expected_output = []
        self.assertEqual(unique(input_list), expected_output)

    def test_edge_single_element(self):
        # A list with a single element.
        input_list = [7]
        expected_output = [7]
        self.assertEqual(unique(input_list), expected_output)

    def test_edge_all_identical_elements(self):
        # A list with all identical elements.
        input_list = [4, 4, 4, 4]
        expected_output = [4]
        self.assertEqual(unique(input_list), expected_output)

    def test_edge_strings_with_duplicates(self):
        # A list of strings with duplicates.
        input_list = ["b", "a", "c", "b"]
        expected_output = ["a", "b", "c"]
        self.assertEqual(unique(input_list), expected_output)

    def test_error_input_none(self):
        # Input is not a list (e.g., None).
        with self.assertRaises(TypeError):
            unique(None)

    def test_error_input_integer(self):
        # Input is not a list (e.g., an integer).
        with self.assertRaises(TypeError):
            unique(123)

    def test_error_input_string(self):
        # Input is not a list (e.g., a string).
        with self.assertRaises(TypeError):
            unique("hello")

    def test_error_non_comparable_elements(self):
        # Input list contains non-comparable elements, leading to a TypeError during sorting.
        with self.assertRaises(TypeError):
            unique([1, "a", {}])