import unittest
from sut.problem_HumanEval_37 import sort_even

class TestSortEven(unittest.TestCase):

    def test_1_docstring_example_1(self):
        # Test case from the docstring
        self.assertEqual(sort_even([1, 2, 3]), [1, 2, 3])

    def test_2_docstring_example_2(self):
        # Test case from the docstring
        self.assertEqual(sort_even([5, 6, 3, 4]), [3, 6, 5, 4])

    def test_3_empty_list(self):
        # Test with an empty list
        self.assertEqual(sort_even([]), [])

    def test_4_single_element_list(self):
        # Test with a list containing a single element (even index)
        self.assertEqual(sort_even([10]), [10])

    def test_5_two_elements_list(self):
        # Test with a list containing two elements (one even, one odd)
        self.assertEqual(sort_even([10, 5]), [10, 5])

    def test_6_longer_list_unsorted_even(self):
        # Test with a longer list where even-indexed elements need sorting
        self.assertEqual(sort_even([4, 1, 2, 3, 0, 5]), [0, 1, 2, 3, 4, 5])

    def test_7_longer_list_already_sorted_even(self):
        # Test with a longer list where even-indexed elements are already sorted
        self.assertEqual(sort_even([0, 1, 2, 3, 4, 5]), [0, 1, 2, 3, 4, 5])

    def test_8_longer_list_reverse_sorted_even(self):
        # Test with a longer list where even-indexed elements are reverse sorted
        self.assertEqual(sort_even([6, 1, 4, 3, 2, 5]), [2, 1, 4, 3, 6, 5])

    def test_9_list_with_duplicate_even_numbers(self):
        # Test with a list containing duplicate numbers at even indices
        self.assertEqual(sort_even([4, 1, 2, 3, 4, 5, 0]), [0, 1, 2, 3, 4, 5, 4])

    def test_10_list_with_negative_numbers(self):
        # Test with a list containing negative numbers
        self.assertEqual(sort_even([-5, 10, -1, 20, -10, 30]), [-10, 10, -5, 20, -1, 30])

if __name__ == '__main__':
    unittest.main()