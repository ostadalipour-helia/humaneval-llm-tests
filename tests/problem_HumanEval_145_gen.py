import unittest
from sut.problem_HumanEval_145 import order_by_points

class TestOrderByPoints(unittest.TestCase):

    def test_01_docstring_example_interpreted(self):
        # Test case derived from the docstring example, strictly following the textual description:
        # Primary sort key: sum of digits (absolute value), ascending.
        # Secondary sort key: original index, ascending (for stable sort).
        # Input: [1, 11, -1, -11, -12]
        # (value, sum_digits, original_index) pairs:
        # (1, 1, 0)
        # (11, 2, 1)
        # (-1, 1, 2)
        # (-11, 2, 3)
        # (-12, 3, 4)
        # Sorted by (sum_digits, original_index):
        # (1, 1, 0) -> 1
        # (-1, 1, 2) -> -1
        # (11, 2, 1) -> 11
        # (-11, 2, 3) -> -11
        # (-12, 3, 4) -> -12
        self.assertListEqual(order_by_points([1, 11, -1, -11, -12]), [1, -1, 11, -11, -12])

    def test_02_empty_list_edge_case(self):
        # Edge case: an empty list should return an empty list.
        self.assertListEqual(order_by_points([]), [])

    def test_03_single_element_list_edge_case(self):
        # Edge case: a list with a single element should return the same list.
        self.assertListEqual(order_by_points([42]), [42])

    def test_04_all_same_digit_sum_positive_boundary(self):
        # Boundary condition: all numbers have the same digit sum (e.g., 1).
        # This heavily tests the secondary sort key (original index).
        # Input: [10, 1, 100, 1000] (all sum to 1)
        # Expected: original order preserved due to identical sums and ascending original indices.
        self.assertListEqual(order_by_points([10, 1, 100, 1000]), [10, 1, 100, 1000])

    def test_05_mixed_signs_zero_and_varying_sums(self):
        # Typical input: a mix of positive, negative, and zero values with different digit sums.
        # Input: [0, -5, 15, -10, 2]
        # (value, sum_digits, original_index) pairs:
        # (0, 0, 0), (-5, 5, 1), (15, 6, 2), (-10, 1, 3), (2, 2, 4)
        # Sorted: (0,0,0), (-10,1,3), (2,2,4), (-5,5,1), (15,6,2)
        self.assertListEqual(order_by_points([0, -5, 15, -10, 2]), [0, -10, 2, -5, 15])

    def test_06_digit_sum_transition_boundary_and_off_by_one(self):
        # Boundary condition: numbers where digit sums change significantly (e.g., 9 vs 10, 19 vs 20).
        # This helps catch off-by-one errors in digit sum calculation.
        # Input: [9, 10, 19, 20]
        # (value, sum_digits, original_index) pairs:
        # (9, 9, 0), (10, 1, 1), (19, 10, 2), (20, 2, 3)
        # Sorted: (10,1,1), (20,2,3), (9,9,0), (19,10,2)
        self.assertListEqual(order_by_points([9, 10, 19, 20]), [10, 20, 9, 19])

    def test_07_all_same_digit_sum_negative_boundary(self):
        # Boundary condition: all negative numbers with the same digit sum.
        # Tests correct handling of negative numbers and index tie-breaking.
        # Input: [-1, -10, -100, -1000] (all sum to 1)
        # Expected: original order preserved.
        self.assertListEqual(order_by_points([-1, -10, -100, -1000]), [-1, -10, -100, -1000])

    def test_08_large_numbers_and_complex_sums_extreme(self):
        # Extreme input: large numbers with varying digit sums and mixed signs.
        # Tests robustness with larger inputs and potential for larger digit sums.
        # Input: [99, -101, 1234, -567]
        # (value, sum_digits, original_index) pairs:
        # (99, 18, 0), (-101, 2, 1), (1234, 10, 2), (-567, 18, 3)
        # Sorted: (-101,2,1), (1234,10,2), (99,18,0), (-567,18,3)
        self.assertListEqual(order_by_points([99, -101, 1234, -567]), [-101, 1234, 99, -567])

    def test_09_duplicate_values_mixed_sums_logic_mutation(self):
        # Logic mutation: list with duplicate values, some having the same digit sum, others different.
        # Ensures stable sorting behavior for duplicates.
        # Input: [1, 11, 1, 2, 11]
        # (value, sum_digits, original_index) pairs:
        # (1, 1, 0), (11, 2, 1), (1, 1, 2), (2, 2, 3), (11, 2,