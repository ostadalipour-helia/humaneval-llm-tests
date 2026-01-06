import unittest
import sut.problem_HumanEval_31 as mod

class TestHybrid(unittest.TestCase):
    def test_boundary_one(self):
            """Test with the number 1, which is explicitly not prime."""
            self.assertEqual(mod.is_prime(1), False)

    def test_boundary_zero(self):
            """Test with 0, a number less than 1, which should not be prime."""
            self.assertEqual(mod.is_prime(0), False)

    def test_boundary_negative(self):
            """Test with a negative number, which should not be prime."""
            self.assertEqual(mod.is_prime(-7), False)

    def test_smallest_prime_two(self):
            """Test with 2, the smallest prime number. Critical for loop boundaries."""
            self.assertEqual(mod.is_prime(2), True)

    def test_prime_three(self):
            """Test with 3, the next prime number, an off-by-one from 2."""
            self.assertEqual(mod.is_prime(3), True)

    def test_smallest_composite_four(self):
            """Test with 4, the smallest composite number. Critical for loop conditions."""
            self.assertEqual(mod.is_prime(4), False)

    def test_typical_prime_eleven(self):
            """Test with a typical prime number from the docstring."""
            self.assertEqual(mod.is_prime(11), True)

    def test_typical_composite_six(self):
            """Test with a typical composite number from the docstring."""
            self.assertEqual(mod.is_prime(6), False)

    def test_large_prime_13441(self):
            """Test with a large prime number from the docstring, for performance and correctness."""
            self.assertEqual(mod.is_prime(13441), True)

    def test_large_composite_product_of_two_primes(self):
            """Test with a large composite number (7 * 13 = 91) to catch factorization issues."""
            self.assertEqual(mod.is_prime(91), False)

    def test_normal_prime_101(self):
            # A typical prime number.
            self.assertTrue(mod.is_prime(101))

    def test_normal_prime_11(self):
            # Another typical prime number.
            self.assertTrue(mod.is_prime(11))

    def test_normal_prime_13441(self):
            # A larger prime number.
            self.assertTrue(mod.is_prime(13441))

    def test_normal_composite_6(self):
            # A typical composite number (2*3).
            self.assertFalse(mod.is_prime(6))

    def test_normal_composite_4(self):
            # A small composite number (2*2).
            self.assertFalse(mod.is_prime(4))

    def test_edge_one_is_not_prime(self):
            # The number 1 is not considered prime by definition.
            self.assertFalse(mod.is_prime(1))

    def test_edge_two_is_smallest_prime(self):
            # The smallest prime number.
            self.assertTrue(mod.is_prime(2))

    def test_edge_zero_is_not_prime(self):
            # Zero is not a prime number.
            self.assertFalse(mod.is_prime(0))

    def test_edge_negative_number_not_prime(self):
            # Negative numbers are not prime.
            self.assertFalse(mod.is_prime(-5))

    def test_error_float_input(self):
            # Input is not an integer.
            with self.assertRaises(TypeError):
                mod.is_prime(3.14)

    def test_error_string_input(self):
            # Input is not an integer.
            with self.assertRaises(TypeError):
                mod.is_prime('hello')

