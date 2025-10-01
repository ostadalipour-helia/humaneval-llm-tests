import unittest
from sut.problem_HumanEval_129 import minPath

class TestMinPath(unittest.TestCase):

    def test_01_example_1(self):
        grid = [[1,2,3], [4,5,6], [7,8,9]]
        k = 3
        expected = [1, 2, 1]
        self.assertEqual(minPath(grid, k), expected)

    def test_02_example_2(self):
        grid = [[5,9,3], [4,1,6], [7,8,2]]
        k = 1
        expected = [1]
        self.assertEqual(minPath(grid, k), expected)

    def test_03_smallest_grid_k_is_1(self):
        grid = [[1,2], [3,4]]
        k = 1
        expected = [1]
        self.assertEqual(minPath(grid, k), expected)

    def test_04_smallest_grid_k_is_2(self):
        grid = [[1,2], [3,4]]
        k = 2
        expected = [1, 2]
        self.assertEqual(minPath(grid, k), expected)

    def test_05_smallest_grid_k_is_3(self):
        grid = [[1,2], [3,4]]
        k = 3
        expected = [1, 2, 1]
        self.assertEqual(minPath(grid, k), expected)

    def test_06_smallest_grid_k_is_4_revisit(self):
        grid = [[1,2], [3,4]]
        k = 4
        expected = [1, 2, 1, 2]
        self.assertEqual(minPath(grid, k), expected)

    def test_07_one_in_middle_k_is_2(self):
        grid = [[7,8,9], [6,1,2], [5,4,3]]
        k = 2
        expected = [1, 2]
        self.assertEqual(minPath(grid, k), expected)

    def test_08_one_in_corner_k_is_3_no_two_nearby(self):
        grid = [[1,7,8], [9,6,5], [4,3,2]]
        k = 3
        expected = [1, 7, 1]
        self.assertEqual(minPath(grid, k), expected)

    def test_09_three_by_three_k_is_4_simple_path(self):
        grid = [[1,2,3], [8,9,4], [7,6,5]]
        k = 4
        expected = [1, 2, 1, 2]
        self.assertEqual(minPath(grid, k), expected)

    def test_10_larger_grid_k_is_2_one_not_at_origin(self):
        grid = [[10,11,12,13], [14,1,2,15], [16,3,4,17], [18,19,20,21]]
        k = 2
        expected = [1, 2]
        self.assertEqual(minPath(grid, k), expected)

if __name__ == '__main__':
    unittest.main()