import unittest
from sut.problem_HumanEval_47 import median

class TestMedian(unittest.TestCase):

    def test_odd_length_basic(self):
        # Test case from docstring: odd length list
        self.assertEqual(median([3, 1, 2, 4, 5]), 3)

    def test_even_length_basic(self):
        # Test case from docstring: even length list
        self.assertEqual(median([-10, 4, 6, 1000, 10, 20]), 15.0)

    def test_single_element_list(self):
        # Test with a list containing a single element
        self.assertEqual(median([7]), 7)

    def test_two_elements_list(self):
        # Test with a list containing two elements
        self.assertEqual(median([10, 20]), 15.0)

    def test_odd_length_negative_numbers(self):
        # Test with an odd length list containing negative numbers
        self.assertEqual(median([-5, -1, -3]), -3)

    def test_even_length_negative_numbers(self):
        # Test with an even length list containing negative numbers
        self.assertEqual(median([-10, -20, -5, -15]), -12.5)

    def test_odd_length_with_duplicates(self):
        # Test with an odd length list containing duplicate numbers
        self.assertEqual(median([1, 5, 2, 5, 3]), 3)

    def test_even_length_with_duplicates(self):
        # Test with an even length list containing duplicate numbers
        self.assertEqual(median([1, 2, 2, 3]), 2.0)

    def test_larger_odd_list_unsorted(self):
        # Test with a larger odd length list that is unsorted
        self.assertEqual(median([9, 1, 7, 3, 5]), 5)

    def test_larger_even_list_unsorted(self):
        # Test with a larger even length list that is unsorted
        self.assertEqual(median([8, 2, 6, 4, 10, 0]), 5.0)