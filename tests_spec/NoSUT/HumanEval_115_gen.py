import unittest
from sut.problem_HumanEval_115 import max_fill

class Test_max_fill(unittest.TestCase):

    def test_normal_multiple_wells_capacity_1(self):
        # Description: Multiple wells, varying water levels, capacity 1.
        grid = [
            [0, 0, 1, 0],
            [0, 1, 0, 0],
            [1, 1, 1, 1]
        ]
        capacity = 1
        expected_output = 6
        self.assertEqual(max_fill(grid, capacity), expected_output)

    def test_normal_all_empty_wells(self):
        # Description: All wells are empty, capacity 5.
        grid = [
            [0, 0, 0],
            [0, 0, 0]
        ]
        capacity = 5
        expected_output = 0
        self.assertEqual(max_fill(grid, capacity), expected_output)

    def test_normal_all_wells_full_exact_capacity(self):
        # Description: All wells full, capacity matches well water exactly.
        grid = [
            [1, 1, 1],
            [1, 1, 1]
        ]
        capacity = 3
        expected_output = 2
        self.assertEqual(max_fill(grid, capacity), expected_output)

    def test_edge_1x1_with_water(self):
        # Description: Smallest possible grid (1x1) with water, capacity 1.
        grid = [[1]]
        capacity = 1
        expected_output = 1
        self.assertEqual(max_fill(grid, capacity), expected_output)

    def test_edge_single_well_max_water_min_capacity(self):
        # Description: Single well with maximum water, minimum capacity.
        grid = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
        capacity = 1
        expected_output = 10
        self.assertEqual(max_fill(grid, capacity), expected_output)

    def test_edge_10x10_full_wells_max_capacity(self):
        # Description: Grid with 10x10 full wells, capacity 10.
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
        expected_output = 10
        self.assertEqual(max_fill(grid, capacity), expected_output)

    def test_error_grid_not_list(self):
        # Description: 'grid' is not a list.
        grid = "not a list"
        capacity = 1
        with self.assertRaises(TypeError):
            max_fill(grid, capacity)

    def test_error_grid_not_rectangular(self):
        # Description: 'grid' is not rectangular (rows have different lengths).
        grid = [
            [0, 1],
            [0, 1, 1]
        ]
        capacity = 1
        with self.assertRaises(ValueError):
            max_fill(grid, capacity)

    def test_error_grid_empty(self):
        # Description: 'grid' is empty (violates 1 <= len(grid)).
        grid = []
        capacity = 1
        with self.assertRaises(ValueError):
            max_fill(grid, capacity)

    def test_error_capacity_less_than_1(self):
        # Description: 'capacity' is less than 1.
        grid = [[0, 1]]
        capacity = 0
        with self.assertRaises(ValueError):
            max_fill(grid, capacity)