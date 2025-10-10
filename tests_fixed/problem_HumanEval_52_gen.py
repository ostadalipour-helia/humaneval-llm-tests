import unittest
from sut_llm.problem_HumanEval_52 import below_threshold

class TestBelowThreshold(unittest.TestCase):

    def test_1_basic_all_below(self):
        # Test case from docstring: all numbers are well below the threshold.
        self.assertEqual(below_threshold([1, 2, 4, 10], 100), True)

    def test_2_basic_one_above(self):
        # Test case from docstring: one number is above the threshold.
        self.assertEqual(below_threshold([1, 20, 4, 10], 5), False)

    def test_3_boundary_one_at_threshold(self):
        # Boundary test: one number is exactly equal to the threshold.
        # This should return False, catching a '<=' mutation.
        self.assertEqual(below_threshold([1, 5, 3], 5), False)

    def test_4_boundary_one_just_below_threshold(self):
        # Boundary test: one number is just one less than the threshold.
        # This should return True.
        self.assertEqual(below_threshold([1, 4, 3], 5), True)

    def test_5_edge_empty_list(self):
        # Edge case: an empty list. Should be True (vacuously true).
        self.assertEqual(below_threshold([], 10), True)

    def test_6_edge_single_element_below(self):
        # Edge case: a single-element list where the element is below the threshold.
        self.assertEqual(below_threshold([5], 10), True)

    def test_7_edge_single_element_at_threshold(self):
        # Edge case: a single-element list where the element is at the threshold.
        # Should be False, catching a '<=' mutation.
        self.assertEqual(below_threshold([10], 10), False)

    def test_8_sign_negative_numbers_and_threshold(self):
        # Test with negative numbers and a negative threshold.
        # All numbers [-5, -2, -10] are less than -1.
        self.assertEqual(below_threshold([-5, -2, -10], -1), True)

    def test_9_sign_zero_and_mixed_numbers_with_zero_threshold(self):
        # Test with zero, positive, and negative numbers, and a zero threshold.
        # 0 is not < 0, 1 is not < 0.
        self.assertEqual(below_threshold([-1, 0, 1], 0), False)

    def test_10_extreme_large_numbers_all_same_below(self):
        # Test with large numbers, all of which are the same and below the threshold.
        self.assertEqual(below_threshold([999999, 999999, 999999], 1000000), True)