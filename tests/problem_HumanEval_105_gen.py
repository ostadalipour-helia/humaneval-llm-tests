import unittest
from sut.problem_HumanEval_105 import by_length

class TestByLength(unittest.TestCase):

    def test_example_from_docstring_1(self):
        # Typical input with duplicates and mixed order, covering multiple steps
        arr = [2, 1, 1, 4, 5, 8, 2, 3]
        expected = ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
        self.assertListEqual(by_length(arr), expected)

    def test_example_from_docstring_2_mixed_invalid(self):
        # Input with valid, negative, and large invalid numbers.
        # Tests filtering logic and handling of non-relevant numbers.
        arr = [1, -1, 55]
        expected = ['One']
        self.assertListEqual(by_length(arr), expected)

    def test_empty_array(self):
        # Edge case: empty input array.
        arr = []
        expected = []
        self.assertListEqual(by_length(arr), expected)

    def test_single_valid_element(self):
        # Edge case: single valid element.
        arr = [5]
        expected = ['Five']
        self.assertListEqual(by_length(arr), expected)

    def test_single_invalid_element_below_boundary(self):
        # Boundary test: single element just below the valid range (0).
        # Catches off-by-one errors like '<=' instead of '<' for lower bound.
        arr = [0]
        expected = []
        self.assertListEqual(by_length(arr), expected)

    def test_single_invalid_element_above_boundary(self):
        # Boundary test: single element just above the valid range (10).
        # Catches off-by-one errors like '>=' instead of '>' for upper bound.
        arr = [10]
        expected = []
        self.assertListEqual(by_length(arr), expected)

    def test_all_valid_boundary_values(self):
        # Boundary test: array containing only the exact boundary values (1 and 9).
        arr = [1, 9]
        expected = ['Nine', 'One']
        self.assertListEqual(by_length(arr), expected)

    def test_all_invalid_values_mixed(self):
        # Extreme input: array with only invalid numbers, including negative, zero, and large.
        # Tests robust filtering and ensures an empty list is returned.
        arr = [0, -5, 10, 100, -100]
        expected = []
        self.assertListEqual(by_length(arr), expected)

    def test_duplicates_and_boundary_values(self):
        # Input with duplicates and boundary values, testing sorting and mapping.
        arr = [1, 1, 9, 9, 5, 2]
        expected = ['Nine', 'Nine', 'Five', 'Two', 'One', 'One']
        self.assertListEqual(by_length(arr), expected)

    def test_sorted_input_all_valid(self):
        # Typical input that is already sorted, primarily testing the reverse and mapping steps.
        arr = [3, 4, 5]
        expected = ['Five', 'Four', 'Three']
        self.assertListEqual(by_length(arr), expected)