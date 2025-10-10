import unittest
from sut.problem_HumanEval_13 import greatest_common_divisor

class TestGreatestCommonDivisor(unittest.TestCase):

    def test_docstring_example_1_coprime(self):
        # Typical case: two coprime positive integers
        self.assertEqual(greatest_common_divisor(3, 5), 1)

    def test_docstring_example_2_common_factor(self):
        # Typical case: two positive integers with a common factor
        self.assertEqual(greatest_common_divisor(25, 15), 5)

    def test_boundary_one_is_zero(self):
        # Boundary case: one input is zero. GCD(a, 0) = |a|.
        self.assertEqual(greatest_common_divisor(10, 0), 10)
        self.assertEqual(greatest_common_divisor(0, 7), 7)

    def test_boundary_both_are_zero(self):
        # Edge case: both inputs are zero. GCD(0, 0) is often defined as 0.
        self.assertEqual(greatest_common_divisor(0, 0), 0)

    def test_edge_one_is_one(self):
        # Edge case: one input is one. GCD(a, 1) = 1.
        self.assertEqual(greatest_common_divisor(7, 1), 1)
        self.assertEqual(greatest_common_divisor(1, 100), 1)

    def test_edge_numbers_are_equal(self):
        # Edge case: both inputs are the same. GCD(a, a) = |a|.
        self.assertEqual(greatest_common_divisor(12, 12), 12)
        self.assertEqual(greatest_common_divisor(-5, -5), 5) # GCD is usually positive

    def test_extreme_both_negative(self):
        # Extreme case: both inputs are negative. GCD(|a|, |b|).
        self.assertEqual(greatest_common_divisor(-25, -15), 5)

    def test_extreme_one_negative(self):
        # Extreme case: one input is negative. GCD(|a|, |b|).
        self.assertEqual(greatest_common_divisor(-12, 18), 6)
        self.assertEqual(greatest_common_divisor(20, -30), 10)

    def test_logic_one_is_multiple_of_other(self):
        # Logic test: one number is a multiple of the other.
        # This tests the termination condition of Euclidean algorithm.
        self.assertEqual(greatest_common_divisor(100, 10), 10)
        self.assertEqual(greatest_common_divisor(77, 11), 11)

    def test_large_numbers(self):
        # Extreme case: large numbers to test efficiency and correctness with larger values.
        # GCD(1000000, 750000) = GCD(2^6 * 5^6, 2^4 * 3 * 5^6) = 2^4 * 5^6 = 16 * 15625 = 250000
        self.assertEqual(greatest_common_divisor(1000000, 750000), 250000)