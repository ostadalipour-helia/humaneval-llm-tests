import unittest
from sut.problem_HumanEval_37 import sort_even

class Test_sort_even(unittest.TestCase):

    def test_normal_already_sorted(self):
        # Description: List where even-indexed elements are already sorted.
        l = [1, 2, 3]
        expected_output = [1, 2, 3]
        self.assertEqual(sort_even(l), expected_output)

    def test_normal_unsorted_even(self):
        # Description: List with unsorted even-indexed elements.
        l = [5, 6, 3, 4]
        expected_output = [3, 6, 5, 4]
        self.assertEqual(sort_even(l), expected_output)

    def test_normal_longer_list(self):
        # Description: A longer list with mixed sorted/unsorted even-indexed elements.
        l = [10, 1, 8, 3, 6, 5]
        expected_output = [6, 1, 8, 3, 10, 5]
        self.assertEqual(sort_even(l), expected_output)

    def test_edge_empty_list(self):
        # Description: Empty list.
        l = []
        expected_output = []
        self.assertEqual(sort_even(l), expected_output)

    def test_edge_single_element(self):
        # Description: List with a single element (at an even index).
        l = [1]
        expected_output = [1]
        self.assertEqual(sort_even(l), expected_output)

    def test_edge_two_elements_sorted(self):
        # Description: List with two elements, even-indexed element is already sorted.
        l = [2, 1]
        expected_output = [2, 1]
        self.assertEqual(sort_even(l), expected_output)

    def test_edge_unsorted_with_duplicates_negatives(self):
        # Description: List with unsorted even-indexed elements, including duplicates or negative numbers.
        l = [5, 2, 3, 4, 1]
        expected_output = [1, 2, 3, 4, 5]
        self.assertEqual(sort_even(l), expected_output)

    def test_edge_negatives_and_zero(self):
        # Description: List with negative numbers and zero.
        l = [0, -1, 10, -5, 5]
        expected_output = [0, -1, 5, -5, 10]
        self.assertEqual(sort_even(l), expected_output)

    def test_error_none_input(self):
        # Description: Input is not a list.
        with self.assertRaises(TypeError):
            sort_even(None)

    def test_error_mixed_types_even(self):
        # Description: Even-indexed elements are not sortable (mixed types).
        with self.assertRaises(TypeError):
            sort_even([1, 'a', 3])

    def test_error_uncomparable_objects(self):
        # Description: Even-indexed elements are unhashable/uncomparable objects.
        with self.assertRaises(TypeError):
            sort_even([{'key': 1}, 2, {'key': 0}])