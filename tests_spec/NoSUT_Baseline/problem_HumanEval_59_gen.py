import unittest
import sut.problem_HumanEval_59 as mod

class TestHybrid(unittest.TestCase):
    def test_smallest_composite_number(self):
            # Boundary test: Smallest n > 1 that is not prime (n=4)
            # Catches issues with initial divisor (2) and loop termination.
            self.assertEqual(mod.largest_prime_factor(4), 2)

    def test_smallest_composite_with_odd_largest_factor(self):
            # Boundary test: Smallest n with an odd largest prime factor (n=9)
            # Catches issues with handling odd divisors.
            self.assertEqual(mod.largest_prime_factor(9), 3)

    def test_product_of_two_distinct_small_primes(self):
            # Typical input, boundary for number of distinct factors (n=6)
            # Catches issues with tracking the largest factor among multiple.
            self.assertEqual(mod.largest_prime_factor(6), 3)

    def test_docstring_example_1(self):
            # Typical input, verifies example behavior
            self.assertEqual(mod.largest_prime_factor(13195), 29)

    def test_docstring_example_2_power_of_two(self):
            # Edge case: n is a power of a single prime (n=2048 = 2^11)
            # Catches off-by-one errors in division loops for single prime factors.
            self.assertEqual(mod.largest_prime_factor(2048), 2)

    def test_number_with_moderately_large_prime_factor(self):
            # Typical/Extreme input: n = 7 * 11 = 77
            # Ensures the algorithm correctly identifies a larger prime factor after a smaller one.
            self.assertEqual(mod.largest_prime_factor(77), 11)

    def test_product_of_many_small_distinct_primes(self):
            # Logic mutation test: n = 2 * 3 * 5 * 7 = 210
            # Verifies that the largest factor is correctly identified when many small factors exist.
            self.assertEqual(mod.largest_prime_factor(210), 7)

    def test_large_number_with_large_prime_factor(self):
            # Extreme input: n = 2^2 * 5^2 * 97 = 4 * 25 * 97 = 100 * 97 = 9700
            # Tests performance and correctness for larger numbers and larger prime factors.
            self.assertEqual(mod.largest_prime_factor(9700), 97)

    def test_product_of_two_larger_primes(self):
            # Boundary/Extreme input: n = 17 * 19 = 323
            # Tests handling of larger prime factors without many small initial divisions.
            self.assertEqual(mod.largest_prime_factor(323), 19)

    def test_number_with_repeated_small_factors_then_a_larger_one(self):
            # Off-by-one/Logic test: n = 2^3 * 3^2 * 17 = 8 * 9 * 17 = 1224
            # Ensures the algorithm fully divides by smaller primes before checking larger ones,
            # and correctly identifies the largest remaining factor.
            self.assertEqual(mod.largest_prime_factor(1224), 17)
    
    if __name__ == '__main__':
        unittest.main()

    def test_normal_multiple_distinct_factors(self):
            # n = 13195, expected_output = 29
            # Comment: A number with multiple distinct prime factors.
            self.assertEqual(mod.largest_prime_factor(13195), 29)

    def test_normal_power_of_two(self):
            # n = 2048, expected_output = 2
            # Comment: A number that is a power of a single prime factor.
            self.assertEqual(mod.largest_prime_factor(2048), 2)

    def test_normal_mixed_factors(self):
            # n = 100, expected_output = 5
            # Comment: A number with multiple prime factors, where the largest is not the smallest.
            self.assertEqual(mod.largest_prime_factor(100), 5)

    def test_edge_smallest_composite(self):
            # n = 4, expected_output = 2
            # Comment: The smallest composite number (n > 1 and not prime).
            self.assertEqual(mod.largest_prime_factor(4), 2)

    def test_edge_power_of_odd_prime(self):
            # n = 81, expected_output = 3
            # Comment: A power of an odd prime.
            self.assertEqual(mod.largest_prime_factor(81), 3)

    def test_edge_product_of_small_primes(self):
            # n = 210, expected_output = 7
            # Comment: Product of the first few distinct primes (2*3*5*7).
            self.assertEqual(mod.largest_prime_factor(210), 7)

    def test_edge_large_composite(self):
            # n = 999999, expected_output = 37
            # Comment: A larger composite number with multiple prime factors (3^3 * 7 * 11 * 13 * 37).
            self.assertEqual(mod.largest_prime_factor(999999), 37)

    def test_error_n_float(self):
            # n = 13.5
            # Comment: Input is not an integer.
            # Precondition: n must be an integer.
            with self.assertRaises(TypeError):
                mod.largest_prime_factor(13.5)

    def test_error_n_string(self):
            # n = 'abc'
            # Comment: Input is not an integer.
            # Precondition: n must be an integer.
            with self.assertRaises(TypeError):
                mod.largest_prime_factor('abc')

