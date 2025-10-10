import unittest
from sut.problem_HumanEval_136 import largest_smallest_integers

class TestLargestSmallestIntegers(unittest.TestCase):

    def test_example_only_positives(self):
        self.assertEqual(largest_smallest_integers([2, 4, 1, 3, 5, 7]), (None, 1))

    def test_example_empty_list(self):
        self.assertEqual(largest_smallest_integers([]), (None, None))

    def test_example_only_zero(self):
        self.assertEqual(largest_smallest_integers([0]), (None, None))

    def test_mixed_positives_and_negatives(self):
        self.assertEqual(largest_smallest_integers([-1, -5, 2, 4, 1]), (-1, 1))

    def test_only_negatives(self):
        self.assertEqual(largest_smallest_integers([-2, -4, -1, -3, -5]), (-1, None))

    def test_mixed_with_duplicates(self):
        self.assertEqual(largest_smallest_integers([-10, -5, -1, 1, 5, 10, -1, 1]), (-1, 1))

    def test_single_negative_and_single_positive(self):
        self.assertEqual(largest_smallest_integers([-7, 3]), (-7, 3))

    def test_large_numbers_mixed(self):
        self.assertEqual(largest_smallest_integers([-1000, -500, 1, 500, 1000]), (-500, 1))

    def test_only_one_negative(self):
        self.assertEqual(largest_smallest_integers([-5]), (-5, None))

    def test_only_one_positive(self):
        self.assertEqual(largest_smallest_integers([5]), (None, 5))

if __name__ == '__main__':
    unittest.main()