import unittest
import sut.problem_HumanEval_25 as mod

class TestHybrid(unittest.TestCase):
    def test_smallest_prime(self):
            # Boundary test: smallest prime number (2)
            self.assertListEqual(mod.factorize(2), [2])

    def test_power_of_smallest_prime(self):
            # Boundary test: power of the smallest prime, tests repeated factors and loop termination
            self.assertListEqual(mod.factorize(8), [2, 2, 2])

    def test_product_of_distinct_primes(self):
            # Typical input: product of multiple distinct primes, verifies order
            self.assertListEqual(mod.factorize(70), [2, 5, 7])

    def test_power_of_another_prime(self):
            # Typical input: power of a different prime, tests repeated factors
            self.assertListEqual(mod.factorize(25), [5, 5])

    def test_prime_number(self):
            # Edge case: a prime number itself, should return a list with just that prime
            self.assertListEqual(mod.factorize(7), [7])

    def test_number_one(self):
            # Edge case: 1 has no prime factors, should return an empty list
            self.assertListEqual(mod.factorize(1), [])

    def test_product_of_repeated_and_distinct_primes(self):
            # Extreme input: combines repeated and distinct factors, verifies order and multiplicity
            self.assertListEqual(mod.factorize(12), [2, 2, 3])

    def test_large_prime(self):
            # Extreme input: a relatively large prime number, tests efficiency for primes
            self.assertListEqual(mod.factorize(97), [97])

    def test_large_composite_number(self):
            # Extreme input: a large composite number with multiple factors, tests full factorization
            self.assertListEqual(mod.factorize(100), [2, 2, 5, 5])

    def test_off_by_one_from_prime(self):
            # Off-by-one test: number just below a prime, tests distinct factors
            self.assertListEqual(mod.factorize(6), [2, 3])

    def test_normal_eight(self):
            self.assertEqual(mod.factorize(8), [2, 2, 2])

    def test_normal_twenty_five(self):
            self.assertEqual(mod.factorize(25), [5, 5])

    def test_normal_seventy(self):
            self.assertEqual(mod.factorize(70), [2, 5, 7])
    
        # Edge cases

    def test_edge_one(self):
            self.assertEqual(mod.factorize(1), [])

    def test_edge_prime_two(self):
            self.assertEqual(mod.factorize(2), [2])

    def test_edge_prime_seventeen(self):
            self.assertEqual(mod.factorize(17), [17])

    def test_edge_perfect_square_four(self):
            self.assertEqual(mod.factorize(4), [2, 2])

    def test_edge_large_prime(self):
            self.assertEqual(mod.factorize(997), [997])
    
        # Error cases

    def test_error_negative(self):
            # Precondition: n must be greater than or equal to 1
            with self.assertRaises(ValueError):
                mod.factorize(-5)

    def test_error_string(self):
            # Precondition: n must be an integer
            with self.assertRaises(TypeError):
                mod.factorize("abc")

