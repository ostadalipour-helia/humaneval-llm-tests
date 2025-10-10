import unittest
from sut.problem_HumanEval_129 import minPath

class TestMinPath(unittest.TestCase):

    def test_example_1_from_docstring(self):
        # Critical: Typical input, path revisits cells.
        grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        k = 3
        expected_output = [1, 2, 1]
        self.assertEqual(minPath(grid, k), expected_output)

    def test_example_2_from_docstring(self):
        # Critical: Edge case k=1 (smallest path length).
        grid = [[5, 9, 3], [4, 1, 6], [7, 8, 2]]
        k = 1
        expected_output = [1]
        self.assertEqual(minPath(grid, k), expected_output)

    def test_smallest_grid_n2_k2(self):
        # Critical: Boundary N=2 (smallest grid size), k=2 (off-by-one from k=1).
        grid = [[1, 2], [3, 4]]
        k = 2
        expected_output = [1, 2] # Path: (0,0) -> (0,1)
        self.assertEqual(minPath(grid, k), expected_output)

    def test_smallest_grid_n2_k3_revisit(self):
        # Critical: Boundary N=2, k=3 (path length > N), forces revisit.
        grid = [[1, 2], [3, 4]]
        k = 3
        expected_output = [1, 2, 1] # Path: (0,0) -> (0,1) -> (0,0)
        self.assertEqual(minPath(grid, k), expected_output)

    def test_one_in_middle_n3_k2(self):
        # Critical: '1' in the middle, typical N=3, k=2.
        grid = [[2, 3, 4], [5, 1, 6], [7, 8, 9]]
        k = 2
        expected_output = [1, 3] # Path: (1,1) -> (0,1)
        self.assertEqual(minPath(grid, k), expected_output)

    def test_one_in_middle_n3_k3_revisit(self):
        # Critical: '1' in the middle, N=3, k=3, forces revisit to '1'.
        grid = [[2, 3, 4], [5, 1, 6], [7, 8, 9]]
        k = 3
        expected_output = [1, 3, 1] # Path: (1,1) -> (0,1) -> (1,1)
        self.assertEqual(minPath(grid, k), expected_output)

    def test_path_through_higher_values_n3_k3(self):
        # Critical: Path must navigate through higher values to find next smallest.
        grid = [[1, 4, 3], [5, 2, 6], [7, 8, 9]]
        k = 3
        expected_output = [1, 4, 1] # Path: (0,0) -> (0,1) -> (0,0)
        self.assertEqual(minPath(grid, k), expected_output)

    def test_longer_path_n3_k4_complex_revisit(self):
        # Critical: Longer path (k=4), N=3, specific value arrangement to test lexicographical choice.
        grid = [[1, 5, 2], [6, 3, 7], [8, 9, 4]]
        k = 4
        expected_output = [1, 5, 1, 5] # Path: (0,0) -> (0,1) -> (0,0) -> (0,1)
        self.assertEqual(minPath(grid, k), expected_output)

    def test_larger_grid_n4_k4_edge_path(self):
        # Critical: Larger grid (N=4), path along an edge, k=4.
        grid = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        k = 4
        expected_output = [1, 2, 1, 2] # Path: (0,0) -> (0,1) -> (0,0) -> (0,1)
        self.assertEqual(minPath(grid, k), expected_output)

    def test_n2_k_equals_n_squared_revisit_all_cells_possible(self):
        # Critical: N=2, k=N*N (k=4), path length equals total cells, forces revisits.
        grid = [[1, 2], [3, 4]]
        k = 4
        expected_output = [1, 2, 1, 2] # Path: (0,0) -> (0,1) -> (0,0) -> (0,1)
        self.assertEqual(minPath(grid, k), expected_output)

if __name__ == '__main__':
    unittest.main()