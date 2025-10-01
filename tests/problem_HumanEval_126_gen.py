import unittest
from sut.problem_HumanEval_126 import is_sorted

class TestIsSorted(unittest.TestCase):

    def test_empty_list(self):
        self.assertTrue(is_sorted([]))

    def test_single_element_list(self):
        self.assertTrue(is_sorted([5]))

    def test_perfectly_sorted_list(self):
        self.assertTrue(is_sorted([1, 2, 3, 4, 5]))

    def test_unsorted_list_simple(self):
        self.assertFalse(is_sorted([1, 3, 2, 4, 5]))

    def test_sorted_with_single_duplicates(self):
        self.assertTrue(is_sorted([1, 2, 2, 3, 3, 4]))

    def test_unsorted_with_single_duplicates(self):
        self.assertFalse(is_sorted([1, 3, 2, 2, 4]))

    def test_sorted_with_too_many_duplicates(self):
        self.assertFalse(is_sorted([1, 2, 2, 2, 3, 4]))

    def test_all_same_two_elements(self):
        self.assertTrue(is_sorted([7, 7]))

    def test_all_same_three_elements(self):
        self.assertFalse(is_sorted([7, 7, 7]))

    def test_longer_sorted_list_with_zero_and_valid_duplicates(self):
        self.assertTrue(is_sorted([0, 10, 20, 20, 30, 40]))

if __name__ == '__main__':
    unittest.main()