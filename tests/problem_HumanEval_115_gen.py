import unittest
from sut.problem_HumanEval_115 import max_fill

class TestMaxFill(unittest.TestCase):

    def test_example_1(self):
        # Test case from the docstring example 1
        grid = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
        capacity = 1
        self.assertEqual(max_fill(grid, capacity), 6)

    def test_example_2(self):
        # Test case from the docstring example 2
        grid = [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
        capacity = 2
        self.assertEqual(max_fill(grid, capacity), 5)

    def test_example_3_no_water(self):
        # Test case from the docstring example 3 (Edge Case: No water, returns 0)
        grid = [[0,0,0], [0,0,0]]
        capacity = 5
        self.assertEqual(max_fill(grid, capacity), 0)

    def test_boundary_min_capacity_and_off_by_one_water(self):
        # Boundary Test: Minimum capacity (1) with water units exactly, less than, and more than capacity
        # Also covers multiple wells and varying well lengths
        grid = [[1], [1,1], [1,1,1]] # 1, 2, 3 units of water
        capacity = 1
        # Well 1: 1 water, capacity 1 -> ceil(1/1) = 1 lower
        # Well 2: 2 water, capacity 1 -> ceil(2/1) = 2 lowers
        # Well 3: 3 water, capacity 1 -> ceil(3/1) = 3 lowers
        self.assertEqual(max_fill(grid, capacity), 1 + 2 + 3) # Expected: 6

    def test_boundary_max_capacity_and_off_by_one_water(self):
        # Boundary Test: Maximum capacity (10) with water units exactly, less than, and more than capacity
        grid = [[1]*10, [1]*9, [1]*11] # 10, 9, 11 units of water
        capacity = 10
        # Well 1: 10 water, capacity 10 -> ceil(10/10) = 1 lower
        # Well 2: 9 water, capacity 10 -> ceil(9/10) = 1 lower
        # Well 3: 11 water, capacity 10 -> ceil(11/10) = 2 lowers
        self.assertEqual(max_fill(grid, capacity), 1 + 1 + 2) # Expected: 4

    def test_edge_single_well_single_water_unit(self):
        # Edge Case: Single well, single unit of water, capacity greater than water
        grid = [[0,0,1,0,0]]
        capacity = 5
        # Well 1: 1 water, capacity 5 -> ceil(1/5) = 1 lower
        self.assertEqual(max_fill(grid, capacity), 1)

    def test_edge_single_well_all_water_min_capacity(self):
        # Edge Case: Single well, all water, minimum capacity (1)
        grid = [[1,1,1,1,1]]
        capacity = 1
        # Well 1: 5 water, capacity 1 -> ceil(5/1) = 5 lowers
        self.assertEqual(max_fill(grid, capacity), 5)

    def test_extreme_large_grid_mixed_water(self):
        # Extreme Input: A larger grid with a mix of full and empty wells
        # 5 wells with 10 water each, 5 wells with 0 water each
        grid = [[1]*10 for _ in range(5)] + [[0]*10 for _ in range(5)]
        capacity = 3
        # 5 wells * ceil(10/3) lowers/well = 5 * 4 = 20 lowers
        # 5 wells * 0 lowers/well = 0 lowers
        self.assertEqual(max_fill(grid, capacity), 20)

    def test_extreme_max_grid_all_water_min_capacity(self):
        # Extreme Input: Max grid dimensions (100x100) with all water, minimum capacity (1)
        grid = [[1]*100 for _ in range(100)]
        capacity = 1
        # 100 wells * (100 water / 1 capacity) lowers/well = 100 * 100 = 10000 lowers
        self.assertEqual(max_fill(grid, capacity), 10000)

    def test_logic_mutation_ceil_division_accuracy(self):
        # Logic Mutation Test: Verifies correct use of ceiling division for non-exact divisions
        # Catches potential bugs if integer division or floor was used instead of ceil
        grid = [[1,1,1,1,1], [1,1,1,1,1,1]] # 5 water, 6 water
        capacity = 3
        # Well 1: 5 water, capacity 3 -> ceil(5/3) = 2 lowers
        # Well 2: 6 water, capacity 3 -> ceil(6/3) = 2 lowers
        self.assertEqual(max_fill(grid, capacity), 2 + 2) # Expected: 4