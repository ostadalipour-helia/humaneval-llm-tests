import unittest
from sut.problem_HumanEval_9 import rolling_max

class TestRollingMax(unittest.TestCase):

    def test_docstring_example(self):
        # Test case directly from the docstring example
        self.assertListEqual(rolling_max([1, 2, 3, 2, 3, 4, 2]), [1, 2, 3, 3, 3, 4, 4])

    def test_empty_list(self):
        # Edge case: empty input list
        self.assertListEqual(rolling_max([]), [])

    def test_single_element_list(self):
        # Edge case: list with a single element
        self.assertListEqual(rolling_max([5]), [5])

    def test_all_increasing_numbers(self):
        # Boundary test: numbers are strictly increasing
        self.assertListEqual(rolling_max([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_all_decreasing_numbers(self):
        # Boundary test: numbers are strictly decreasing, max should stay the same
        self.assertListEqual(rolling_max([5, 4, 3, 2, 1]), [5, 5, 5, 5, 5])

    def test_mixed_positive_negative_zero(self):
        # Extreme input: mixed positive, negative, and zero values
        self.assertListEqual(rolling_max([0, -5, 10, -2, 0, 15]), [0, 0, 10, 10, 10, 15])

    def test_all_negative_numbers(self):
        # Extreme input: all negative numbers
        self.assertListEqual(rolling_max([-10, -5, -12, -3, -8]), [-10, -5, -5, -3, -3])

    def test_max_stays_same_then_changes(self):
        # Boundary test: current number equals current max, then drops, then increases
        self.assertListEqual(rolling_max([7, 7, 5, 7, 6, 8]), [7, 7, 7, 7, 7, 8])

    def test_duplicates_and_zeros(self):
        # Edge case: list with duplicate values and zeros
        self.assertListEqual(rolling_max([0, 0, 5, 5, 0, 10]), [0, 0, 5, 5, 5, 10])

    def test_long_list_with_fluctuations(self):
        # Typical input: a longer list with various increases and decreases
        self.assertListEqual(rolling_max([10, 2, 15, 5, 20, 1, 18, 25, 3]), [10, 10, 15, 15, 20, 20, 20, 25, 25])