import unittest
from sut.problem_HumanEval_133 import sum_squares

class TestSumSquares(unittest.TestCase):

    def test_example_1_positive_integers(self):
        # Typical input, all positive integers
        # [1,2,3] -> ceil([1,2,3]) -> [1,2,3] -> 1^2 + 2^2 + 3^2 = 1 + 4 + 9 = 14
        self.assertEqual(sum_squares([1, 2, 3]), 14)

    def test_example_2_positive_floats_and_zero(self):
        # Typical input, positive floats and zero, tests ceiling behavior
        # [1.4,4.2,0] -> ceil([1.4,4.2,0]) -> [2,5,0] -> 2^2 + 5^2 + 0^2 = 4 + 25 + 0 = 29
        self.assertEqual(sum_squares([1.4, 4.2, 0]), 29)

    def test_example_3_negative_float_and_positives(self):
        # Critical test for negative float ceiling behavior
        # [-2.4,1,1] -> ceil([-2.4,1,1]) -> [-2,1,1] -> (-2)^2 + 1^2 + 1^2 = 4 + 1 + 1 = 6
        self.assertEqual(sum_squares([-2.4, 1, 1]), 6)

    def test_empty_list_edge_case(self):
        # Edge case: empty list, should return 0
        self.assertEqual(sum_squares([]), 0)

    def test_single_element_positive_float_boundary(self):
        # Edge case: single element, positive float, tests ceiling
        # [3.1] -> ceil([3.1]) -> [4] -> 4^2 = 16
        self.assertEqual(sum_squares([3.1]), 16)

    def test_single_element_negative_float_boundary(self):
        # Edge case: single element, negative float, tests ceiling
        # [-3.9] -> ceil([-3.9]) -> [-3] -> (-3)^2 = 9
        self.assertEqual(sum_squares([-3.9]), 9)

    def test_all_negative_integers(self):
        # Extreme input: all negative integers
        # [-1,-2,-3] -> ceil([-1,-2,-3]) -> [-1,-2,-3] -> (-1)^2 + (-2)^2 + (-3)^2 = 1 + 4 + 9 = 14
        self.assertEqual(sum_squares([-1, -2, -3]), 14)

    def test_mixed_signs_and_floats_around_zero(self):
        # Logic mutation test: floats around zero and integers, mixed signs
        # [-0.5, 0.5, 1.5] -> ceil([-0.5, 0.5, 1.5]) -> [0, 1, 2] -> 0^2 + 1^2 + 2^2 = 0 + 1 + 4 = 5
        self.assertEqual(sum_squares([-0.5, 0.5, 1.5]), 5)

    def test_boundary_just_below_and_above_integer(self):
        # Boundary testing for ceiling function: values just below, just above, and exact integer
        # [0.99, 1.01, 2.0] -> ceil([0.99, 1.01, 2.0]) -> [1, 2, 2] -> 1^2 + 2^2 + 2^2 = 1 + 4 + 4 = 9
        self.assertEqual(sum_squares([0.99, 1.01, 2.0]), 9)

    def test_large_numbers_and_duplicates_after_ceiling(self):
        # Extreme input: large numbers, and values that become duplicates after ceiling
        # [99.1, 99.9, 100] -> ceil([99.1, 99.9, 100]) -> [100, 100, 100] -> 100^2 + 100^2 + 100^2 = 10000 + 10000 + 10000 = 30000
        self.assertEqual(sum_squares([99.1, 99.9, 100]), 30000)