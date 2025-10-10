import unittest
from sut.problem_HumanEval_75 import is_multiply_prime

class TestIsMultiplyPrime(unittest.TestCase):

    def test_example_case(self):
        self.assertTrue(is_multiply_prime(30))

    def test_valid_case_two_three_seven(self):
        self.assertTrue(is_multiply_prime(42))

    def test_valid_case_two_five_seven(self):
        self.assertTrue(is_multiply_prime(70))

    def test_valid_case_two_three_eleven(self):
        self.assertTrue(is_multiply_prime(66))

    def test_valid_case_two_three_thirteen(self):
        self.assertTrue(is_multiply_prime(78))

    def test_one_is_not_multiply_prime(self):
        self.assertFalse(is_multiply_prime(1))

    def test_prime_number_is_not_multiply_prime(self):
        self.assertFalse(is_multiply_prime(2))

    def test_product_of_two_primes_is_not_multiply_prime(self):
        self.assertFalse(is_multiply_prime(6))

    def test_product_of_three_non_distinct_primes_is_not_multiply_prime_1(self):
        self.assertFalse(is_multiply_prime(8))

    def test_product_of_three_non_distinct_primes_is_not_multiply_prime_2(self):
        self.assertFalse(is_multiply_prime(99))

if __name__ == '__main__':
    unittest.main()