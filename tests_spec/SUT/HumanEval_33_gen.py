import unittest
from sut.problem_HumanEval_33 import sort_third

class Test_sort_third(unittest.TestCase):

    def test_normal_case_1(self):
        self.assertEqual(sort_third([1, 2, 3]), [' ', '1', ',', ' ', '2', ',', '[', '3', ']'])

    def test_normal_case_2(self):
        self.assertEqual(sort_third([5, 6, 3, 4, 8, 9, 2]), [' ', '5', ',', ' ', '6', ',', ' ', '3', ',', ' ', '4', ',', ' ', '8', ',', ' ', '9', ',', '[', '2', ']'])

    def test_normal_case_3(self):
        self.assertEqual(sort_third([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]), [' ', '9', ',', ' ', '8', ',', ' ', '7', ',', ' ', '6', ',', ' ', '5', ',', ' ', '4', ',', ' ', '3', ',', ' ', '2', ',', ' ', '1', ',', '[', '0', ']'])

    def test_normal_case_4(self):
        self.assertEqual(sort_third([10, 20, 30, 40, 50, 60]), [' ', '1', '0', ',', ' ', '2', ',', ',', ' ', '0', '0', ',', '0', '4', '0', '3', ' ', '5', '6', ',', ' ', '[', '0', ']'])

    def test_edge_case_empty(self):
        self.assertEqual(sort_third([]), ['[', ']'])

    def test_edge_case_single_element(self):
        self.assertEqual(sort_third([10]), ['[', '1', '0', ']'])

    def test_edge_case_two_elements(self):
        self.assertEqual(sort_third([1, 2]), [' ', '1', ',', '[', '2', ']'])

    def test_edge_case_reverse_sorted(self):
        self.assertEqual(sort_third([9, 2, 1, 3, 5, 4]), [' ', '9', ',', ' ', '2', ',', ' ', '1', ',', ' ', '3', ',', ' ', '5', ',', '[', '4', ']'])

    def test_edge_case_duplicates(self):
        self.assertEqual(sort_third([1, 2, 3, 1, 5, 6, 1]), [' ', '1', ',', ' ', '2', ',', ' ', '3', ',', ' ', '1', ',', ' ', '5', ',', ' ', '6', ',', '[', '1', ']'])

    def test_edge_case_negatives(self):
        self.assertEqual(sort_third([-1, 0, -3, -2, -5, -6]), [' ', '-', '1', ',', ' ', '0', ',', ' ', '-', ',', ',', ' ', '-', '2', ',', '3', '-', '5', '6', ' ', '-', '[', ']'])