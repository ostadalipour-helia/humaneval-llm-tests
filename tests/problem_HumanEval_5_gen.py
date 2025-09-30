import unittest
from sut.problem_HumanEval_5 import intersperse

class TestIntersperse(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(intersperse([], 4), [])

    def test_single_element_list(self):
        self.assertEqual(intersperse([1], 4), [1])

    def test_two_elements_list(self):
        self.assertEqual(intersperse([1, 2], 4), [1, 4, 2])

    def test_three_elements_positive(self):
        self.assertEqual(intersperse([1, 2, 3], 4), [1, 4, 2, 4, 3])

    def test_negative_numbers_zero_delimiter(self):
        self.assertEqual(intersperse([-1, -2, -3], 0), [-1, 0, -2, 0, -3])

    def test_list_with_zeros_positive_delimiter(self):
        self.assertEqual(intersperse([0, 1, 0], 5), [0, 5, 1, 5, 0])

    def test_delimiter_in_list_multiple_times(self):
        self.assertEqual(intersperse([1, 4, 2, 4], 4), [1, 4, 4, 4, 2, 4, 4])

    def test_longer_list_negative_delimiter(self):
        self.assertEqual(intersperse([10, 20, 30, 40, 50], -1), [10, -1, 20, -1, 30, -1, 40, -1, 50])

    def test_different_positive_values(self):
        self.assertEqual(intersperse([7, 8, 9], 100), [7, 100, 8, 100, 9])

    def test_two_elements_negative_delimiter(self):
        self.assertEqual(intersperse([10, 20], -5), [10, -5, 20])

if __name__ == '__main__':
    unittest.main()