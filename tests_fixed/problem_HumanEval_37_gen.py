import unittest
from sut_llm.problem_HumanEval_37 import sort_even

class TestSortEven(unittest.TestCase):

    def test_empty_list(self):
        """
        Test case for an empty input list.
        Ensures the function handles the smallest possible list correctly.
        (Edge Case: Empty collection)
        """
        self.assertListEqual(sort_even([]), [])

    def test_single_element_list(self):
        """
        Test case for a list with a single element.
        The single element is at an even index (0), so it should remain unchanged.
        (Edge Case: Single element collection, Boundary: first element)
        """
        self.assertListEqual(sort_even([5]), [5])

    def test_two_elements_list(self):
        """
        Test case for a list with two elements.
        Index 0 is even, index 1 is odd. Only index 0 can be sorted.
        (Boundary: Smallest list with both even/odd indices, Off-by-one: length 2)
        """
        self.assertListEqual(sort_even([2, 1]), [2, 1])

    def test_three_elements_list_docstring_example(self):
        """
        Test case matching the first docstring example.
        Even indices 0 and 2 are sorted.
        (Boundary: length 3, Typical Input)
        """
        self.assertListEqual(sort_even([1, 2, 3]), [1, 2, 3])

    def test_four_elements_list_docstring_example(self):
        """
        Test case matching the second docstring example.
        Even indices 0 and 2 are sorted.
        (Typical Input, Return Value Testing: needs sorting)
        """
        self.assertListEqual(sort_even([5, 6, 3, 4]), [3, 6, 5, 4])

    def test_typical_unsorted_even_indices(self):
        """
        Test case with a longer list where even indices are unsorted.
        Ensures correct sorting of even-indexed elements while preserving odd-indexed ones.
        (Typical Input, Logic Mutation: checks sorting logic)
        """
        self.assertListEqual(sort_even([9, 2, 1, 4, 7, 6, 3, 8, 5]), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_even_indices_already_sorted(self):
        """
        Test case where the even-indexed elements are already in sorted order.
        Ensures the function doesn't alter already sorted parts unnecessarily.
        (Typical Input, Return Value Testing: already sorted path)
        """
        self.assertListEqual(sort_even([1, 10, 3, 20, 5, 30]), [1, 10, 3, 20, 5, 30])

    def test_list_with_duplicate_values(self):
        """
        Test case with duplicate values, including duplicates at even indices.
        Ensures sorting handles duplicates correctly.
        (Edge Case: Duplicate values, Logic Mutation: sorting stability)
        """
        self.assertListEqual(sort_even([4, 1, 2, 3, 4, 5, 2, 7]), [2, 1, 2, 3, 4, 5, 4, 7])

    def test_list_with_negative_and_zero_values(self):
        """
        Test case including negative numbers and zero at even indices.
        Ensures correct numerical sorting across different signs.
        (Extreme Input: Sign and Zero Testing, Logic Mutation: comparison logic)
        """
        self.assertListEqual(sort_even([-5, 10, 0, -20, 5, 30, -1]), [-5, 10, -1, -20, 0, 30, 5])

    def test_long_list_even_at_ends_and_middle(self):
        """
        Test case with a longer list where even indices are at the beginning, middle, and end.
        Ensures all even indices are correctly identified and sorted, regardless of position.
        (Extreme Input, Boundary: first and last elements, Off-by-one: various positions)
        """
        self.assertListEqual(sort_even([10, 1, 8, 2, 6, 3, 4, 4, 2, 5, 0]), [0, 1, 2, 2, 4, 3, 6, 4, 8, 5, 10])

if __name__ == '__main__':
    unittest.main()