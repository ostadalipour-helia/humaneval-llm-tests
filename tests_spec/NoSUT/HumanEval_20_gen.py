import unittest
from sut.problem_HumanEval_20 import find_closest_elements

class Test_find_closest_elements(unittest.TestCase):

    def test_normal_distinct_closest(self):
        # "Typical case with distinct closest elements."
        numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2.2]
        expected_output = (2.0, 2.2)
        self.assertEqual(find_closest_elements(numbers), expected_output)

    def test_normal_non_adjacent_closest(self):
        # "Closest elements are not adjacent in the input list."
        numbers = [10.0, 1.0, 5.0, 8.0]
        expected_output = (8.0, 10.0)
        self.assertEqual(find_closest_elements(numbers), expected_output)

    def test_normal_closest_at_beginning(self):
        # "Closest elements are at the beginning of the list."
        numbers = [0.1, 0.2, 0.3, 0.4]
        expected_output = (0.1, 0.2)
        self.assertEqual(find_closest_elements(numbers), expected_output)

    def test_edge_identical_elements_multiple_times(self):
        # "Closest elements are identical and appear multiple times."
        numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2.0]
        expected_output = (2.0, 2.0)
        self.assertEqual(find_closest_elements(numbers), expected_output)

    def test_edge_two_elements_list(self):
        # "List with exactly two elements, requiring ordering."
        numbers = [5.0, 1.0]
        expected_output = (1.0, 5.0)
        self.assertEqual(find_closest_elements(numbers), expected_output)

    def test_edge_negative_numbers(self):
        # "List containing negative numbers."
        numbers = [-1.0, -2.0, -1.5]
        expected_output = (-1.5, -1.0)
        self.assertEqual(find_closest_elements(numbers), expected_output)

    def test_edge_high_precision_numbers(self):
        # "Numbers with high precision."
        numbers = [1.234567, 1.234568, 1.0]
        expected_output = (1.234567, 1.234568)
        self.assertEqual(find_closest_elements(numbers), expected_output)

    def test_error_empty_list(self):
        # "Input list has fewer than two elements (empty list)."
        numbers = []
        with self.assertRaises(ValueError):
            find_closest_elements(numbers)

    def test_error_single_element_list(self):
        # "Input list has fewer than two elements (single element list)."
        numbers = [1.0]
        with self.assertRaises(ValueError):
            find_closest_elements(numbers)

    def test_error_input_not_list(self):
        # "Input is not a list."
        numbers = None
        with self.assertRaises(TypeError):
            find_closest_elements(numbers)

    def test_error_list_contains_integers(self):
        # "Input list contains integers instead of floats (type mismatch)."
        numbers = [1, 2, 3]
        with self.assertRaises(TypeError):
            find_closest_elements(numbers)

    def test_error_list_contains_string(self):
        # "Input list contains non-float elements (string)."
        numbers = [1.0, '2.0', 3.0]
        with self.assertRaises(TypeError):
            find_closest_elements(numbers)