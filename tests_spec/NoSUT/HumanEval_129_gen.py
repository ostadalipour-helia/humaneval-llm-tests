import unittest
from sut.problem_HumanEval_129 import minPath

class Test_minPath(unittest.TestCase):
    def test_normal_case_basic_backtrack(self):
        grid = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        k = 3
        expected_output = [1, 2, 1]
        self.assertEqual(minPath(grid, k), expected_output)

    def test_normal_case_middle_start(self):
        grid = [
            [10, 20, 30],
            [40, 1, 50],
            [60, 70, 80]
        ]
        k = 4
        expected_output = [1, 40, 1, 50]
        self.assertEqual(minPath(grid, k), expected_output)

    def test_edge_case_n2_k2(self):
        grid = [
            [1, 2],
            [3, 4]
        ]
        k = 2
        expected_output = [1, 2]
        self.assertEqual(minPath(grid, k), expected_output)

    def test_edge_case_n2_long_path(self):
        grid = [
            [4, 3],
            [2, 1]
        ]
        k = 5
        expected_output = [1, 2, 1, 2, 1]
        self.assertEqual(minPath(grid, k), expected_output)

    def test_edge_case_complex_path(self):
        grid = [
            [1, 5, 9],
            [2, 6, 10],
            [3, 7, 8]
        ]
        k = 6
        expected_output = [1, 2, 3, 2, 1, 5]
        self.assertEqual(minPath(grid, k), expected_output)

    def test_error_empty_grid(self):
        grid = []
        k = 3
        with self.assertRaises(ValueError):
            minPath(grid, k)

    def test_error_non_square_grid(self):
        grid = [
            [1, 2],
            [3]
        ]
        k = 2
        with self.assertRaises(ValueError):
            minPath(grid, k)

    def test_error_n_less_than_2(self):
        grid = [
            [1]
        ]
        k = 1
        with self.assertRaises(ValueError):
            minPath(grid, k)

    def test_error_k_not_positive(self):
        grid = [
            [1, 2],
            [3, 4]
        ]
        k = 0
        with self.assertRaises(ValueError):
            minPath(grid, k)

    def test_error_duplicate_values(self):
        grid = [
            [1, 2],
            [3, 3]
        ]
        k = 2
        with self.assertRaises(ValueError):
            minPath(grid, k)

    def test_error_missing_value(self):
        grid = [
            [1, 2],
            [3, 5]
        ]
        k = 2
        with self.assertRaises(ValueError):
            minPath(grid, k)

    def test_error_non_integer_value(self):
        grid = [
            [1, "a"],
            [3, 4]
        ]
        k = 2
        with self.assertRaises(TypeError):
            minPath(grid, k)