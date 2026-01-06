import unittest
from sut.problem_HumanEval_145 import order_by_points

class Test_order_by_points(unittest.TestCase):

    def test_normal_complex_sorting(self):
        # Normal case: mixed positive/negative, multiple same sums, stability check
        nums = [1, 11, -1, -11, -12]
        expected = [1, -1, 11, -11, -12]
        self.assertEqual(order_by_points(nums), expected)

    def test_normal_stability_same_sum(self):
        # Normal case: multiple numbers with the same sum of digits, stability is key
        nums = [12, 21, 3, 100]
        expected = [100, 12, 21, 3]
        self.assertEqual(order_by_points(nums), expected)

    def test_normal_already_sorted(self):
        # Normal case: input is already sorted by sum of digits
        nums = [10, 20, 30]
        expected = [10, 20, 30]
        self.assertEqual(order_by_points(nums), expected)

    def test_edge_empty_list(self):
        # Edge case: empty list
        nums = []
        expected = []
        self.assertEqual(order_by_points(nums), expected)

    def test_edge_single_element(self):
        # Edge case: single element list
        nums = [7]
        expected = [7]
        self.assertEqual(order_by_points(nums), expected)

    def test_edge_all_same_sum_stability(self):
        # Edge case: all elements have the same sum of digits, original order preserved
        nums = [1, 10, 100]
        expected = [1, 10, 100]
        self.assertEqual(order_by_points(nums), expected)

    def test_edge_duplicates_and_negatives_stability(self):
        # Edge case: duplicates and negatives, testing stability
        nums = [1, 11, 1, -11]
        expected = [1, 1, 11, -11]
        self.assertEqual(order_by_points(nums), expected)

    def test_edge_zero_and_negatives(self):
        # Edge case: includes zero and negative numbers, testing sum of digits for 0 and stability
        nums = [0, 10, -1]
        expected = [0, 10, -1]
        self.assertEqual(order_by_points(nums), expected)

    def test_edge_large_numbers(self):
        # Edge case: large numbers with different sums
        nums = [999, 1000000000000000000]
        expected = [1000000000000000000, 999]
        self.assertEqual(order_by_points(nums), expected)

    def test_error_non_list_none(self):
        # Error case: input is None instead of a list
        with self.assertRaises(TypeError):
            order_by_points(None)

    def test_error_non_list_int(self):
        # Error case: input is an integer instead of a list
        with self.assertRaises(TypeError):
            order_by_points(123)

    def test_error_list_with_float(self):
        # Error case: list contains non-integer (float) elements
        with self.assertRaises(TypeError):
            order_by_points([1, 2.5, 3])

    def test_error_list_with_string(self):
        # Error case: list contains non-integer (string) elements
        with self.assertRaises(TypeError):
            order_by_points([1, 'a', 3])