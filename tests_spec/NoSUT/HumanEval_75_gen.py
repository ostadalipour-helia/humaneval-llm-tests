import unittest
from sut.problem_HumanEval_75 import is_multiply_prime

class Test_is_multiply_prime(unittest.TestCase):

    def test_normal_case_30(self):
        # 30 = 2 * 3 * 5 (product of 3 distinct primes)
        self.assertTrue(is_multiply_prime(30))

    def test_normal_case_42(self):
        # 42 = 2 * 3 * 7 (product of 3 distinct primes)
        self.assertTrue(is_multiply_prime(42))

    def test_normal_case_not_multiply_prime_10(self):
        # 10 = 2 * 5 (product of only 2 primes)
        self.assertFalse(is_multiply_prime(10))

    def test_normal_case_not_distinct_primes_12(self):
        # 12 = 2 * 2 * 3 (product of 3 primes, but not distinct as 2 is repeated)
        self.assertFalse(is_multiply_prime(12))

    def test_normal_case_prime_number_97(self):
        # 97 is a prime number, not a product of 3 primes.
        self.assertFalse(is_multiply_prime(97))

    def test_edge_case_zero(self):
        # 0 is not a product of prime numbers.
        self.assertFalse(is_multiply_prime(0))

    def test_edge_case_one(self):
        # 1 is not a product of prime numbers.
        self.assertFalse(is_multiply_prime(1))

    def test_edge_case_largest_valid_multiply_prime_78(self):
        # 78 = 2 * 3 * 13 (largest number < 100 that is a product of 3 distinct primes)
        self.assertTrue(is_multiply_prime(78))

    def test_edge_case_just_below_smallest_multiply_prime_29(self):
        # Smallest product of 3 distinct primes is 30. 29 is prime and less than 30.
        self.assertFalse(is_multiply_prime(29))

    def test_edge_case_not_distinct_primes_99(self):
        # 99 = 3 * 3 * 11 (product of 3 primes, but not distinct)
        self.assertFalse(is_multiply_prime(99))

    def test_error_case_non_integer_input(self):
        # Input `a` must be an integer.
        with self.assertRaises(TypeError):
            is_multiply_prime("abc")

    def test_error_case_input_equals_100(self):
        # Input `a` must be strictly less than 100.
        # As per spec, returning False is an acceptable behavior for this boundary violation.
        self.assertFalse(is_multiply_prime(100))

    def test_error_case_negative_input(self):
        # Input `a` must be greater than or equal to 0.
        # As per spec, returning False is an acceptable behavior for this boundary violation.
        self.assertFalse(is_multiply_prime(-5))