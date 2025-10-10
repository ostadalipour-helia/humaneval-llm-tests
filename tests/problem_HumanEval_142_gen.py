import unittest
from sut.problem_HumanEval_142 import sum_squares

class TestSumSquares(unittest.TestCase):

    def test_01_empty_list(self):
        # Edge Case: Empty list
        # Expected: 0 (as per docstring example)
        self.assertEqual(sum_squares([]), 0)

    def test_02_single_element_list_index_0(self):
        # Edge Case: Single element list
        # Index 0 is a multiple of 3, so square the element.
        # 5**2 = 25
        self.assertEqual(sum_squares([5]), 25)

    def test_03_small_list_only_multiple_of_3_indices(self):
        # Typical Case: List with indices 0, 1, 2
        # Index 0 (mult of 3): 1**2 = 1
        # Index 1 (no change): 2
        # Index 2 (no change): 3
        # Sum: 1 + 2 + 3 = 6 (as per docstring example)
        self.assertEqual(sum_squares([1, 2, 3]), 6)

    def test_04_list_with_multiple_of_4_not_3_index(self):
        # Typical Case: List hitting index 4 (multiple of 4, not 3)
        # Index 0 (mult of 3): 1**2 = 1
        # Index 1 (no change): 2
        # Index 2 (no change): 3
        # Index 3 (mult of 3): 4**2 = 16
        # Index 4 (mult of 4, not 3): 5**3 = 125
        # Sum: 1 + 2 + 3 + 16 + 125 = 147
        self.assertEqual(sum_squares([1, 2, 3, 4, 5]), 147)

    def test_05_boundary_index_multiple_of_3_and_4_precedence(self):
        # Boundary/Logic Mutation: Index 12 is a multiple of both 3 and 4.
        # The rule "multiple of 3" takes precedence.
        # List of 13 elements, value 2 at index 12.
        # Index 12 (mult of 3): 2**2 = 4
        # All other elements are 0, so their contribution is 0.
        # Sum: 4
        self.assertEqual(sum_squares([0]*12 + [2]), 4)

    def test_06_off_by_one_and_boundary_around_multiples(self):
        # Off-by-One/Boundary: Test indices 2, 3, 4, 5
        # Index 0 (mult of 3): 1**2 = 1
        # Index 1 (no change): 1
        # Index 2 (no change): 1
        # Index 3 (mult of 3): 10**2 = 100
        # Index 4 (mult of 4, not 3): 100**3 = 1_000_000
        # Index 5 (no change): 1
        # Sum: 1 + 1 + 1 + 100 + 1_000_000 + 1 = 1_000_104
        self.assertEqual(sum_squares([1, 1, 1, 10, 100, 1]), 1_000_104)

    def test_07_extreme_negative_numbers_and_docstring_example(self):
        # Extreme/Sign Testing: Negative numbers, as per docstring example.
        # Index 0 (mult of 3): (-1)**2 = 1
        # Index 1 (no change): -5
        # Index 2 (no change): 2
        # Index 3 (mult of 3): (-1)**2 = 1
        # Index 4 (mult of 4, not 3): (-5)**3 = -125
        # Sum: 1 + (-5) + 2 + 1 + (-125) = -126
        self.assertEqual(sum_squares([-1, -5, 2, -1, -5]), -126)

    def test_08_edge_case_all_zeros_long_list(self):
        # Edge Case/Sign Testing: List of all zeros.
        # All operations (square, cube, no change) on 0 result in 0.
        # Sum: 0
        self.assertEqual(sum_squares([0]*15), 0)

    def test_09_logic_mutation_mixed_conditions_and_off_by_one(self):
        # Logic Mutation: Test various conditions and off-by-one for indices.
        # Index 0 (mult of 3): 1**2 = 1
        # Index 1 (no change): 1
        # Index 2 (no change): 1
        # Index 3 (mult of 3): 2**2 = 4
        # Index 4 (mult of 4, not 3): 3**3 = 27
        # Index 5 (no change): 1
        # Index 6 (mult of 3): 4**2 = 16
        # Index 7 (no change): 1
        # Index 8 (mult of 4, not 3): 5**3 = 125
        # Sum: 1 + 1 + 1 + 4 + 27 + 1 + 16 + 1 + 125 = 177
        self.assertEqual(sum_squares([1, 1, 1, 2, 3, 1, 4, 1, 5]), 177)

    def test_10_extreme_long_list_large_numbers_all_conditions(self):
        # Extreme/Boundary: Long list with large numbers, hitting all conditions multiple times.
        # Index 0 (mult of 3): 1**2 = 1
        # Index 1 (no change): 2
        # Index 2 (no change): 3
        # Index 3 (mult of 3): 4**2 = 16
        # Index 4 (mult of 4, not 3): 5**3 = 125
        # Index 5 (no change): 6
        # Index 6 (mult of 3): 7**2 = 49
        # Index 7 (no change): 8
        # Index 8 (mult of 4, not 3): 9**3 = 729
        # Index 9 (mult of 3): 10**2 = 100
        # Index 10 (no change): 11
        # Index 11 (no change): 12
        # Index 12 (mult of 3, precedence): 13**2 = 169
        # Index 13 (no change): 14
        # Index 14 (no change): 15
        # Index 15 (mult of 3, precedence): 16**2 = 256
        # Sum: 1 + 2 + 3 + 16 + 125 + 6 + 49 + 8 + 729 + 100 + 11 + 12 + 169 + 14 + 15 + 256 = 1516
        self.assertEqual(sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]), 1516)