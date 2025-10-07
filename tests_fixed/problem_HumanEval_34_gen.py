import unittest
from sut_llm.problem_HumanEval_34 import unique

class TestUnique(unittest.TestCase):

    def test_01_basic_example(self):
        self.assertEqual(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]), [0, 2, 3, 5, 9, 123])

    def test_02_empty_list(self):
        self.assertEqual(unique([]), [])

    def test_03_single_element_list(self):
        self.assertEqual(unique([7]), [7])

    def test_04_all_unique_and_sorted(self):
        self.assertEqual(unique([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_05_all_unique_but_unsorted(self):
        self.assertEqual(unique([5, 1, 4, 2, 3]), [1, 2, 3, 4, 5])

    def test_06_all_duplicate_elements(self):
        self.assertEqual(unique([8, 8, 8, 8]), [8])

    def test_07_list_with_negative_numbers_and_zero(self):
        self.assertEqual(unique([-3, -1, 0, -3, -1]), [-3, -1, 0])

    def test_08_mixed_positive_negative_zero_with_duplicates(self):
        self.assertEqual(unique([0, -5, 2, 0, -5, 1, 2]), [-5, 0, 1, 2])

    def test_09_many_duplicates_and_wider_range(self):
        self.assertEqual(unique([10, 1, 100, 1, 10, 100, 50, 50]), [1, 10, 50, 100])

    def test_10_already_sorted_with_duplicates(self):
        self.assertEqual(unique([1, 1, 2, 2, 3, 3, 4, 4]), [1, 2, 3, 4])

if __name__ == '__main__':
    unittest.main()