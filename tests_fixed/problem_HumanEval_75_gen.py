import unittest
from sut_llm.problem_HumanEval_75 import is_multiply_prime

class TestIsMultiplyPrime(unittest.TestCase):

    # Test 1: Smallest number that is a product of 3 distinct primes (Boundary, Typical)
    def test_smallest_valid_product_distinct(self):
        self.assertEqual(is_multiply_prime(30), True) # 2 * 3 * 5

    # Test 2: Largest number < 100 that is a product of 3 distinct primes (Boundary, Extreme)
    def test_largest_valid_product_distinct(self):
        self.assertEqual(is_multiply_prime(78), True) # 2 * 3 * 13

    # Test 3: Edge case: Input is 1 (no prime factors)
    def test_one_as_input(self):
        self.assertEqual(is_multiply_prime(1), False)

    # Test 4: Edge case: Input is a prime number (1 prime factor, Off-by-one)
    def test_prime_number_input(self):
        self.assertEqual(is_multiply_prime(7), False)

    # Test 5: Off-by-one: Product of exactly two prime numbers
    def test_product_of_two_primes(self):
        self.assertEqual(is_multiply_prime(6), False) # 2 * 3

    # Test 6: Logic Mutation: Product of three primes, two of which are identical
    def test_product_of_three_primes_two_identical(self):
        self.assertEqual(is_multiply_prime(12), True) # 2 * 2 * 3

    # Test 7: Logic Mutation: Product of three identical primes
    def test_product_of_three_identical_primes(self):
        self.assertEqual(is_multiply_prime(8), True) # 2 * 2 * 2

    # Test 8: Off-by-one: Product of four prime numbers
    def test_product_of_four_primes(self):
        self.assertEqual(is_multiply_prime(60), False) # 2 * 2 * 3 * 5

    # Test 9: Extreme input: Largest prime number less than 100 (Boundary, Edge)
    def test_largest_prime_below_100(self):
        self.assertEqual(is_multiply_prime(97), False)

    # Test 10: Extreme input: Largest number < 100 that is a product of 3 primes, non-distinct (Boundary, Typical, Logic Mutation)
    def test_largest_valid_product_non_distinct(self):
        self.assertEqual(is_multiply_prime(99), True) # 3 * 3 * 11