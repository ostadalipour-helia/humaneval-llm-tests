import unittest
from sut.problem_HumanEval_33 import sort_third

class Test_sort_third(unittest.TestCase):
    def test_normal_case_basic_sort(self):
        # General case with multiple elements at indices divisible by three that need sorting.
        l = [5, 6, 3, 4, 8, 9, 2]
        expected = [2, 6, 3, 4, 8, 9, 5]
        self.assertEqual(sort_third(l), expected)

    def test_normal_case_longer_list(self):
        # Longer list with several elements at indices divisible by three, demonstrating sorting.
        l = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        expected = [0, 8, 7, 3, 5, 4, 6, 2, 1, 9]
        self.assertEqual(sort_third(l), expected)

    def test_normal_case_already_sorted(self):
        # List where elements at divisible-by-three indices are already sorted.
        l = [10, 20, 30, 40, 50, 60]
        expected = [10, 20, 30, 40, 50, 60]
        self.assertEqual(sort_third(l), expected)

    def test_edge_case_empty_list(self):
        # Empty list.
        l = []
        expected = []
        self.assertEqual(sort_third(l), expected)

    def test_edge_case_single_element(self):
        # List with a single element (at index 0, which is divisible by three).
        l = [10]
        expected = [10]
        self.assertEqual(sort_third(l), expected)

    def test_edge_case_reverse_sorted(self):
        # Elements at divisible-by-three indices are reverse sorted.
        l = [9, 2, 1, 3, 5, 4]
        expected = [3, 2, 1, 9, 5, 4]
        self.assertEqual(sort_third(l), expected)

    def test_edge_case_duplicates(self):
        # List with duplicate elements at indices divisible by three.
        l = [1, 2, 3, 1, 5, 6, 1]
        expected = [1, 2, 3, 1, 5, 6, 1]
        self.assertEqual(sort_third(l), expected)

    def test_edge_case_negative_numbers(self):
        # List containing negative numbers.
        l = [-1, 0, -3, -2, -5, -6]
        expected = [-2, 0, -3, -1, -5, -6]
        self.assertEqual(sort_third(l), expected)

    def test_error_case_none_input(self):
        # Input is not a list (None).
        with self.assertRaises(TypeError):
            sort_third(None)

    def test_error_case_non_list_int(self):
        # Input is an integer, not a list.
        with self.assertRaises(TypeError):
            sort_third(123)

    def test_error_case_uncomparable_types_at_divisible_indices_1(self):
        # List contains uncomparable types at indices divisible by three (e.g., int and str), leading to a sorting error.
        with self.assertRaises(TypeError):
            sort_third([1, 'a', 3])

    def test_error_case_uncomparable_types_at_divisible_indices_2(self):
        # List contains uncomparable types at indices divisible by three (e.g., int and str), leading to a sorting error.
        with self.assertRaises(TypeError):
            sort_third([1, 2, 3, 'b', 5, 6])