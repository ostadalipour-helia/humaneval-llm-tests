import unittest
from sut.problem_HumanEval_26 import remove_duplicates

class Test_remove_duplicates(unittest.TestCase):
    def test_normal_mixed_unique_and_duplicate(self):
        # Example from docstring: mixed unique and duplicate elements.
        numbers = [1, 2, 3, 2, 4]
        expected_output = [1, 3, 4]
        self.assertEqual(remove_duplicates(numbers), expected_output)

    def test_normal_all_unique(self):
        # All elements are unique, so all should be kept.
        numbers = [5, 6, 7, 8]
        expected_output = [5, 6, 7, 8]
        self.assertEqual(remove_duplicates(numbers), expected_output)

    def test_normal_multiple_duplicates(self):
        # Multiple elements appear more than once, some appear once.
        numbers = [10, 20, 10, 30, 20, 40]
        expected_output = [30, 40]
        self.assertEqual(remove_duplicates(numbers), expected_output)

    def test_edge_empty_list(self):
        # Empty input list.
        numbers = []
        expected_output = []
        self.assertEqual(remove_duplicates(numbers), expected_output)

    def test_edge_all_duplicates(self):
        # All elements are duplicates, so the output should be an empty list.
        numbers = [1, 1, 1, 1]
        expected_output = []
        self.assertEqual(remove_duplicates(numbers), expected_output)

    def test_edge_single_unique_element(self):
        # List with a single unique element.
        numbers = [7]
        expected_output = [7]
        self.assertEqual(remove_duplicates(numbers), expected_output)

    def test_edge_negative_numbers_and_zero(self):
        # List containing negative numbers and zero.
        numbers = [-1, 0, -1, 2]
        expected_output = [0, 2]
        self.assertEqual(remove_duplicates(numbers), expected_output)

    def test_error_input_not_list(self):
        # Input is not a list.
        numbers = "not_a_list"
        with self.assertRaises(TypeError):
            remove_duplicates(numbers)

    def test_error_list_contains_non_integers(self):
        # Input list contains non-integer elements.
        numbers = [1, 2, "three", 4]
        with self.assertRaises(TypeError):
            remove_duplicates(numbers)