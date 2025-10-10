import unittest
from sut.problem_HumanEval_82 import prime_length

class TestPrimeLength(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(prime_length(''), False)

    def test_single_char_string(self):
        self.assertEqual(prime_length('a'), False)

    def test_length_two_prime(self):
        self.assertEqual(prime_length('ab'), True)

    def test_length_three_prime(self):
        self.assertEqual(prime_length('abc'), True)

    def test_length_four_composite(self):
        self.assertEqual(prime_length('abcd'), False)

    def test_example_hello(self):
        self.assertEqual(prime_length('Hello'), True)

    def test_example_orange(self):
        self.assertEqual(prime_length('orange'), False)

    def test_example_kittens(self):
        self.assertEqual(prime_length('kittens'), True)

    def test_length_nine_composite(self):
        self.assertEqual(prime_length('abcdefghi'), False)

    def test_length_eleven_prime(self):
        self.assertEqual(prime_length('abcdefghijk'), True)