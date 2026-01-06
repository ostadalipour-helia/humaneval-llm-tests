import unittest
from sut.problem_HumanEval_9 import rolling_max

class Test_rolling_max(unittest.TestCase):

    def test_normal_case_1(self):
        self.assertEqual(rolling_max([1, 2, 3, 2, 3, 4, 2]), [1, 2, 3, 3, 3, 4, 4])

    def test_normal_case_2(self):
        self.assertEqual(rolling_max([5, 1, 8, 2, 9]), [5, 5, 8, 8, 9])

    def test_strictly_decreasing(self):
        self.assertEqual(rolling_max([10, 9, 8, 7, 6]), [10, 10, 10, 10, 10])

    def test_with_negatives_and_zero(self):
        self.assertEqual(rolling_max([-5, -1, -8, 0, -2]), [-5, -1, -1, 0, 0])

    def test_edge_empty_list(self):
        self.assertEqual(rolling_max([]), [])

    def test_edge_single_element(self):
        self.assertEqual(rolling_max([7]), [7])

    def test_edge_all_identical(self):
        self.assertEqual(rolling_max([3, 3, 3, 3]), [3, 3, 3, 3])

    def test_edge_all_zeros(self):
        self.assertEqual(rolling_max([0, 0, 0]), [0, 0, 0])

    def test_duplicate_normal_case_1(self):
        self.assertEqual(rolling_max([1, 2, 3, 2, 3, 4, 2]), [1, 2, 3, 3, 3, 4, 4])

    def test_duplicate_strictly_decreasing(self):
        self.assertEqual(rolling_max([10, 9, 8, 7, 6]), [10, 10, 10, 10, 10])