import unittest
import sut.problem_HumanEval_142 as mod

class TestHybrid(unittest.TestCase):
    def test_01_empty_list(self):
            # Edge Case: Empty list
            # Expected: 0 (as per docstring example)
            self.assertEqual(mod.sum_squares([]), 0)

    def test_02_single_element_list_index_0(self):
            # Edge Case: Single element list
            # Index 0 is a multiple of 3, so square the element.
            # 5**2 = 25
            self.assertEqual(mod.sum_squares([5]), 25)

    def test_03_small_list_only_multiple_of_3_indices(self):
            # Typical Case: List with indices 0, 1, 2
            # Index 0 (mult of 3): 1**2 = 1
            # Index 1 (no change): 2
            # Index 2 (no change): 3
            # Sum: 1 + 2 + 3 = 6 (as per docstring example)
            self.assertEqual(mod.sum_squares([1, 2, 3]), 6)

    def test_04_list_with_multiple_of_4_not_3_index(self):
            # Typical Case: List hitting index 4 (multiple of 4, not 3)
            # Index 0 (mult of 3): 1**2 = 1
            # Index 1 (no change): 2
            # Index 2 (no change): 3
            # Index 3 (mult of 3): 4**2 = 16
            # Index 4 (mult of 4, not 3): 5**3 = 125
            # Sum: 1 + 2 + 3 + 16 + 125 = 147
            self.assertEqual(mod.sum_squares([1, 2, 3, 4, 5]), 147)

    def test_05_boundary_index_multiple_of_3_and_4_precedence(self):
            # Boundary/Logic Mutation: Index 12 is a multiple of both 3 and 4.
            # The rule "multiple of 3" takes precedence.
            # List of 13 elements, value 2 at index 12.
            # Index 12 (mult of 3): 2**2 = 4
            # All other elements are 0, so their contribution is 0.
            # Sum: 4
            self.assertEqual(mod.sum_squares([0]*12 + [2]), 4)

    def test_06_off_by_one_and_boundary_around_multiples(self):
            # Off-by-One/Boundary: Test indices 2, 3, 4, 5
            # Index 0 (mult of 3): 1**2 = 1
            # Index 1 (no change): 1
            # Index 2 (no change): 1
            # Index 3 (mult of 3): 10**2 = 100
            # Index 4 (mult of 4, not 3): 100**3 = 1_000_000
            # Index 5 (no change): 1
            # Sum: 1 + 1 + 1 + 100 + 1_000_000 + 1 = 1_000_104
            self.assertEqual(mod.sum_squares([1, 1, 1, 10, 100, 1]), 1_000_104)

    def test_07_extreme_negative_numbers_and_docstring_example(self):
            # Extreme/Sign Testing: Negative numbers, as per docstring example.
            # Index 0 (mult of 3): (-1)**2 = 1
            # Index 1 (no change): -5
            # Index 2 (no change): 2
            # Index 3 (mult of 3): (-1)**2 = 1
            # Index 4 (mult of 4, not 3): (-5)**3 = -125
            # Sum: 1 + (-5) + 2 + 1 + (-125) = -126
            self.assertEqual(mod.sum_squares([-1, -5, 2, -1, -5]), -126)

    def test_08_edge_case_all_zeros_long_list(self):
            # Edge Case/Sign Testing: List of all zeros.
            # All operations (square, cube, no change) on 0 result in 0.
            # Sum: 0
            self.assertEqual(mod.sum_squares([0]*15), 0)

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
            self.assertEqual(mod.sum_squares([1, 1, 1, 2, 3, 1, 4, 1, 5]), 177)

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
            self.assertEqual(mod.sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]), 1516)

    def test_normal_case_basic_sum(self):
            # Normal case: [1, 2, 3]
            # idx 0 (1) is multiple of 3 -> 1*1 = 1
            # idx 1 (2) is not multiple of 3 or 4 -> 2
            # idx 2 (3) is not multiple of 3 or 4 -> 3
            # Sum: 1 + 2 + 3 = 6
            self.assertEqual(mod.sum_squares([1, 2, 3]), 6)

    def test_normal_case_mixed_negatives(self):
            # Normal case: [-1, -5, 2, -1, -5]
            # idx 0 (-1) is multiple of 3 -> (-1)*(-1) = 1
            # idx 1 (-5) is not multiple of 3 or 4 -> -5
            # idx 2 (2) is not multiple of 3 or 4 -> 2
            # idx 3 (-1) is multiple of 3 -> (-1)*(-1) = 1
            # idx 4 (-5) is multiple of 4 -> (-5)*(-5)*(-5) = -125
            # Sum: 1 + (-5) + 2 + 1 + (-125) = -126
            self.assertEqual(mod.sum_squares([-1, -5, 2, -1, -5]), -126)

    def test_normal_case_long_list_all_rules(self):
            # Normal case: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
            # idx 0 (1): 1^2 = 1
            # idx 1 (2): 2
            # idx 2 (3): 3
            # idx 3 (4): 4^2 = 16 (multiple of 3 takes precedence over 4, but 3%3==0, 4%3!=0, 4%4==0)
            # idx 4 (5): 5^3 = 125
            # idx 5 (6): 6
            # idx 6 (7): 7^2 = 49
            # idx 7 (8): 8
            # idx 8 (9): 9^3 = 729
            # idx 9 (10): 10^2 = 100
            # idx 10 (11): 11
            # idx 11 (12): 12
            # Sum: 1+2+3+16+125+6+49+8+729+100+11+12 = 1062
            self.assertEqual(mod.sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]), 1062)

    def test_edge_case_empty_list(self):
            # Edge case: Empty list
            self.assertEqual(mod.sum_squares([]), 0)

    def test_edge_case_single_element_zero(self):
            # Edge case: Single element, zero
            # idx 0 (0) is multiple of 3 -> 0*0 = 0
            self.assertEqual(mod.sum_squares([0]), 0)

    def test_edge_case_single_element_large(self):
            # Edge case: Single element, large number
            # idx 0 (100) is multiple of 3 -> 100*100 = 10000
            self.assertEqual(mod.sum_squares([100]), 10000)

    def test_edge_case_all_twos(self):
            # Edge case: List with all same elements
            # idx 0 (2): 2^2 = 4
            # idx 1 (2): 2
            # idx 2 (2): 2
            # idx 3 (2): 2^2 = 4
            # idx 4 (2): 2^3 = 8
            # Sum: 4 + 2 + 2 + 4 + 8 = 20
            self.assertEqual(mod.sum_squares([2, 2, 2, 2, 2]), 20)

    def test_error_case_none_input(self):
            # Error case: Input is None
            with self.assertRaises(TypeError):
                mod.sum_squares(None)

    def test_error_case_string_input(self):
            # Error case: Input is a string
            with self.assertRaises(TypeError):
                mod.sum_squares("not a list")

    def test_error_case_list_with_string(self):
            # Error case: List contains a string
            with self.assertRaises(TypeError):
                mod.sum_squares([1, "a", 3])

