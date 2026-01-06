import unittest
from sut.problem_HumanEval_87 import get_row

class Test_get_row(unittest.TestCase):

    def test_multiple_occurrences(self):
        lst = [
            [1, 2, 3, 4, 5, 6],
            [1, 2, 3, 4, 1, 6],
            [1, 2, 3, 4, 5, 1]
        ]
        x = 1
        expected = [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
        self.assertEqual(get_row(lst, x), expected)

    def test_single_occurrence(self):
        lst = [
            [10, 20, 30],
            [40, 50, 60],
            [70, 80, 90]
        ]
        x = 50
        expected = [(1, 1)]
        self.assertEqual(get_row(lst, x), expected)

    def test_not_present(self):
        lst = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        x = 0
        expected = []
        self.assertEqual(get_row(lst, x), expected)

    def test_empty_list(self):
        lst = []
        x = 1
        expected = []
        self.assertEqual(get_row(lst, x), expected)

    def test_with_empty_rows(self):
        lst = [
            [],
            [1],
            [1, 2, 3]
        ]
        x = 3
        expected = [(2, 2)]
        self.assertEqual(get_row(lst, x), expected)

    def test_all_elements_are_x(self):
        lst = [
            [7, 7, 7],
            [7, 7, 7]
        ]
        x = 7
        expected = [(0, 2), (0, 1), (0, 0), (1, 2), (1, 1), (1, 0)]
        self.assertEqual(get_row(lst, x), expected)

    def test_single_column_rows(self):
        lst = [
            [10],
            [20],
            [30]
        ]
        x = 20
        expected = [(1, 0)]
        self.assertEqual(get_row(lst, x), expected)

    def test_single_row_multiple_occurrences(self):
        lst = [
            [1, 2, 3, 1]
        ]
        x = 1
        expected = [(0, 3), (0, 0)]
        self.assertEqual(get_row(lst, x), expected)