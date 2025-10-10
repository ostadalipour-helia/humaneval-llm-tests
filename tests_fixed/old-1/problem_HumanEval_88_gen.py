import unittest
from sut_llm.problem_HumanEval_88 import sort_array

class TestSortArray(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(sort_array([]), [])

    def test_single_element_array(self):
        self.assertEqual(sort_array([5]), [5])

    def test_ascending_sort_example(self):
        # Example from docstring: first=2, last=5, sum=7 (odd) -> ascending
        self.assertEqual(sort_array([2, 4, 3, 0, 1, 5]), [0, 1, 2, 3, 4, 5])

    def test_descending_sort_example(self):
        # Example from docstring: first=2, last=6, sum=8 (even) -> descending
        self.assertEqual(sort_array([2, 4, 3, 0, 1, 5, 6]), [6, 5, 4, 3, 2, 1, 0])

    def test_ascending_sort_simple(self):
        # Simple case: first=1, last=2, sum=3 (odd) -> ascending
        self.assertEqual(sort_array([1, 0, 2]), [0, 1, 2])

    def test_descending_sort_simple(self):
        # Simple case: first=10, last=0, sum=10 (even) -> descending
        self.assertEqual(sort_array([10, 5, 0]), [10, 5, 0])

    def test_ascending_sort_with_duplicates(self):
        # Array with duplicates: first=3, last=6, sum=9 (odd) -> ascending
        self.assertEqual(sort_array([3, 1, 4, 1, 5, 9, 2, 6]), [1, 1, 2, 3, 4, 5, 6, 9])

    def test_descending_sort_with_zero_and_duplicates(self):
        # Array with zero and duplicates: first=10, last=0, sum=10 (even) -> descending
        self.assertEqual(sort_array([10, 10, 20, 0, 0]), [20, 10, 10, 0, 0])

    def test_ascending_sort_longer_array(self):
        # Longer array: first=10, last=5, sum=15 (odd) -> ascending
        self.assertEqual(sort_array([10, 1, 8, 2, 7, 3, 6, 4, 5]), [1, 2, 3, 4, 5, 6, 7, 8, 10])

    def test_array_immutability(self):
        # Test that the original array is not modified
        original_array = [3, 1, 2]
        original_array_copy = list(original_array) # Create a true copy for comparison
        
        # For this array: first=3, last=2, sum=5 (odd) -> ascending
        result = sort_array(original_array)
        
        self.assertEqual(original_array, original_array_copy) # Assert original array is unchanged
        self.assertEqual(result, [1, 2, 3]) # Assert the result is correct