import unittest
from sut_llm.problem_HumanEval_26 import remove_duplicates

class TestRemoveDuplicates(unittest.TestCase):

    def test_example_from_docstring(self):
        self.assertEqual(remove_duplicates([1, 2, 3, 2, 4]), [1, 3, 4])

    def test_no_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_all_elements_are_duplicates(self):
        self.assertEqual(remove_duplicates([1, 1, 2, 2, 3, 3]), [])

    def test_empty_list(self):
        self.assertEqual(remove_duplicates([]), [])

    def test_single_element_list(self):
        self.assertEqual(remove_duplicates([5]), [5])

    def test_list_with_two_identical_elements(self):
        self.assertEqual(remove_duplicates([7, 7]), [])

    def test_duplicates_at_beginning_and_end(self):
        self.assertEqual(remove_duplicates([1, 2, 3, 1, 2]), [3])

    def test_duplicates_at_the_beginning(self):
        self.assertEqual(remove_duplicates([1, 1, 2, 3, 4]), [2, 3, 4])

    def test_list_with_negative_numbers_and_zeros(self):
        self.assertEqual(remove_duplicates([-1, 0, 1, -1, 0, 2]), [1, 2])

    def test_larger_list_with_various_duplicates(self):
        self.assertEqual(remove_duplicates([10, 20, 10, 30, 40, 20, 50, 60, 60]), [30, 40, 50])

if __name__ == '__main__':
    unittest.main()