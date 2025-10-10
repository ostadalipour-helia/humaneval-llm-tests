import unittest
from sut.problem_HumanEval_5 import intersperse

class TestIntersperse(unittest.TestCase):

    def test_empty_list(self):
        """
        Test case: Empty input list.
        Boundary condition: Smallest possible list.
        Expected: An empty list.
        """
        self.assertListEqual(intersperse([], 4), [])

    def test_single_element_list(self):
        """
        Test case: Single element input list.
        Boundary condition: List with one element.
        Expected: The original list, as no elements to intersperse between.
        """
        self.assertListEqual(intersperse([1], 4), [1])

    def test_two_elements_list(self):
        """
        Test case: Two element input list.
        Boundary condition: Smallest list where intersperse should add one delimiter.
        Expected: List with one delimiter inserted.
        """
        self.assertListEqual(intersperse([1, 2], 4), [1, 4, 2])

    def test_typical_three_elements(self):
        """
        Test case: Typical three element input list.
        Expected: List with two delimiters inserted. (From docstring)
        """
        self.assertListEqual(intersperse([1, 2, 3], 4), [1, 4, 2, 4, 3])

    def test_longer_list_positive_delimiter(self):
        """
        Test case: A longer list with a positive delimiter.
        Typical/Extreme input: Verifies correct behavior for more elements.
        """
        self.assertListEqual(intersperse([10, 20, 30, 40, 50], 5), [10, 5, 20, 5, 30, 5, 40, 5, 50])

    def test_list_with_zero_delimiter(self):
        """
        Test case: Input list with a zero as the delimiter.
        Sign/Zero testing: Checks handling of zero delimiter.
        """
        self.assertListEqual(intersperse([1, 2, 3], 0), [1, 0, 2, 0, 3])

    def test_list_with_negative_delimiter(self):
        """
        Test case: Input list with a negative delimiter.
        Sign/Zero testing: Checks handling of negative delimiter.
        """
        self.assertListEqual(intersperse([1, 2, 3], -5), [1, -5, 2, -5, 3])

    def test_list_with_negative_numbers(self):
        """
        Test case: Input list containing negative numbers.
        Sign/Zero testing: Checks handling of negative numbers in the input list.
        """
        self.assertListEqual(intersperse([-1, -2, -3], 4), [-1, 4, -2, 4, -3])

    def test_list_with_zero_and_duplicates(self):
        """
        Test case: Input list containing zeros and duplicate numbers.
        Edge case: Checks handling of non-unique and zero values in the list.
        """
        self.assertListEqual(intersperse([0, 0, 5, 5], 1), [0, 1, 0, 1, 5, 1, 5])

    def test_list_all_same_values(self):
        """
        Test case: Input list where all elements are the same.
        Edge case: Ensures logic doesn't depend on unique values.
        """
        self.assertListEqual(intersperse([7, 7, 7, 7], 9), [7, 9, 7, 9, 7, 9, 7])