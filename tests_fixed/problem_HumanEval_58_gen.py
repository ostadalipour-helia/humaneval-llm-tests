import unittest
from sut_llm.problem_HumanEval_58 import common

class TestCommonFunction(unittest.TestCase):

    def test_example_one(self):
        # Test case from docstring
        l1 = [1, 4, 3, 34, 653, 2, 5]
        l2 = [5, 7, 1, 5, 9, 653, 121]
        expected = [1, 5, 653]
        self.assertEqual(common(l1, l2), expected)

    def test_example_two(self):
        # Test case from docstring
        l1 = [5, 3, 2, 8]
        l2 = [3, 2]
        expected = [2, 3]
        self.assertEqual(common(l1, l2), expected)

    def test_no_common_elements(self):
        # Test case where lists have no common elements
        l1 = [1, 2, 3]
        l2 = [4, 5, 6]
        expected = []
        self.assertEqual(common(l1, l2), expected)

    def test_one_common_element(self):
        # Test case with exactly one common element
        l1 = [10, 20, 30]
        l2 = [30, 40, 50]
        expected = [30]
        self.assertEqual(common(l1, l2), expected)

    def test_duplicates_in_input_lists(self):
        # Test case with duplicates in input lists, ensuring unique output
        l1 = [1, 2, 2, 3, 3, 3]
        l2 = [2, 3, 4, 4]
        expected = [2, 3]
        self.assertEqual(common(l1, l2), expected)

    def test_empty_lists(self):
        # Test case with both input lists being empty
        l1 = []
        l2 = []
        expected = []
        self.assertEqual(common(l1, l2), expected)

    def test_one_list_empty(self):
        # Test case with one input list being empty
        l1 = [1, 2, 3]
        l2 = []
        expected = []
        self.assertEqual(common(l1, l2), expected)

    def test_all_elements_common(self):
        # Test case where all elements are common
        l1 = [1, 2, 3]
        l2 = [1, 2, 3]
        expected = [1, 2, 3]
        self.assertEqual(common(l1, l2), expected)

    def test_negative_and_zero_numbers(self):
        # Test case with negative numbers and zero
        l1 = [-5, 0, 5, 10]
        l2 = [0, -5, 15, 20]
        expected = [-5, 0]
        self.assertEqual(common(l1, l2), expected)

    def test_unsorted_large_numbers(self):
        # Test case with unsorted larger numbers, ensuring sorted output
        l1 = [99, 1, 50, 1000, 2]
        l2 = [2, 1000, 50, 5]
        expected = [2, 50, 1000]
        self.assertEqual(common(l1, l2), expected)

if __name__ == '__main__':
    unittest.main()