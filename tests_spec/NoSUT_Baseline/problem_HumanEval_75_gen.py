import unittest
import sut.problem_HumanEval_75 as mod

class TestHybrid(unittest.TestCase):
    def test_smallest_valid_product_distinct(self):
            self.assertEqual(mod.is_multiply_prime(30), True) # 2 * 3 * 5
    
        # Test 2: Largest number < 100 that is a product of 3 distinct primes (Boundary, Extreme)

    def test_largest_valid_product_distinct(self):
            self.assertEqual(mod.is_multiply_prime(78), True) # 2 * 3 * 13
    
        # Test 3: Edge case: Input is 1 (no prime factors)

    def test_one_as_input(self):
            self.assertEqual(mod.is_multiply_prime(1), False)
    
        # Test 4: Edge case: Input is a prime number (1 prime factor, Off-by-one)

    def test_prime_number_input(self):
            self.assertEqual(mod.is_multiply_prime(7), False)
    
        # Test 5: Off-by-one: Product of exactly two prime numbers

    def test_product_of_two_primes(self):
            self.assertEqual(mod.is_multiply_prime(6), False) # 2 * 3
    
        # Test 6: Logic Mutation: Product of three primes, two of which are identical

    def test_product_of_three_primes_two_identical(self):
            self.assertEqual(mod.is_multiply_prime(12), True) # 2 * 2 * 3
    
        # Test 7: Logic Mutation: Product of three identical primes

    def test_product_of_three_identical_primes(self):
            self.assertEqual(mod.is_multiply_prime(8), True) # 2 * 2 * 2
    
        # Test 8: Off-by-one: Product of four prime numbers

    def test_product_of_four_primes(self):
            self.assertEqual(mod.is_multiply_prime(60), False) # 2 * 2 * 3 * 5
    
        # Test 9: Extreme input: Largest prime number less than 100 (Boundary, Edge)

    def test_largest_prime_below_100(self):
            self.assertEqual(mod.is_multiply_prime(97), False)
    
        # Test 10: Extreme input: Largest number < 100 that is a product of 3 primes, non-distinct (Boundary, Typical, Logic Mutation)

    def test_largest_valid_product_non_distinct(self):
            self.assertEqual(mod.is_multiply_prime(99), True) # 3 * 3 * 11

    def test_normal_case_30(self):
            # 30 = 2 * 3 * 5 (product of 3 distinct primes)
            self.assertTrue(mod.is_multiply_prime(30))

    def test_normal_case_42(self):
            # 42 = 2 * 3 * 7 (product of 3 distinct primes)
            self.assertTrue(mod.is_multiply_prime(42))

    def test_normal_case_not_multiply_prime_10(self):
            # 10 = 2 * 5 (product of only 2 primes)
            self.assertFalse(mod.is_multiply_prime(10))

    def test_normal_case_prime_number_97(self):
            # 97 is a prime number, not a product of 3 primes.
            self.assertFalse(mod.is_multiply_prime(97))

    def test_edge_case_zero(self):
            # 0 is not a product of prime numbers.
            self.assertFalse(mod.is_multiply_prime(0))

    def test_edge_case_one(self):
            # 1 is not a product of prime numbers.
            self.assertFalse(mod.is_multiply_prime(1))

    def test_edge_case_largest_valid_multiply_prime_78(self):
            # 78 = 2 * 3 * 13 (largest number < 100 that is a product of 3 distinct primes)
            self.assertTrue(mod.is_multiply_prime(78))

    def test_edge_case_just_below_smallest_multiply_prime_29(self):
            # Smallest product of 3 distinct primes is 30. 29 is prime and less than 30.
            self.assertFalse(mod.is_multiply_prime(29))

    def test_error_case_input_equals_100(self):
            # Input `a` must be strictly less than 100.
            # As per spec, returning False is an acceptable behavior for this boundary violation.
            self.assertFalse(mod.is_multiply_prime(100))

    def test_error_case_negative_input(self):
            # Input `a` must be greater than or equal to 0.
            # As per spec, returning False is an acceptable behavior for this boundary violation.
            self.assertFalse(mod.is_multiply_prime(-5))

