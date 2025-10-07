import unittest
from sut_llm.problem_HumanEval_59 import largest_prime_factor

class TestLargestPrimeFactor(unittest.TestCase):

    def test_example_one(self):
        # Test case from the docstring
        self.assertEqual(largest_prime_factor(13195), 29)

    def test_example_two(self):
        # Test case from the docstring (power of 2)
        self.assertEqual(largest_prime_factor(2048), 2)

    def test_smallest_composite(self):
        # Test with the smallest composite number
        self.assertEqual(largest_prime_factor(4), 2)

    def test_product_of_two_primes(self):
        # Test with a product of two distinct primes
        self.assertEqual(largest_prime_factor(6), 3)

    def test_product_of_two_odd_primes(self):
        # Test with a product of two distinct odd primes
        self.assertEqual(largest_prime_factor(15), 5)

    def test_product_of_three_primes(self):
        # Test with a product of three distinct primes
        self.assertEqual(largest_prime_factor(30), 5)

    def test_number_with_repeated_factors(self):
        # Test with a number having repeated prime factors (e.g., 2^2 * 5^2)
        self.assertEqual(largest_prime_factor(100), 5)

    def test_larger_number_with_larger_prime_factor(self):
        # Test with a larger number and a larger prime factor
        self.assertEqual(largest_prime_factor(999), 37) # 3^3 * 37

    def test_number_with_repeated_odd_factors(self):
        # Test with a number having repeated odd prime factors (e.g., 3 * 5^2)
        self.assertEqual(largest_prime_factor(75), 5)

    def test_product_of_two_larger_primes(self):
        # Test with a product of two relatively larger primes
        self.assertEqual(largest_prime_factor(143), 13) # 11 * 13

if __name__ == '__main__':
    unittest.main()