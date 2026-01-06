import unittest
from sut.problem_HumanEval_52 import below_threshold

class Test_below_threshold(unittest.TestCase):

    def test_all_numbers_below_threshold(self):
        l = [1, 2, 4, 10]
        t = 100
        original_l = list(l) # Copy for invariant check
        result = below_threshold(l, t)
        self.assertTrue(result, "Expected True when all numbers are strictly below the threshold.")
        self.assertEqual(l, original_l, "Input list 'l' should not be modified.")

    def test_at_least_one_number_not_below_threshold(self):
        l = [1, 20, 4, 10]
        t = 5
        original_l = list(l)
        result = below_threshold(l, t)
        self.assertFalse(result, "Expected False when at least one number is not strictly below the threshold.")
        self.assertEqual(l, original_l, "Input list 'l' should not be modified.")

    def test_list_with_negative_numbers_all_below(self):
        l = [-5, 0, 3]
        t = 10
        original_l = list(l)
        result = below_threshold(l, t)
        self.assertTrue(result, "Expected True for negative numbers all below threshold.")
        self.assertEqual(l, original_l, "Input list 'l' should not be modified.")

    def test_empty_list(self):
        l = []
        t = 5
        original_l = list(l)
        result = below_threshold(l, t)
        self.assertTrue(result, "Expected True for an empty list (vacuously true).")
        self.assertEqual(l, original_l, "Input list 'l' should not be modified.")

    def test_all_numbers_equal_to_threshold(self):
        l = [5, 5, 5]
        t = 5
        original_l = list(l)
        result = below_threshold(l, t)
        self.assertFalse(result, "Expected False when all numbers are equal to the threshold (not strictly below).")
        self.assertEqual(l, original_l, "Input list 'l' should not be modified.")

    def test_floats_very_close_to_threshold_but_below(self):
        l = [4.9, 4.99, 4.999]
        t = 5
        original_l = list(l)
        result = below_threshold(l, t)
        self.assertTrue(result, "Expected True for floats very close to but still below the threshold.")
        self.assertEqual(l, original_l, "Input list 'l' should not be modified.")

    def test_floats_equal_or_above_threshold(self):
        l = [5.0, 5.1, 6]
        t = 5
        original_l = list(l)
        result = below_threshold(l, t)
        self.assertFalse(result, "Expected False for floats equal to or above the threshold.")
        self.assertEqual(l, original_l, "Input list 'l' should not be modified.")

    def test_single_element_equal_to_threshold(self):
        l = [10]
        t = 10
        original_l = list(l)
        result = below_threshold(l, t)
        self.assertFalse(result, "Expected False for a single element equal to the threshold.")
        self.assertEqual(l, original_l, "Input list 'l' should not be modified.")

    def test_positive_numbers_with_negative_threshold(self):
        l = [1, 2, 3]
        t = -1
        original_l = list(l)
        result = below_threshold(l, t)
        self.assertFalse(result, "Expected False when positive numbers are compared to a negative threshold.")
        self.assertEqual(l, original_l, "Input list 'l' should not be modified.")

    def test_error_l_not_a_list(self):
        l = "not a list"
        t = 5
        with self.assertRaises(TypeError, msg="Expected TypeError when 'l' is not a list."):
            below_threshold(l, t)

    def test_error_t_not_numeric(self):
        l = [1, 2, 3]
        t = "not an int"
        with self.assertRaises(TypeError, msg="Expected TypeError when 't' is not an integer."):
            below_threshold(l, t)

    def test_error_list_contains_non_comparable_elements(self):
        l = [1, "a", 3]
        t = 5
        with self.assertRaises(TypeError, msg="Expected TypeError when list contains non-numeric elements."):
            below_threshold(l, t)