import unittest
from sut.problem_HumanEval_30 import get_positive

class TestGetPositive(unittest.TestCase):

    def test_docstring_example_1(self):
        # Verifies the first example from the docstring.
        self.assertListEqual(get_positive([-1, 2, -4, 5, 6]), [2, 5, 6])

    def test_docstring_example_2(self):
        # Verifies the second example from the docstring.
        self.assertListEqual(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), [5, 3, 2, 3, 9, 123, 1])

    def test_empty_input_list(self):
        # Edge case: an empty list should return an empty list.
        self.assertListEqual(get_positive([]), [])

    def test_list_with_only_zeros(self):
        # Boundary case: a list containing only zeros.
        # Catches mutations like `x >= 0`.
        self.assertListEqual(get_positive([0, 0, 0, 0]), [])

    def test_list_with_only_negative_numbers(self):
        # Edge case: a list containing only negative numbers.
        # Catches mutations like `x <= 0` or `x < 0`.
        self.assertListEqual(get_positive([-10, -5, -1, -100]), [])

    def test_list_with_only_positive_numbers(self):
        # Edge case: a list containing only positive numbers.
        # Catches mutations like `x <= 0` or `x < 0`.
        self.assertListEqual(get_positive([1, 5, 10, 100]), [1, 5, 10, 100])

    def test_boundary_values_around_zero(self):
        # Boundary testing: includes numbers exactly at, one below, and one above zero.
        # Crucial for `x > 0` vs `x >= 0` or `x != 0` mutations.
        self.assertListEqual(get_positive([-2, -1, 0, 1, 2]), [1, 2])

    def test_large_and_small_integers(self):
        # Extreme/unusual inputs: very large and very small integers, mixed with boundary values.
        self.assertListEqual(get_positive([10**9, -10**9, 0, 1, -1, 5]), [10**9, 1, 5])

    def test_float_numbers_and_zero_point_five(self):
        # Extreme/unusual inputs: includes float numbers, including those close to zero.
        # Tests boundary conditions for floats (e.g., 0.0, 0.5, -0.5).
        self.assertListEqual(get_positive([0.5, -0.5, 0.0, 1.0, -1.0, 2.5, -0.001, 0.001]), [0.5, 1.0, 2.5, 0.001])

    def test_duplicates_and_order_preservation(self):
        # Logic mutation test: ensures duplicates are preserved and original order is maintained for positive numbers.
        self.assertListEqual(get_positive([1, -1, 2, 0, 1, 3, -3, 2]), [1, 2, 1, 3, 2])