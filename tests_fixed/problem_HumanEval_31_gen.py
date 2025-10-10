import unittest
from sut_llm.problem_HumanEval_31 import is_prime

class TestIsPrime(unittest.TestCase):

    def test_boundary_one(self):
        """Test with the number 1, which is explicitly not prime."""
        self.assertEqual(is_prime(1), False)

    def test_boundary_zero(self):
        """Test with 0, a number less than 1, which should not be prime."""
        self.assertEqual(is_prime(0), False)

    def test_boundary_negative(self):
        """Test with a negative number, which should not be prime."""
        self.assertEqual(is_prime(-7), False)

    def test_smallest_prime_two(self):
        """Test with 2, the smallest prime number. Critical for loop boundaries."""
        self.assertEqual(is_prime(2), True)

    def test_prime_three(self):
        """Test with 3, the next prime number, an off-by-one from 2."""
        self.assertEqual(is_prime(3), True)

    def test_smallest_composite_four(self):
        """Test with 4, the smallest composite number. Critical for loop conditions."""
        self.assertEqual(is_prime(4), False)

    def test_typical_prime_eleven(self):
        """Test with a typical prime number from the docstring."""
        self.assertEqual(is_prime(11), True)

    def test_typical_composite_six(self):
        """Test with a typical composite number from the docstring."""
        self.assertEqual(is_prime(6), False)

    def test_large_prime_13441(self):
        """Test with a large prime number from the docstring, for performance and correctness."""
        self.assertEqual(is_prime(13441), True)

    def test_large_composite_product_of_two_primes(self):
        """Test with a large composite number (7 * 13 = 91) to catch factorization issues."""
        self.assertEqual(is_prime(91), False)