import unittest
from sut.problem_HumanEval_35 import max_element

class TestMaxElement(unittest.TestCase):

    def test_basic_positive_list(self):
        """
        Test with a simple list of positive integers, max at the end.
        Covers typical input and verifies exact output.
        """
        self.assertEqual(max_element([1, 2, 3]), 3)

    def test_mixed_numbers_list(self):
        """
        Test with a list containing positive, negative, and zero values,
        including a large positive number. Covers typical/extreme input.
        """
        self.assertEqual(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), 123)

    def test_single_element_list(self):
        """
        Test with a list containing only one element.
        Covers an edge case and potential off-by-one errors in loop initialization.
        """
        self.assertEqual(max_element([7]), 7)

    def test_empty_list(self):
        """
        Test with an empty list.
        This is a critical edge case. Assuming standard Python `max()` behavior,
        it should raise a ValueError.
        """
        with self.assertRaises(ValueError):
            max_element([])

    def test_all_negative_numbers(self):
        """
        Test with a list containing only negative numbers.
        Covers sign testing and ensures correct comparison with negative values.
        """
        self.assertEqual(max_element([-1, -5, -10, -2]), -1)

    def test_max_at_start(self):
        """
        Test with the maximum element located at the beginning of the list.
        Covers a boundary condition and potential off-by-one errors in loop logic.
        """
        self.assertEqual(max_element([10, 1, 2, 3]), 10)

    def test_max_at_end(self):
        """
        Test with the maximum element located at the end of the list.
        Covers a boundary condition and potential off-by-one errors in loop termination.
        """
        self.assertEqual(max_element([1, 2, 3, 10]), 10)

    def test_max_in_middle(self):
        """
        Test with the maximum element located in the middle of the list.
        Covers a typical scenario and ensures correct iteration.
        """
        self.assertEqual(max_element([1, 5, 10, 2, 3]), 10)

    def test_list_with_duplicates_and_max(self):
        """
        Test with a list containing duplicate values, including the maximum element.
        Covers an edge case with duplicates and ensures the correct max is returned.
        """
        self.assertEqual(max_element([1, 5, 2, 5, 10, 10]), 10)

    def test_list_with_zero_and_mixed_signs(self):
        """
        Test with a list containing zero, positive, and negative numbers.
        Covers sign testing and ensures zero is handled correctly in comparisons.
        """
        self.assertEqual(max_element([-5, 0, 5, -1]), 5)