import unittest
import sut.problem_HumanEval_52 as mod

class TestHybrid(unittest.TestCase):
    def test_1_basic_all_below(self):
            # Test case from docstring: all numbers are well below the threshold.
            self.assertEqual(mod.below_threshold([1, 2, 4, 10], 100), True)

    def test_2_basic_one_above(self):
            # Test case from docstring: one number is above the threshold.
            self.assertEqual(mod.below_threshold([1, 20, 4, 10], 5), False)

    def test_3_boundary_one_at_threshold(self):
            # Boundary test: one number is exactly equal to the threshold.
            # This should return False, catching a '<=' mutation.
            self.assertEqual(mod.below_threshold([1, 5, 3], 5), False)

    def test_5_edge_empty_list(self):
            # Edge case: an empty list. Should be True (vacuously true).
            self.assertEqual(mod.below_threshold([], 10), True)

    def test_6_edge_single_element_below(self):
            # Edge case: a single-element list where the element is below the threshold.
            self.assertEqual(mod.below_threshold([5], 10), True)

    def test_7_edge_single_element_at_threshold(self):
            # Edge case: a single-element list where the element is at the threshold.
            # Should be False, catching a '<=' mutation.
            self.assertEqual(mod.below_threshold([10], 10), False)

    def test_8_sign_negative_numbers_and_threshold(self):
            # Test with negative numbers and a negative threshold.
            # All numbers [-5, -2, -10] are less than -1.
            self.assertEqual(mod.below_threshold([-5, -2, -10], -1), True)

    def test_9_sign_zero_and_mixed_numbers_with_zero_threshold(self):
            # Test with zero, positive, and negative numbers, and a zero threshold.
            # 0 is not < 0, 1 is not < 0.
            self.assertEqual(mod.below_threshold([-1, 0, 1], 0), False)

    def test_10_extreme_large_numbers_all_same_below(self):
            # Test with large numbers, all of which are the same and below the threshold.
            self.assertEqual(mod.below_threshold([999999, 999999, 999999], 1000000), True)

    def test_list_with_negative_numbers_all_below(self):
            l = [-5, 0, 3]
            t = 10
            original_l = list(l)
            result = mod.below_threshold(l, t)
            self.assertTrue(result, "Expected True for negative numbers all below threshold.")
            self.assertEqual(l, original_l, "Input list 'l' should not be modified.")

    def test_empty_list(self):
            l = []
            t = 5
            original_l = list(l)
            result = mod.below_threshold(l, t)
            self.assertTrue(result, "Expected True for an empty list (vacuously true).")
            self.assertEqual(l, original_l, "Input list 'l' should not be modified.")

    def test_all_numbers_equal_to_threshold(self):
            l = [5, 5, 5]
            t = 5
            original_l = list(l)
            result = mod.below_threshold(l, t)
            self.assertFalse(result, "Expected False when all numbers are equal to the threshold (not strictly below).")
            self.assertEqual(l, original_l, "Input list 'l' should not be modified.")

    def test_floats_very_close_to_threshold_but_below(self):
            l = [4.9, 4.99, 4.999]
            t = 5
            original_l = list(l)
            result = mod.below_threshold(l, t)
            self.assertTrue(result, "Expected True for floats very close to but still below the threshold.")
            self.assertEqual(l, original_l, "Input list 'l' should not be modified.")

    def test_floats_equal_or_above_threshold(self):
            l = [5.0, 5.1, 6]
            t = 5
            original_l = list(l)
            result = mod.below_threshold(l, t)
            self.assertFalse(result, "Expected False for floats equal to or above the threshold.")
            self.assertEqual(l, original_l, "Input list 'l' should not be modified.")

    def test_single_element_equal_to_threshold(self):
            l = [10]
            t = 10
            original_l = list(l)
            result = mod.below_threshold(l, t)
            self.assertFalse(result, "Expected False for a single element equal to the threshold.")
            self.assertEqual(l, original_l, "Input list 'l' should not be modified.")

    def test_positive_numbers_with_negative_threshold(self):
            l = [1, 2, 3]
            t = -1
            original_l = list(l)
            result = mod.below_threshold(l, t)
            self.assertFalse(result, "Expected False when positive numbers are compared to a negative threshold.")
            self.assertEqual(l, original_l, "Input list 'l' should not be modified.")

    def test_error_l_not_a_list(self):
            l = "not a list"
            t = 5
            with self.assertRaises(TypeError, msg="Expected TypeError when 'l' is not a list."):
                mod.below_threshold(l, t)

    def test_error_t_not_numeric(self):
            l = [1, 2, 3]
            t = "not an int"
            with self.assertRaises(TypeError, msg="Expected TypeError when 't' is not an integer."):
                mod.below_threshold(l, t)

    def test_error_list_contains_non_comparable_elements(self):
            l = [1, "a", 3]
            t = 5
            with self.assertRaises(TypeError, msg="Expected TypeError when list contains non-numeric elements."):
                mod.below_threshold(l, t)

