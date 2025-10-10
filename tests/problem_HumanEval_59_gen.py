import unittest
from sut.problem_HumanEval_59 import largest_prime_factor

class TestLargestPrimeFactor(unittest.TestCase):

    def test_smallest_composite_number(self):
        # Boundary test: Smallest n > 1 that is not prime (n=4)
        # Catches issues with initial divisor (2) and loop termination.
        self.assertEqual(largest_prime_factor(4), 2)

    def test_smallest_composite_with_odd_largest_factor(self):
        # Boundary test: Smallest n with an odd largest prime factor (n=9)
        # Catches issues with handling odd divisors.
        self.assertEqual(largest_prime_factor(9), 3)

    def test_product_of_two_distinct_small_primes(self):
        # Typical input, boundary for number of distinct factors (n=6)
        # Catches issues with tracking the largest factor among multiple.
        self.assertEqual(largest_prime_factor(6), 3)

    def test_docstring_example_1(self):
        # Typical input, verifies example behavior
        self.assertEqual(largest_prime_factor(13195), 29)

    def test_docstring_example_2_power_of_two(self):
        # Edge case: n is a power of a single prime (n=2048 = 2^11)
        # Catches off-by-one errors in division loops for single prime factors.
        self.assertEqual(largest_prime_factor(2048), 2)

    def test_number_with_moderately_large_prime_factor(self):
        # Typical/Extreme input: n = 7 * 11 = 77
        # Ensures the algorithm correctly identifies a larger prime factor after a smaller one.
        self.assertEqual(largest_prime_factor(77), 11)

    def test_product_of_many_small_distinct_primes(self):
        # Logic mutation test: n = 2 * 3 * 5 * 7 = 210
        # Verifies that the largest factor is correctly identified when many small factors exist.
        self.assertEqual(largest_prime_factor(210), 7)

    def test_large_number_with_large_prime_factor(self):
        # Extreme input: n = 2^2 * 5^2 * 97 = 4 * 25 * 97 = 100 * 97 = 9700
        # Tests performance and correctness for larger numbers and larger prime factors.
        self.assertEqual(largest_prime_factor(9700), 97)

    def test_product_of_two_larger_primes(self):
        # Boundary/Extreme input: n = 17 * 19 = 323
        # Tests handling of larger prime factors without many small initial divisions.
        self.assertEqual(largest_prime_factor(323), 19)

    def test_number_with_repeated_small_factors_then_a_larger_one(self):
        # Off-by-one/Logic test: n = 2^3 * 3^2 * 17 = 8 * 9 * 17 = 1224
        # Ensures the algorithm fully divides by smaller primes before checking larger ones,
        # and correctly identifies the largest remaining factor.
        self.assertEqual(largest_prime_factor(1224), 17)

if __name__ == '__main__':
    unittest.main()