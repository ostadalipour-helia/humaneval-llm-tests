import unittest
import sut.problem_HumanEval_145 as mod

class TestHybrid(unittest.TestCase):
    def test_02_empty_list_edge_case(self):
            # Edge case: an empty list should return an empty list.
            self.assertListEqual(mod.order_by_points([]), [])

    def test_03_single_element_list_edge_case(self):
            # Edge case: a list with a single element should return the same list.
            self.assertListEqual(mod.order_by_points([42]), [42])

    def test_04_all_same_digit_sum_positive_boundary(self):
            # Boundary condition: all numbers have the same digit sum (e.g., 1).
            # This heavily tests the secondary sort key (original index).
            # Input: [10, 1, 100, 1000] (all sum to 1)
            # Expected: original order preserved due to identical sums and ascending original indices.
            self.assertListEqual(mod.order_by_points([10, 1, 100, 1000]), [10, 1, 100, 1000])

    def test_06_digit_sum_transition_boundary_and_off_by_one(self):
            # Boundary condition: numbers where digit sums change significantly (e.g., 9 vs 10, 19 vs 20).
            # This helps catch off-by-one errors in digit sum calculation.
            # Input: [9, 10, 19, 20]
            # (value, sum_digits, original_index) pairs:
            # (9, 9, 0), (10, 1, 1), (19, 10, 2), (20, 2, 3)
            # Sorted: (10,1,1), (20,2,3), (9,9,0), (19,10,2)
            self.assertListEqual(mod.order_by_points([9, 10, 19, 20]), [10, 20, 9, 19])

    def test_07_all_same_digit_sum_negative_boundary(self):
            # Boundary condition: all negative numbers with the same digit sum.
            # Tests correct handling of negative numbers and index tie-breaking.
            # Input: [-1, -10, -100, -1000] (all sum to 1)
            # Expected: original order preserved.
            self.assertListEqual(mod.order_by_points([-1, -10, -100, -1000]), [-1, -10, -100, -1000])

    def test_normal_stability_same_sum(self):
            # Normal case: multiple numbers with the same sum of digits, stability is key
            nums = [12, 21, 3, 100]
            expected = [100, 12, 21, 3]
            self.assertEqual(mod.order_by_points(nums), expected)

    def test_normal_already_sorted(self):
            # Normal case: input is already sorted by sum of digits
            nums = [10, 20, 30]
            expected = [10, 20, 30]
            self.assertEqual(mod.order_by_points(nums), expected)

    def test_edge_empty_list(self):
            # Edge case: empty list
            nums = []
            expected = []
            self.assertEqual(mod.order_by_points(nums), expected)

    def test_edge_single_element(self):
            # Edge case: single element list
            nums = [7]
            expected = [7]
            self.assertEqual(mod.order_by_points(nums), expected)

    def test_edge_all_same_sum_stability(self):
            # Edge case: all elements have the same sum of digits, original order preserved
            nums = [1, 10, 100]
            expected = [1, 10, 100]
            self.assertEqual(mod.order_by_points(nums), expected)

    def test_edge_large_numbers(self):
            # Edge case: large numbers with different sums
            nums = [999, 1000000000000000000]
            expected = [1000000000000000000, 999]
            self.assertEqual(mod.order_by_points(nums), expected)

    def test_error_non_list_none(self):
            # Error case: input is None instead of a list
            with self.assertRaises(TypeError):
                mod.order_by_points(None)

    def test_error_non_list_int(self):
            # Error case: input is an integer instead of a list
            with self.assertRaises(TypeError):
                mod.order_by_points(123)

    def test_error_list_with_string(self):
            # Error case: list contains non-integer (string) elements
            with self.assertRaises(TypeError):
                mod.order_by_points([1, 'a', 3])

