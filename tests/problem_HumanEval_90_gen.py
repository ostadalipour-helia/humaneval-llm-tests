import unittest
from sut.problem_HumanEval_90 import next_smallest

class TestNextSmallest(unittest.TestCase):

    def test_docstring_example_basic_sorted(self):
        # Test a typical case with a sorted list
        self.assertEqual(next_smallest([1, 2, 3, 4, 5]), 2)

    def test_docstring_example_basic_unsorted(self):
        # Test a typical case with an unsorted list
        self.assertEqual(next_smallest([5, 1, 4, 3, 2]), 2)

    def test_edge_empty_list(self):
        # Boundary test: empty list
        self.assertIsNone(next_smallest([]))

    def test_edge_single_element_list(self):
        # Boundary test: list with a single element
        self.assertIsNone(next_smallest([7]))

    def test_edge_all_same_elements(self):
        # Boundary test: list where all elements are identical
        self.assertIsNone(next_smallest([5, 5, 5, 5]))

    def test_boundary_two_distinct_elements(self):
        # Boundary test: the smallest possible list that should return a value
        self.assertEqual(next_smallest([10, 20]), 20)

    def test_negative_numbers(self):
        # Test with negative numbers, including unsorted order
        self.assertEqual(next_smallest([-5, -1, -4, -3, -2]), -4)

    def test_mixed_numbers_with_zero(self):
        # Test with a mix of positive, negative, and zero values
        self.assertEqual(next_smallest([-10, 0, 5, -2, 1]), -2)

    def test_duplicates_but_still_has_second_smallest(self):
        # Test with duplicates where the second smallest distinct element exists
        # This catches mutations that don't correctly handle distinctness.
        self.assertEqual(next_smallest([1, 1, 2, 3, 4]), 2)

    def test_large_numbers_and_unsorted(self):
        # Test with larger numbers and an unsorted list to ensure robustness
        self.assertEqual(next_smallest([1000, 50, 200, 10, 500]), 50)