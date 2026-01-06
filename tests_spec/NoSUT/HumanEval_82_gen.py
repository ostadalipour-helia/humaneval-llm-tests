import unittest
from sut.problem_HumanEval_82 import prime_length

class Test_prime_length(unittest.TestCase):
    def test_normal_prime_length_5(self):
        # Length is 5, which is a prime number.
        self.assertTrue(prime_length('Hello'))

    def test_normal_not_prime_length_6(self):
        # Length is 6, which is not a prime number.
        self.assertFalse(prime_length('orange'))

    def test_normal_prime_length_7(self):
        # Length is 7, which is a prime number.
        self.assertTrue(prime_length('abcdcba'))

    def test_edge_empty_string(self):
        # Length is 0. 0 is not a prime number.
        self.assertFalse(prime_length(''))

    def test_edge_single_character_string(self):
        # Length is 1. 1 is not a prime number.
        self.assertFalse(prime_length('a'))

    def test_edge_smallest_prime_length_2(self):
        # Length is 2. 2 is the smallest prime number.
        self.assertTrue(prime_length('ab'))

    def test_edge_large_prime_length_13(self):
        # Length is 13, which is a prime number.
        self.assertTrue(prime_length('abcdefghijklm'))

    def test_edge_large_not_prime_length_14(self):
        # Length is 14, which is not a prime number.
        self.assertFalse(prime_length('abcdefghijklmn'))

    def test_edge_special_chars_not_prime_length_4(self):
        # Length is 4, which is not a prime number. Content of string does not affect primality of length.
        self.assertFalse(prime_length('!@#$'))

    def test_error_integer_input(self):
        # Input is an integer, not a string.
        with self.assertRaises(TypeError):
            prime_length(123)

    def test_error_none_input(self):
        # Input is None, not a string.
        with self.assertRaises(TypeError):
            prime_length(None)

    def test_error_list_input(self):
        # Input is a list, not a string.
        with self.assertRaises(TypeError):
            prime_length([1, 2, 3])