import unittest
from sut.problem_HumanEval_82 import prime_length

class TestPrimeLength(unittest.TestCase):

    def test_example_hello(self):
        self.assertEqual(prime_length('Hello'), True)

    def test_example_abcdcba(self):
        self.assertEqual(prime_length('abcdcba'), True)

    def test_example_kittens(self):
        self.assertEqual(prime_length('kittens'), True)

    def test_example_orange(self):
        self.assertEqual(prime_length('orange'), False)

    def test_empty_string(self):
        self.assertEqual(prime_length(''), False)

    def test_single_character_string(self):
        self.assertEqual(prime_length('a'), False)

    def test_length_two_prime(self):
        self.assertEqual(prime_length('hi'), True)

    def test_length_four_not_prime(self):
        self.assertEqual(prime_length('test'), False)

    def test_length_nine_not_prime(self):
        self.assertEqual(prime_length('ninechars'), False)

    def test_length_eleven_prime(self):
        self.assertEqual(prime_length('elevenchars'), True)

if __name__ == '__main__':
    unittest.main()