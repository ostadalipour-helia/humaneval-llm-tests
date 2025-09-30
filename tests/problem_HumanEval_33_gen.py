import unittest
from sut.problem_HumanEval_33 import sort_third

class TestSortThird(unittest.TestCase):

    def test_01_empty_list(self):
        # Test with an empty list
        self.assertEqual(sort_third([]), [])

    def test_02_single_element_list(self):
        # Test with a list containing a single element (index 0 is divisible by 3)
        self.assertEqual(sort_third([5]), [5])

    def test_03_docstring_example_1(self):
        # Test with the first example from the docstring
        self.assertEqual(sort_third([1, 2, 3]), [1, 2, 3])

    def test_04_docstring_example_2(self):
        # Test with the second example from the docstring
        self.assertEqual(sort_third([5, 6, 3, 4, 8, 9, 2]), [2, 6, 3, 4, 8, 9, 5])

    def test_05_already_sorted_divisible_indices(self):
        # Test where elements at divisible-by-three indices are already sorted
        self.assertEqual(sort_third([1, 2, 3, 4, 5, 6, 7]), [1, 2, 3, 4, 5, 6, 7])

    def test_06_reverse_sorted_divisible_indices(self):
        # Test where elements at divisible-by-three indices are in reverse order
        self.assertEqual(sort_third([7, 2, 5, 4, 3, 6, 1]), [1, 2, 5, 4, 3, 6, 7])

    def test_07_mixed_values_and_longer_list(self):
        # Test with a longer list and mixed values, including multiple divisible-by-three indices
        self.assertEqual(sort_third([9, 1, 8, 2, 7, 3, 6, 4, 5, 0]), [0, 1, 8, 2, 7, 3, 6, 4, 5, 9])

    def test_08_list_with_negative_numbers(self):
        # Test with negative numbers and zeros
        self.assertEqual(sort_third([-1, 0, -5, 2, -3, 4, -2]), [-2, 0, -5, -1, -3, 4, 2])

    def test_09_list_with_duplicate_values_at_divisible_indices(self):
        # Test with duplicate values at divisible-by-three indices
        self.assertEqual(sort_third([3, 1, 2, 1, 5, 4, 3, 7, 0]), [1, 1, 2, 3, 5, 4, 3, 7, 0])

    def test_10_short_list_only_first_element_affected(self):
        # Test a short list where only the first element (index 0) is affected
        self.assertEqual(sort_third([10, 20]), [10, 20])

if __name__ == '__main__':
    unittest.main()