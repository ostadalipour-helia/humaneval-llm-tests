import unittest
from sut.problem_HumanEval_142 import sum_squares

class Test_sum_squares(unittest.TestCase):
    def test_normal_case_basic_sum(self):
        # Normal case: [1, 2, 3]
        # idx 0 (1) is multiple of 3 -> 1*1 = 1
        # idx 1 (2) is not multiple of 3 or 4 -> 2
        # idx 2 (3) is not multiple of 3 or 4 -> 3
        # Sum: 1 + 2 + 3 = 6
        self.assertEqual(sum_squares([1, 2, 3]), 6)

    def test_normal_case_mixed_negatives(self):
        # Normal case: [-1, -5, 2, -1, -5]
        # idx 0 (-1) is multiple of 3 -> (-1)*(-1) = 1
        # idx 1 (-5) is not multiple of 3 or 4 -> -5
        # idx 2 (2) is not multiple of 3 or 4 -> 2
        # idx 3 (-1) is multiple of 3 -> (-1)*(-1) = 1
        # idx 4 (-5) is multiple of 4 -> (-5)*(-5)*(-5) = -125
        # Sum: 1 + (-5) + 2 + 1 + (-125) = -126
        self.assertEqual(sum_squares([-1, -5, 2, -1, -5]), -126)

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
        self.assertEqual(sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]), 1062)

    def test_edge_case_empty_list(self):
        # Edge case: Empty list
        self.assertEqual(sum_squares([]), 0)

    def test_edge_case_single_element_zero(self):
        # Edge case: Single element, zero
        # idx 0 (0) is multiple of 3 -> 0*0 = 0
        self.assertEqual(sum_squares([0]), 0)

    def test_edge_case_single_element_large(self):
        # Edge case: Single element, large number
        # idx 0 (100) is multiple of 3 -> 100*100 = 10000
        self.assertEqual(sum_squares([100]), 10000)

    def test_edge_case_all_twos(self):
        # Edge case: List with all same elements
        # idx 0 (2): 2^2 = 4
        # idx 1 (2): 2
        # idx 2 (2): 2
        # idx 3 (2): 2^2 = 4
        # idx 4 (2): 2^3 = 8
        # Sum: 4 + 2 + 2 + 4 + 8 = 20
        self.assertEqual(sum_squares([2, 2, 2, 2, 2]), 20)

    def test_error_case_none_input(self):
        # Error case: Input is None
        with self.assertRaises(TypeError):
            sum_squares(None)

    def test_error_case_string_input(self):
        # Error case: Input is a string
        with self.assertRaises(TypeError):
            sum_squares("not a list")

    def test_error_case_list_with_float(self):
        # Error case: List contains a float
        with self.assertRaises(TypeError):
            sum_squares([1, 2.5, 3])

    def test_error_case_list_with_string(self):
        # Error case: List contains a string
        with self.assertRaises(TypeError):
            sum_squares([1, "a", 3])