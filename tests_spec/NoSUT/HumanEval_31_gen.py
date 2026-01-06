import unittest
from sut.problem_HumanEval_31 import is_prime

class Test_is_prime(unittest.TestCase):
    def test_normal_prime_101(self):
        # A typical prime number.
        self.assertTrue(is_prime(101))

    def test_normal_prime_11(self):
        # Another typical prime number.
        self.assertTrue(is_prime(11))

    def test_normal_prime_13441(self):
        # A larger prime number.
        self.assertTrue(is_prime(13441))

    def test_normal_composite_6(self):
        # A typical composite number (2*3).
        self.assertFalse(is_prime(6))

    def test_normal_composite_4(self):
        # A small composite number (2*2).
        self.assertFalse(is_prime(4))

    def test_edge_one_is_not_prime(self):
        # The number 1 is not considered prime by definition.
        self.assertFalse(is_prime(1))

    def test_edge_two_is_smallest_prime(self):
        # The smallest prime number.
        self.assertTrue(is_prime(2))

    def test_edge_zero_is_not_prime(self):
        # Zero is not a prime number.
        self.assertFalse(is_prime(0))

    def test_edge_negative_number_not_prime(self):
        # Negative numbers are not prime.
        self.assertFalse(is_prime(-5))

    def test_error_float_input(self):
        # Input is not an integer.
        with self.assertRaises(TypeError):
            is_prime(3.14)

    def test_error_string_input(self):
        # Input is not an integer.
        with self.assertRaises(TypeError):
            is_prime('hello')