import unittest
from sut.problem_HumanEval_136 import largest_smallest_integers

class Test_largest_smallest_integers(unittest.TestCase):

    # Normal Cases
    def test_normal_mixed_pos_neg_integers(self):
        self.assertEqual(largest_smallest_integers([1, 2, 3, -1, -2, -3]), (-1, 1))

    def test_normal_mixed_pos_neg_different_ranges(self):
        self.assertEqual(largest_smallest_integers([-10, -5, -1, 1, 5, 10]), (-1, 1))

    def test_normal_only_positive_integers(self):
        self.assertEqual(largest_smallest_integers([2, 4, 1, 3, 5, 7]), (None, 1))

    def test_normal_only_negative_integers(self):
        self.assertEqual(largest_smallest_integers([-1, -5, -10, -2]), (-1, None))

    # Edge Cases
    def test_edge_empty_list(self):
        self.assertEqual(largest_smallest_integers([]), (None, None))

    def test_edge_list_with_only_zero(self):
        self.assertEqual(largest_smallest_integers([0]), (None, None))

    def test_edge_single_negative_integer(self):
        self.assertEqual(largest_smallest_integers([-1]), (-1, None))

    def test_edge_single_positive_integer(self):
        self.assertEqual(largest_smallest_integers([1]), (None, 1))

    def test_edge_list_with_zero_and_extremes(self):
        self.assertEqual(largest_smallest_integers([-5, 0, 5]), (-5, 5))

    def test_edge_smallest_negative_and_smallest_positive(self):
        self.assertEqual(largest_smallest_integers([-1, 1]), (-1, 1))

    # Error Cases
    def test_error_input_is_none(self):
        with self.assertRaises(TypeError):
            largest_smallest_integers(None)

    def test_error_input_is_not_list(self):
        with self.assertRaises(TypeError):
            largest_smallest_integers(123)

    def test_error_list_contains_float(self):
        with self.assertRaises(TypeError):
            largest_smallest_integers([1, 2.5, 3])

    def test_error_list_contains_string(self):
        with self.assertRaises(TypeError):
            largest_smallest_integers([1, "a", 3])