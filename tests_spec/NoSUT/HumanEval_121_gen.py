import unittest
from sut.problem_HumanEval_121 import solution

class Test_solution(unittest.TestCase):

    def test_normal_mixed_odd_even(self):
        # Description: Mixed odd/even numbers, some in even positions are odd.
        lst = [5, 8, 7, 1]
        self.assertEqual(solution(lst), 12)

    def test_normal_all_odd(self):
        # Description: All elements are odd, sum of those in even positions.
        lst = [3, 3, 3, 3, 3]
        self.assertEqual(solution(lst), 9)

    def test_normal_no_odd_in_even_pos(self):
        # Description: No odd elements found in even positions.
        lst = [30, 13, 24, 321]
        self.assertEqual(solution(lst), 0)

    def test_edge_single_odd_element(self):
        # Description: Single element list, element is odd and in an even position.
        lst = [7]
        self.assertEqual(solution(lst), 7)

    def test_edge_single_even_element(self):
        # Description: Single element list, element is even and in an even position.
        lst = [8]
        self.assertEqual(solution(lst), 0)

    def test_edge_all_even_elements(self):
        # Description: All elements are even, resulting in a sum of zero.
        lst = [2, 4, 6, 8]
        self.assertEqual(solution(lst), 0)

    def test_edge_negative_odd_elements(self):
        # Description: List with negative odd numbers in even positions.
        lst = [-1, 2, -3, 4, -5]
        self.assertEqual(solution(lst), -9)

    def test_edge_zero_and_odd_in_odd_pos(self):
        # Description: List including zero (which is even), and odd numbers in odd positions.
        lst = [0, 1, 2, 3, 4, 5]
        self.assertEqual(solution(lst), 0)

    def test_error_empty_list(self):
        # Description: Input list is empty, violating 'non-empty' precondition.
        lst = []
        with self.assertRaises(ValueError):
            solution(lst)

    def test_error_non_integer_elements(self):
        # Description: Input list contains non-integer elements, violating 'all elements are integers' precondition.
        lst = [1, 2, "a", 4]
        with self.assertRaises(TypeError):
            solution(lst)

    def test_error_input_not_list_none(self):
        # Description: Input is not a list (None).
        lst = None
        with self.assertRaises(TypeError):
            solution(lst)

    def test_error_input_not_list_tuple(self):
        # Description: Input is a tuple instead of a list.
        lst = (1, 2, 3)
        with self.assertRaises(TypeError):
            solution(lst)

    def test_invariance_list_not_modified(self):
        # Description: Checks that the input list is not modified by the function.
        original_lst = [5, 8, 7, 1, 9]
        # Create a copy to compare against later
        lst_copy = list(original_lst)
        
        # Call the function
        _ = solution(original_lst)
        
        # Assert that the original list remains unchanged
        self.assertEqual(original_lst, lst_copy)