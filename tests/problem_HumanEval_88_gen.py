import unittest
from sut.problem_HumanEval_88 import sort_array

class TestSortArray(unittest.TestCase):

    def test_empty_array(self):
        """
        Test case for an empty input array.
        Edge Case: Empty collection.
        """
        arr = []
        expected = []
        self.assertListEqual(sort_array(arr), expected)

    def test_single_element_array(self):
        """
        Test case for an array with a single element.
        Edge Case: Single element collection.
        """
        arr = [5]
        expected = [5]
        self.assertListEqual(sort_array(arr), expected)

    def test_ascending_sort_example(self):
        """
        Test case for an array that should be sorted in ascending order.
        (First + Last) sum is odd. Typical/Expected input.
        Example from docstring.
        """
        arr = [2, 4, 3, 0, 1, 5] # first=2, last=5, sum=7 (odd)
        expected = [0, 1, 2, 3, 4, 5]
        self.assertListEqual(sort_array(arr), expected)

    def test_descending_sort_example(self):
        """
        Test case for an array that should be sorted in descending order.
        (First + Last) sum is even. Typical/Expected input.
        Example from docstring.
        """
        arr = [2, 4, 3, 0, 1, 5, 6] # first=2, last=6, sum=8 (even)
        expected = [6, 5, 4, 3, 2, 1, 0]
        self.assertListEqual(sort_array(arr), expected)

    def test_boundary_two_elements_sum_odd(self):
        """
        Test case for a two-element array where (First + Last) sum is odd.
        Boundary Test: Smallest non-trivial array, odd sum.
        """
        arr = [1, 0] # first=1, last=0, sum=1 (odd)
        expected = [0, 1]
        self.assertListEqual(sort_array(arr), expected)

    def test_boundary_two_elements_sum_even(self):
        """
        Test case for a two-element array where (First + Last) sum is even.
        Boundary Test: Smallest non-trivial array, even sum.
        """
        arr = [0, 2] # first=0, last=2, sum=2 (even)
        expected = [2, 0]
        self.assertListEqual(sort_array(arr), expected)

    def test_array_not_modified(self):
        """
        Test to ensure the original array is not modified.
        Critical Requirement: Immutability.
        """
        original_arr = [2, 4, 3, 0, 1, 5]
        arr_copy = list(original_arr) # Create a copy to pass
        sort_array(arr_copy)
        self.assertListEqual(original_arr, [2, 4, 3, 0, 1, 5]) # Assert original remains unchanged

    def test_all_same_elements_sum_even(self):
        """
        Test case with all identical elements, resulting in an even sum.
        Edge Case: All same values.
        """
        arr = [7, 7, 7, 7] # first=7, last=7, sum=14 (even)
        expected = [7, 7, 7, 7] # Should be descending, but already sorted
        self.assertListEqual(sort_array(arr), expected)

    def test_duplicates_and_zeros_sum_odd(self):
        """
        Test case with duplicate values and zeros, where (First + Last) sum is odd.
        Extreme/Unusual Input: Duplicates, zeros, longer array.
        """
        arr = [0, 3, 1, 4, 1, 5, 9, 2, 7] # first=0, last=7, sum=7 (odd)
        expected = [0, 1, 1, 2, 3, 4, 5, 7, 9]
        self.assertListEqual(sort_array(arr), expected)

    def test_large_numbers_sum_even_unsorted(self):
        """
        Test case with large numbers and an even sum, requiring descending sort.
        Extreme/Unusual Input: Large numbers, unsorted.
        """
        arr = [100000, 500, 20000, 10] # first=100000, last=10, sum=100010 (even)
        expected = [100000, 20000, 500, 10]
        self.assertListEqual(sort_array(arr), expected)