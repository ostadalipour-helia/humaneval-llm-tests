import unittest
from sut.problem_HumanEval_58 import common

class TestCommon(unittest.TestCase):

    def test_docstring_example_1(self):
        # Typical case with duplicates in input lists, verifies uniqueness and sorting
        l1 = [1, 4, 3, 34, 653, 2, 5]
        l2 = [5, 7, 1, 5, 9, 653, 121]
        expected = [1, 5, 653]
        self.assertListEqual(common(l1, l2), expected)

    def test_docstring_example_2(self):
        # Typical case where one list is a subset of the other, verifies sorting
        l1 = [5, 3, 2, 8]
        l2 = [3, 2]
        expected = [2, 3]
        self.assertListEqual(common(l1, l2), expected)

    def test_empty_lists(self):
        # Edge case: both lists are empty
        l1 = []
        l2 = []
        expected = []
        self.assertListEqual(common(l1, l2), expected)

    def test_one_empty_list(self):
        # Edge case: one list is empty, the other is not
        l1 = [1, 2, 3]
        l2 = []
        expected = []
        self.assertListEqual(common(l1, l2), expected)

    def test_no_common_elements(self):
        # Boundary case: lists have no elements in common
        # Catches logic mutations like 'and' becoming 'or'
        l1 = [1, 2, 3]
        l2 = [4, 5, 6]
        expected = []
        self.assertListEqual(common(l1, l2), expected)

    def test_all_common_elements(self):
        # Boundary case: all elements are common and in order
        l1 = [1, 2, 3]
        l2 = [1, 2, 3]
        expected = [1, 2, 3]
        self.assertListEqual(common(l1, l2), expected)

    def test_negative_numbers_and_zero(self):
        # Extreme case: includes negative numbers and zero, verifies sorting
        l1 = [-1, 0, 5, -3]
        l2 = [0, -3, 7, 5]
        expected = [-3, 0, 5]
        self.assertListEqual(common(l1, l2), expected)

    def test_duplicates_in_both_lists_complex_order(self):
        # Edge case: multiple duplicates in both lists, verifies uniqueness and sorting
        l1 = [10, 20, 10, 30, 20]
        l2 = [20, 10, 40, 10, 50]
        expected = [10, 20]
        self.assertListEqual(common(l1, l2), expected)

    def test_single_common_element_large_numbers(self):
        # Boundary/Extreme case: single common element with large numbers
        l1 = [1000000, 2, 3]
        l2 = [4, 1000000, 5]
        expected = [1000000]
        self.assertListEqual(common(l1, l2), expected)

    def test_lists_with_different_lengths_some_common(self):
        # Typical case: lists of different lengths with several common elements
        l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        l2 = [2, 4, 6, 8, 10]
        expected = [2, 4, 6, 8, 10]
        self.assertListEqual(common(l1, l2), expected)