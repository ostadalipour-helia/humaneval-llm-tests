import unittest
from sut_llm.problem_HumanEval_90 import next_smallest

class TestNextSmallest(unittest.TestCase):

    def test_docstring_example_sorted_list(self):
        # next_smallest([1, 2, 3, 4, 5]) == 2
        self.assertEqual(next_smallest([1, 2, 3, 4, 5]), 2)

    def test_docstring_example_unsorted_list(self):
        # next_smallest([5, 1, 4, 3, 2]) == 2
        self.assertEqual(next_smallest([5, 1, 4, 3, 2]), 2)

    def test_docstring_example_empty_list(self):
        # next_smallest([]) == None
        self.assertIsNone(next_smallest([]))

    def test_docstring_example_two_identical_elements(self):
        # next_smallest([1, 1]) == None
        self.assertIsNone(next_smallest([1, 1]))

    def test_single_element_list(self):
        # A list with only one element should return None
        self.assertIsNone(next_smallest([7]))

    def test_two_distinct_elements(self):
        # A list with two distinct elements, the second is the 2nd smallest
        self.assertEqual(next_smallest([10, 20]), 20)

    def test_list_with_negative_numbers(self):
        # Test with negative numbers
        self.assertEqual(next_smallest([-5, -1, -3, -2]), -3)

    def test_list_with_mixed_numbers_and_zero(self):
        # Test with mixed positive, negative, and zero
        self.assertEqual(next_smallest([-10, 0, 5, -5]), -5)

    def test_list_with_duplicates_and_clear_second_smallest(self):
        # Test with duplicates where the 2nd smallest is distinct
        self.assertEqual(next_smallest([1, 2, 2, 3, 4]), 2)

    def test_larger_unsorted_list_with_duplicates(self):
        # Test a larger unsorted list with some duplicates
        self.assertEqual(next_smallest([100, 10, 20, 10, 5, 50]), 10)