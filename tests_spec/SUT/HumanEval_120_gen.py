import unittest
from sut.problem_HumanEval_120 import maximum

class Test_maximum(unittest.TestCase):

    def test_normal_case_1(self):
        self.assertEqual(maximum([-4, -3, 5], 3), [-4, -3, 5])

    def test_normal_case_2(self):
        self.assertEqual(maximum([-4, 4, 4], 2), [4, 4])

    def test_normal_case_3(self):
        self.assertEqual(maximum([-3, -2, -1, 1, 1, 2, 2], 1), [2])

    def test_normal_case_4(self):
        self.assertEqual(maximum([5, 10, 15, 20, 25], 3), [15, 20, 25])

    def test_edge_case_k_is_zero(self):
        self.assertEqual(maximum([1, 2, 3, 4, 5], 0), [])

    def test_edge_case_full_range(self):
        self.assertEqual(maximum([-1000, 0, 500, 1000], 4), [-1000, 0, 500, 1000])

    def test_edge_case_single_element(self):
        self.assertEqual(maximum([7], 1), [7])

    def test_edge_case_all_negative(self):
        self.assertEqual(maximum([-10, -5, -2, -1], 2), [-2, -1])

    def test_edge_case_all_identical(self):
        self.assertEqual(maximum([5, 5, 5, 5, 5], 3), [5, 5, 5])

    def test_edge_case_sorted_array(self):
        self.assertEqual(maximum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5), [6, 7, 8, 9, 10])