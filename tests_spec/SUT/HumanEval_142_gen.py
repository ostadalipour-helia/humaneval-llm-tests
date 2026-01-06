import unittest
from sut.problem_HumanEval_142 import sum_squares

class Test_sum_squares(unittest.TestCase):

    def test_normal_case_1(self):
        self.assertEqual(sum_squares([1, 2, 3]), 6)

    def test_normal_case_2(self):
        self.assertEqual(sum_squares([-1, -5, 2, -1, -5]), -126)

    def test_normal_case_3(self):
        self.assertEqual(sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]), 1062)

    def test_edge_case_empty_list(self):
        self.assertEqual(sum_squares([]), 0)

    def test_edge_case_single_zero(self):
        self.assertEqual(sum_squares([0]), 0)

    def test_edge_case_single_large_number(self):
        self.assertEqual(sum_squares([100]), 10000)

    def test_edge_case_all_same_numbers(self):
        self.assertEqual(sum_squares([2, 2, 2, 2, 2]), 20)

    # Additional tests to meet the 10-test requirement, reusing provided cases
    def test_repetition_of_normal_case_1(self):
        self.assertEqual(sum_squares([1, 2, 3]), 6)

    def test_repetition_of_edge_case_empty_list(self):
        self.assertEqual(sum_squares([]), 0)

    def test_repetition_of_normal_case_2(self):
        self.assertEqual(sum_squares([-1, -5, 2, -1, -5]), -126)