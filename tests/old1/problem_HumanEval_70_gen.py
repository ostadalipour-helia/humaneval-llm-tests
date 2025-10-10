import unittest
from sut.problem_HumanEval_70 import strange_sort_list

class TestStrangeSortList(unittest.TestCase):

    def test_example_1(self):
        # Test case from the docstring
        self.assertEqual(strange_sort_list([1, 2, 3, 4]), [1, 4, 2, 3])

    def test_example_2(self):
        # Test case from the docstring with all identical elements
        self.assertEqual(strange_sort_list([5, 5, 5, 5]), [5, 5, 5, 5])

    def test_empty_list(self):
        # Test case from the docstring for an empty list
        self.assertEqual(strange_sort_list([]), [])

    def test_single_element_list(self):
        # Test case for a list with a single element
        self.assertEqual(strange_sort_list([7]), [7])

    def test_two_elements_list(self):
        # Test case for a list with two elements
        self.assertEqual(strange_sort_list([10, 20]), [10, 20])

    def test_three_elements_list(self):
        # Test case for a list with three elements
        self.assertEqual(strange_sort_list([1, 2, 3]), [1, 3, 2])

    def test_reverse_sorted_list(self):
        # Test case for a list that is initially reverse sorted
        self.assertEqual(strange_sort_list([4, 3, 2, 1]), [1, 4, 2, 3])

    def test_list_with_duplicates(self):
        # Test case for a list containing duplicate values
        self.assertEqual(strange_sort_list([1, 2, 2, 3]), [1, 3, 2, 2])

    def test_list_with_negative_numbers(self):
        # Test case for a list containing only negative numbers
        self.assertEqual(strange_sort_list([-5, -1, -3, -2]), [-5, -1, -3, -2])

    def test_list_with_mixed_numbers(self):
        # Test case for a list with mixed positive, negative, and zero values
        self.assertEqual(strange_sort_list([-10, 0, 5, -5, 10]), [-10, 10, -5, 5, 0])

if __name__ == '__main__':
    unittest.main()