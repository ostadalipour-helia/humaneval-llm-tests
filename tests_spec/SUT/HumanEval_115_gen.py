import unittest
from sut.problem_HumanEval_115 import max_fill

class Test_max_fill(unittest.TestCase):

    def test_case_0(self):
        grid = [[0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]]
        capacity = 1
        expected = 6
        self.assertEqual(max_fill(grid, capacity), expected)

    def test_case_1(self):
        grid = [[0, 0, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1]]
        capacity = 2
        expected = 5
        self.assertEqual(max_fill(grid, capacity), expected)

    def test_case_2(self):
        grid = [[0, 0, 0], [0, 0, 0]]
        capacity = 5
        expected = 0
        self.assertEqual(max_fill(grid, capacity), expected)

    def test_case_3(self):
        grid = [[1, 1, 1], [1, 1, 1]]
        capacity = 3
        expected = 2
        self.assertEqual(max_fill(grid, capacity), expected)

    def test_case_4(self):
        grid = [[1]]
        capacity = 1
        expected = 1
        self.assertEqual(max_fill(grid, capacity), expected)

    def test_case_5(self):
        grid = [[0]]
        capacity = 1
        expected = 0
        self.assertEqual(max_fill(grid, capacity), expected)

    def test_case_6(self):
        grid = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
        capacity = 1
        expected = 10
        self.assertEqual(max_fill(grid, capacity), expected)

    def test_case_7(self):
        grid = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
        capacity = 10
        expected = 1
        self.assertEqual(max_fill(grid, capacity), expected)

    def test_case_8(self):
        grid = [[1, 0, 1], [0, 1, 0]]
        capacity = 1
        expected = 3
        self.assertEqual(max_fill(grid, capacity), expected)

    def test_case_9(self):
        grid = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]
        capacity = 10
        expected = 10
        self.assertEqual(max_fill(grid, capacity), expected)