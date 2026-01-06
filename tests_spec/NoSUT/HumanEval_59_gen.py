import unittest
from sut.problem_HumanEval_59 import largest_prime_factor

class Test_largest_prime_factor(unittest.TestCase):
    def test_normal_multiple_distinct_factors(self):
        # n = 13195, expected_output = 29
        # Comment: A number with multiple distinct prime factors.
        self.assertEqual(largest_prime_factor(13195), 29)

    def test_normal_power_of_two(self):
        # n = 2048, expected_output = 2
        # Comment: A number that is a power of a single prime factor.
        self.assertEqual(largest_prime_factor(2048), 2)

    def test_normal_mixed_factors(self):
        # n = 100, expected_output = 5
        # Comment: A number with multiple prime factors, where the largest is not the smallest.
        self.assertEqual(largest_prime_factor(100), 5)

    def test_edge_smallest_composite(self):
        # n = 4, expected_output = 2
        # Comment: The smallest composite number (n > 1 and not prime).
        self.assertEqual(largest_prime_factor(4), 2)

    def test_edge_power_of_odd_prime(self):
        # n = 81, expected_output = 3
        # Comment: A power of an odd prime.
        self.assertEqual(largest_prime_factor(81), 3)

    def test_edge_product_of_small_primes(self):
        # n = 210, expected_output = 7
        # Comment: Product of the first few distinct primes (2*3*5*7).
        self.assertEqual(largest_prime_factor(210), 7)

    def test_edge_large_composite(self):
        # n = 999999, expected_output = 37
        # Comment: A larger composite number with multiple prime factors (3^3 * 7 * 11 * 13 * 37).
        self.assertEqual(largest_prime_factor(999999), 37)

    def test_error_n_equals_one(self):
        # n = 1
        # Comment: Input is not greater than 1.
        # Precondition: n must be greater than 1 (n > 1).
        with self.assertRaises(ValueError):
            largest_prime_factor(1)

    def test_error_n_is_prime(self):
        # n = 7
        # Comment: Input is a prime number.
        # Precondition: n must not be a prime number.
        with self.assertRaises(ValueError):
            largest_prime_factor(7)

    def test_error_n_float(self):
        # n = 13.5
        # Comment: Input is not an integer.
        # Precondition: n must be an integer.
        with self.assertRaises(TypeError):
            largest_prime_factor(13.5)

    def test_error_n_string(self):
        # n = 'abc'
        # Comment: Input is not an integer.
        # Precondition: n must be an integer.
        with self.assertRaises(TypeError):
            largest_prime_factor('abc')