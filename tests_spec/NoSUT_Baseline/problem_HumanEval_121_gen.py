import unittest
import sut.problem_HumanEval_121 as mod

class TestHybrid(unittest.TestCase):
    def test_example_one(self):
            # Basic functionality - Example 1 from docstring
            # [5 (idx 0, even pos, odd val), 8, 7 (idx 2, even pos, odd val), 1]
            # Sum = 5 + 7 = 12
            self.assertEqual(mod.solution([5, 8, 7, 1]), 12)

    def test_example_two(self):
            # Basic functionality - Example 2 from docstring
            # [3 (idx 0), 3, 3 (idx 2), 3, 3 (idx 4)]
            # Sum = 3 + 3 + 3 = 9
            self.assertEqual(mod.solution([3, 3, 3, 3, 3]), 9)

    def test_example_three_returns_zero(self):
            # Basic functionality - Example 3 from docstring, returns 0
            # [30 (idx 0, even pos, even val), 13, 24 (idx 2, even pos, even val), 321]
            # No elements meet criteria.
            self.assertEqual(mod.solution([30, 13, 24, 321]), 0)

    def test_edge_case_single_element_qualifying(self):
            # Edge case: single element list, element qualifies
            # [7 (idx 0, even pos, odd val)]
            self.assertEqual(mod.solution([7]), 7)

    def test_edge_case_single_element_not_qualifying(self):
            # Edge case: single element list, element does not qualify
            # [8 (idx 0, even pos, even val)]
            self.assertEqual(mod.solution([8]), 0)

    def test_boundary_first_element_qualifies_only(self):
            # Boundary condition: only the first element (index 0) qualifies
            # [1 (idx 0, even pos, odd val), 2, 4, 6, 8]
            self.assertEqual(mod.solution([1, 2, 4, 6, 8]), 1)

    def test_boundary_last_even_position_qualifies_only(self):
            # Boundary condition: only the last element in an even position qualifies
            # [2, 4, 6, 8, 9 (idx 4, even pos, odd val)]
            self.assertEqual(mod.solution([2, 4, 6, 8, 9]), 9)

    def test_extreme_negative_odd_numbers(self):
            # Extreme/unusual input: list with negative odd numbers
            # [-1 (idx 0), 2, -3 (idx 2), 4, -5 (idx 4)]
            # Sum = -1 + -3 + -5 = -9
            self.assertEqual(mod.solution([-1, 2, -3, 4, -5]), -9)

    def test_extreme_large_numbers(self):
            # Extreme/unusual input: list with very large numbers
            # [1000000001 (idx 0), 2, 3000000003 (idx 2), 4, 5000000005 (idx 4), 6]
            # Sum = 1000000001 + 3000000003 + 5000000005 = 9000000009
            self.assertEqual(mod.solution([1000000001, 2, 3000000003, 4, 5000000005, 6]), 9000000009)

    def test_logic_mutation_all_odd_but_position_matters(self):
            # Logic mutation: all elements are odd, but only those in even positions should be summed
            # [1 (idx 0), 3, 5 (idx 2), 7, 9 (idx 4), 11]
            # Sum = 1 + 5 + 9 = 15
            self.assertEqual(mod.solution([1, 3, 5, 7, 9, 11]), 15)

    def test_normal_mixed_odd_even(self):
            # Description: Mixed odd/even numbers, some in even positions are odd.
            lst = [5, 8, 7, 1]
            self.assertEqual(mod.solution(lst), 12)

    def test_normal_all_odd(self):
            # Description: All elements are odd, sum of those in even positions.
            lst = [3, 3, 3, 3, 3]
            self.assertEqual(mod.solution(lst), 9)

    def test_normal_no_odd_in_even_pos(self):
            # Description: No odd elements found in even positions.
            lst = [30, 13, 24, 321]
            self.assertEqual(mod.solution(lst), 0)

    def test_edge_single_odd_element(self):
            # Description: Single element list, element is odd and in an even position.
            lst = [7]
            self.assertEqual(mod.solution(lst), 7)

    def test_edge_single_even_element(self):
            # Description: Single element list, element is even and in an even position.
            lst = [8]
            self.assertEqual(mod.solution(lst), 0)

    def test_edge_all_even_elements(self):
            # Description: All elements are even, resulting in a sum of zero.
            lst = [2, 4, 6, 8]
            self.assertEqual(mod.solution(lst), 0)

    def test_edge_negative_odd_elements(self):
            # Description: List with negative odd numbers in even positions.
            lst = [-1, 2, -3, 4, -5]
            self.assertEqual(mod.solution(lst), -9)

    def test_edge_zero_and_odd_in_odd_pos(self):
            # Description: List including zero (which is even), and odd numbers in odd positions.
            lst = [0, 1, 2, 3, 4, 5]
            self.assertEqual(mod.solution(lst), 0)

    def test_error_non_integer_elements(self):
            # Description: Input list contains non-integer elements, violating 'all elements are integers' precondition.
            lst = [1, 2, "a", 4]
            with self.assertRaises(TypeError):
                mod.solution(lst)

    def test_error_input_not_list_none(self):
            # Description: Input is not a list (None).
            lst = None
            with self.assertRaises(TypeError):
                mod.solution(lst)

    def test_invariance_list_not_modified(self):
            # Description: Checks that the input list is not modified by the function.
            original_lst = [5, 8, 7, 1, 9]
            # Create a copy to compare against later
            lst_copy = list(original_lst)
            
            # Call the function
            _ = mod.solution(original_lst)
            
            # Assert that the original list remains unchanged
            self.assertEqual(original_lst, lst_copy)

