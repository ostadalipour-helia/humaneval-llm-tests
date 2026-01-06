import unittest
import sut.problem_HumanEval_82 as mod

class TestHybrid(unittest.TestCase):
    def test_empty_string(self):
            self.assertEqual(mod.prime_length(''), False)

    def test_single_char_string(self):
            self.assertEqual(mod.prime_length('a'), False)

    def test_length_two_prime(self):
            self.assertEqual(mod.prime_length('ab'), True)

    def test_length_three_prime(self):
            self.assertEqual(mod.prime_length('abc'), True)

    def test_length_four_composite(self):
            self.assertEqual(mod.prime_length('abcd'), False)

    def test_example_hello(self):
            self.assertEqual(mod.prime_length('Hello'), True)

    def test_example_orange(self):
            self.assertEqual(mod.prime_length('orange'), False)

    def test_example_kittens(self):
            self.assertEqual(mod.prime_length('kittens'), True)

    def test_length_nine_composite(self):
            self.assertEqual(mod.prime_length('abcdefghi'), False)

    def test_length_eleven_prime(self):
            self.assertEqual(mod.prime_length('abcdefghijk'), True)

    def test_normal_prime_length_5(self):
            # Length is 5, which is a prime number.
            self.assertTrue(mod.prime_length('Hello'))

    def test_normal_not_prime_length_6(self):
            # Length is 6, which is not a prime number.
            self.assertFalse(mod.prime_length('orange'))

    def test_normal_prime_length_7(self):
            # Length is 7, which is a prime number.
            self.assertTrue(mod.prime_length('abcdcba'))

    def test_edge_empty_string(self):
            # Length is 0. 0 is not a prime number.
            self.assertFalse(mod.prime_length(''))

    def test_edge_single_character_string(self):
            # Length is 1. 1 is not a prime number.
            self.assertFalse(mod.prime_length('a'))

    def test_edge_smallest_prime_length_2(self):
            # Length is 2. 2 is the smallest prime number.
            self.assertTrue(mod.prime_length('ab'))

    def test_edge_large_prime_length_13(self):
            # Length is 13, which is a prime number.
            self.assertTrue(mod.prime_length('abcdefghijklm'))

    def test_edge_large_not_prime_length_14(self):
            # Length is 14, which is not a prime number.
            self.assertFalse(mod.prime_length('abcdefghijklmn'))

    def test_edge_special_chars_not_prime_length_4(self):
            # Length is 4, which is not a prime number. Content of string does not affect primality of length.
            self.assertFalse(mod.prime_length('!@#$'))

    def test_error_integer_input(self):
            # Input is an integer, not a string.
            with self.assertRaises(TypeError):
                mod.prime_length(123)

    def test_error_none_input(self):
            # Input is None, not a string.
            with self.assertRaises(TypeError):
                mod.prime_length(None)

