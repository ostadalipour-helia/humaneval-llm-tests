import unittest
from sut.problem_HumanEval_34 import unique

class TestUnique(unittest.TestCase):

    def test_01_docstring_example(self):
        # Test with the example provided in the docstring
        self.assertListEqual(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]), [0, 2, 3, 5, 9, 123])

    def test_02_empty_list(self):
        # Edge case: Test with an empty list
        self.assertListEqual(unique([]), [])

    def test_03_single_element_list(self):
        # Edge case: Test with a list containing a single element
        self.assertListEqual(unique([7]), [7])

    def test_04_all_identical_elements(self):
        # Edge case: Test with a list where all elements are identical
        self.assertListEqual(unique([4, 4, 4, 4]), [4])

    def test_05_already_sorted_no_duplicates(self):
        # Boundary condition: Test with an already sorted list with no duplicates
        self.assertListEqual(unique([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_06_reverse_sorted_no_duplicates(self):
        # Boundary condition: Test with a reverse sorted list with no duplicates
        self.assertListEqual(unique([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_07_mixed_positive_negative_zero_duplicates(self):
        # Typical input: Test with a mix of positive, negative, and zero values, with duplicates
        self.assertListEqual(unique([-3, 0, 5, -3, 2, 0, 1]), [-3, 0, 1, 2, 5])

    def test_08_large_numbers_and_many_duplicates(self):
        # Extreme input: Test with larger numbers and multiple duplicates
        self.assertListEqual(unique([1000, 500, 1000, 200, 500, 1000, 100]), [100, 200, 500, 1000])

    def test_09_all_negative_numbers_duplicates(self):
        # Boundary condition: Test with only negative numbers and duplicates
        self.assertListEqual(unique([-5, -1, -5, -3, -1, -2]), [-5, -3, -2, -1])

    def test_10_two_elements_one_duplicate(self):
        # Off-by-one error check: Test with a small list containing two identical elements
        self.assertListEqual(unique([2, 2]), [2])