import unittest
from sut.problem_HumanEval_30 import get_positive

class TestGetPositive(unittest.TestCase):

    def test_docstring_example_1(self):
        self.assertEqual(get_positive([-1, 2, -4, 5, 6]), [2, 5, 6])

    def test_docstring_example_2(self):
        self.assertEqual(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), [5, 3, 2, 3, 9, 123, 1])

    def test_all_positive_numbers(self):
        self.assertEqual(get_positive([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_all_negative_numbers(self):
        self.assertEqual(get_positive([-1, -2, -3, -4, -5]), [])

    def test_mixed_numbers_with_zeros(self):
        self.assertEqual(get_positive([0, 1, -1, 2, -2, 0, 3]), [1, 2, 3])

    def test_empty_list(self):
        self.assertEqual(get_positive([]), [])

    def test_list_with_only_zeros(self):
        self.assertEqual(get_positive([0, 0, 0, 0]), [])

    def test_single_positive_number(self):
        self.assertEqual(get_positive([42]), [42])

    def test_single_negative_number(self):
        self.assertEqual(get_positive([-99]), [])

    def test_single_zero(self):
        self.assertEqual(get_positive([0]), [])

if __name__ == '__main__':
    unittest.main()