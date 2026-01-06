import unittest
from sut.problem_HumanEval_129 import minPath

class Test_minPath(unittest.TestCase):

    def test_case_0(self):
        grid = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        k = 3
        expected = [1, 2, 1]
        self.assertEqual(minPath(grid, k), expected)

    def test_case_1(self):
        grid = [
            [5, 9, 3],
            [4, 1, 6],
            [7, 8, 2]
        ]
        k = 1
        expected = [1]
        self.assertEqual(minPath(grid, k), expected)

    def test_case_2(self):
        grid = [
            [10, 20, 30],
            [40, 1, 50],
            [60, 70, 80]
        ]
        k = 4
        expected = [1, 20, 1, 20]
        self.assertEqual(minPath(grid, k), expected)

    def test_case_3(self):
        grid = [
            [1, 2],
            [3, 4]
        ]
        k = 2
        expected = [1, 2]
        self.assertEqual(minPath(grid, k), expected)

    def test_case_4(self):
        grid = [
            [4, 3],
            [2, 1]
        ]
        k = 5
        expected = [1, 2, 1, 2, 1]
        self.assertEqual(minPath(grid, k), expected)

    def test_case_5(self):
        grid = [
            [1, 5, 9],
            [2, 6, 10],
            [3, 7, 8]
        ]
        k = 6
        expected = [1, 2, 1, 2, 1, 2]
        self.assertEqual(minPath(grid, k), expected)

    def test_case_6(self):
        grid = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        k = 3
        expected = [1, 2, 1]
        self.assertEqual(minPath(grid, k), expected)

    def test_case_7(self):
        grid = [
            [5, 9, 3],
            [4, 1, 6],
            [7, 8, 2]
        ]
        k = 1
        expected = [1]
        self.assertEqual(minPath(grid, k), expected)

    def test_case_8(self):
        grid = [
            [10, 20, 30],
            [40, 1, 50],
            [60, 70, 80]
        ]
        k = 4
        expected = [1, 20, 1, 20]
        self.assertEqual(minPath(grid, k), expected)

    def test_case_9(self):
        grid = [
            [1, 2],
            [3, 4]
        ]
        k = 2
        expected = [1, 2]
        self.assertEqual(minPath(grid, k), expected)