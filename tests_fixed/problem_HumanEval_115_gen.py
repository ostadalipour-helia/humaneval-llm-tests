import unittest
from sut_llm.problem_HumanEval_115 import max_fill

class TestMaxFill(unittest.TestCase):

    def test_example_1(self):
        grid = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
        capacity = 1
        self.assertEqual(max_fill(grid, capacity), 6)

    def test_example_2(self):
        grid = [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
        capacity = 2
        self.assertEqual(max_fill(grid, capacity), 5)

    def test_example_3(self):
        grid = [[0,0,0], [0,0,0]]
        capacity = 5
        self.assertEqual(max_fill(grid, capacity), 0)

    def test_single_well_exact_capacity(self):
        grid = [[1,1,1,1]]
        capacity = 4
        self.assertEqual(max_fill(grid, capacity), 1)

    def test_single_well_uneven_capacity(self):
        grid = [[1,1,1,1,1]]
        capacity = 2
        self.assertEqual(max_fill(grid, capacity), 3)

    def test_multiple_empty_wells(self):
        grid = [[0,0], [0,0], [0,0]]
        capacity = 1
        self.assertEqual(max_fill(grid, capacity), 0)

    def test_multiple_full_wells_capacity_one(self):
        grid = [[1,1], [1,1], [1,1]]
        capacity = 1
        self.assertEqual(max_fill(grid, capacity), 6)

    def test_mixed_wells_and_capacity(self):
        grid = [[1,0,1], [0,1,0], [1,1,1]]
        capacity = 3
        self.assertEqual(max_fill(grid, capacity), 3)

    def test_large_grid_small_capacity(self):
        grid = [[1,1,1,1,1,1,1,1,1,1], [1,1,1,1,1,1,1,1,1,1]]
        capacity = 1
        self.assertEqual(max_fill(grid, capacity), 20)

    def test_large_grid_large_capacity(self):
        grid = [[1,1,1,1,1,1,1,1,1,1], [1,1,1,1,1,1,1,1,1,1]]
        capacity = 10
        self.assertEqual(max_fill(grid, capacity), 2)

if __name__ == '__main__':
    unittest.main()