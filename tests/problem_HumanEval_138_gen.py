import unittest
from sut.problem_HumanEval_138 import is_equal_to_sum_even

class TestIsEqualToSumEven(unittest.TestCase):

    def test_minimum_true_case(self):
        # Boundary test: Smallest number that can be a sum of 4 positive even numbers (2+2+2+2=8)
        # Also an edge case for the lower bound of 'True' results.
        self.assertEqual(is_equal_to_sum_even(8), True)

    def test_one_below_minimum_true_case_odd(self):
        # Boundary test: One less than the minimum true case, and it's odd.
        # Catches off-by-one errors and logic mutations (e.g., changing >= to > or issues with odd numbers).
        self.assertEqual(is_equal_to_sum_even(7), False)

    def test_one_below_minimum_true_case_even(self):
        # Boundary test: One less than the minimum true case, and it's even.
        # Catches off-by-one errors and logic mutations (e.g., changing >= to >).
        self.assertEqual(is_equal_to_sum_even(6), False)

    def test_typical_even_number(self):
        # Typical input: A common even number well above the boundary.
        self.assertEqual(is_equal_to_sum_even(10), True)

    def test_typical_odd_number_above_boundary(self):
        # Logic mutation test: Number is >= 8 but is odd.
        # Verifies the 'even' condition is correctly applied.
        self.assertEqual(is_equal_to_sum_even(9), False)

    def test_zero_input(self):
        # Edge case: Zero input.
        # Tests handling of non-positive numbers.
        self.assertEqual(is_equal_to_sum_even(0), False)

    def test_negative_even_input(self):
        # Edge case: Negative even number.
        # Tests handling of negative numbers.
        self.assertEqual(is_equal_to_sum_even(-2), False)

    def test_large_even_number(self):
        # Extreme input: A very large even number.
        # Checks scalability and ensures logic holds for large values.
        self.assertEqual(is_equal_to_sum_even(1000000), True)

    def test_large_odd_number(self):
        # Extreme input: A very large odd number.
        # Checks scalability and ensures odd numbers are correctly rejected even if large.
        self.assertEqual(is_equal_to_sum_even(1000001), False)

    def test_another_small_even_false_case(self):
        # Edge case: Another small even number that should be false.
        # Reinforces the lower bound for 'True' results.
        self.assertEqual(is_equal_to_sum_even(4), False)