import unittest
from sut.problem_HumanEval_24 import largest_divisor

class Test_largest_divisor(unittest.TestCase):
    def test_normal_composite_15(self):
        # Normal case: A composite number, finding its largest proper divisor.
        self.assertEqual(largest_divisor(15), 5)

    def test_normal_composite_10(self):
        # Normal case: Another composite number.
        self.assertEqual(largest_divisor(10), 5)

    def test_normal_composite_12(self):
        # Normal case: A composite number with multiple divisors.
        self.assertEqual(largest_divisor(12), 6)

    def test_edge_smallest_prime_2(self):
        # Edge case: The smallest valid input number (prime).
        self.assertEqual(largest_divisor(2), 1)

    def test_edge_prime_7(self):
        # Edge case: A prime number, its only divisor smaller than itself is 1.
        self.assertEqual(largest_divisor(7), 1)

    def test_edge_perfect_square_4(self):
        # Edge case: A perfect square.
        self.assertEqual(largest_divisor(4), 2)

    def test_edge_power_of_2_8(self):
        # Edge case: A power of 2.
        self.assertEqual(largest_divisor(8), 4)

    def test_error_n_is_1(self):
        # Error case: Input 'n' is 1, violating the 'n > 1' precondition.
        with self.assertRaises(ValueError):
            largest_divisor(1)

    def test_error_n_is_0(self):
        # Error case: Input 'n' is 0, violating the 'n > 1' precondition.
        with self.assertRaises(ValueError):
            largest_divisor(0)

    def test_error_n_is_negative(self):
        # Error case: Input 'n' is a negative integer.
        with self.assertRaises(ValueError):
            largest_divisor(-5)

    def test_error_n_is_float(self):
        # Error case: Input 'n' is a float.
        with self.assertRaises(TypeError):
            largest_divisor(15.5)

    def test_error_n_is_string(self):
        # Error case: Input 'n' is a string.
        with self.assertRaises(TypeError):
            largest_divisor('abc')