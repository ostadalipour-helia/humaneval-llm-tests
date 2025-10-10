import unittest
from sut_llm.problem_HumanEval_121 import solution

class TestSolution(unittest.TestCase):

    def test_example_one(self):
        # Basic functionality - Example 1 from docstring
        # [5 (idx 0, even pos, odd val), 8, 7 (idx 2, even pos, odd val), 1]
        # Sum = 5 + 7 = 12
        self.assertEqual(solution([5, 8, 7, 1]), 12)

    def test_example_two(self):
        # Basic functionality - Example 2 from docstring
        # [3 (idx 0), 3, 3 (idx 2), 3, 3 (idx 4)]
        # Sum = 3 + 3 + 3 = 9
        self.assertEqual(solution([3, 3, 3, 3, 3]), 9)

    def test_example_three_returns_zero(self):
        # Basic functionality - Example 3 from docstring, returns 0
        # [30 (idx 0, even pos, even val), 13, 24 (idx 2, even pos, even val), 321]
        # No elements meet criteria.
        self.assertEqual(solution([30, 13, 24, 321]), 0)

    def test_edge_case_single_element_qualifying(self):
        # Edge case: single element list, element qualifies
        # [7 (idx 0, even pos, odd val)]
        self.assertEqual(solution([7]), 7)

    def test_edge_case_single_element_not_qualifying(self):
        # Edge case: single element list, element does not qualify
        # [8 (idx 0, even pos, even val)]
        self.assertEqual(solution([8]), 0)

    def test_boundary_first_element_qualifies_only(self):
        # Boundary condition: only the first element (index 0) qualifies
        # [1 (idx 0, even pos, odd val), 2, 4, 6, 8]
        self.assertEqual(solution([1, 2, 4, 6, 8]), 1)

    def test_boundary_last_even_position_qualifies_only(self):
        # Boundary condition: only the last element in an even position qualifies
        # [2, 4, 6, 8, 9 (idx 4, even pos, odd val)]
        self.assertEqual(solution([2, 4, 6, 8, 9]), 9)

    def test_extreme_negative_odd_numbers(self):
        # Extreme/unusual input: list with negative odd numbers
        # [-1 (idx 0), 2, -3 (idx 2), 4, -5 (idx 4)]
        # Sum = -1 + -3 + -5 = -9
        self.assertEqual(solution([-1, 2, -3, 4, -5]), -9)

    def test_extreme_large_numbers(self):
        # Extreme/unusual input: list with very large numbers
        # [1000000001 (idx 0), 2, 3000000003 (idx 2), 4, 5000000005 (idx 4), 6]
        # Sum = 1000000001 + 3000000003 + 5000000005 = 9000000009
        self.assertEqual(solution([1000000001, 2, 3000000003, 4, 5000000005, 6]), 9000000009)

    def test_logic_mutation_all_odd_but_position_matters(self):
        # Logic mutation: all elements are odd, but only those in even positions should be summed
        # [1 (idx 0), 3, 5 (idx 2), 7, 9 (idx 4), 11]
        # Sum = 1 + 5 + 9 = 15
        self.assertEqual(solution([1, 3, 5, 7, 9, 11]), 15)