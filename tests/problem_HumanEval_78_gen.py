import unittest
from sut.problem_HumanEval_78 import hex_key

class TestHexKey(unittest.TestCase):

    def test_empty_string(self):
        # Edge Case: Empty input string
        # Expected: 0 prime digits
        self.assertEqual(hex_key(""), 0)

    def test_single_prime_digit(self):
        # Edge Case: Single character input, which is a prime hex digit
        # Expected: 1 prime digit
        self.assertEqual(hex_key("2"), 1)

    def test_single_non_prime_digit(self):
        # Edge Case: Single character input, which is a non-prime hex digit
        # Expected: 0 prime digits
        self.assertEqual(hex_key("A"), 0)

    def test_mixed_digits_one_prime(self):
        # Typical Input / Logic Mutation: String with one prime and one non-prime
        # Example from docstring: "AB" (B is prime, A is not)
        # Expected: 1 prime digit
        self.assertEqual(hex_key("AB"), 1)

    def test_mixed_digits_multiple_same_primes(self):
        # Typical Input / Logic Mutation: String with multiple occurrences of the same prime digit
        # Example from docstring: "1077E" (two 7s are prime)
        # Expected: 2 prime digits
        self.assertEqual(hex_key("1077E"), 2)

    def test_all_prime_digits(self):
        # Boundary Test: String containing all possible prime hex digits
        # Primes: 2, 3, 5, 7, B, D
        # Expected: 6 prime digits
        self.assertEqual(hex_key("2357BD"), 6)

    def test_all_non_prime_digits(self):
        # Boundary Test: String containing all possible non-prime hex digits
        # Non-primes: 0, 1, 4, 6, 8, 9, A, C, E, F
        # Expected: 0 prime digits
        self.assertEqual(hex_key("014689ACEF"), 0)

    def test_long_mixed_string_from_example(self):
        # Extreme Input / Typical: Long string with a mix of prime and non-prime digits
        # Example from docstring: "123456789ABCDEF0"
        # Primes: 2, 3, 5, 7, B, D -> 6 primes
        # Expected: 6 prime digits
        self.assertEqual(hex_key("123456789ABCDEF0"), 6)

    def test_long_string_with_one_isolated_prime(self):
        # Extreme Input / Logic Mutation: Long string where only one digit is prime, surrounded by non-primes
        # Expected: 1 prime digit
        self.assertEqual(hex_key("FFFFF3FFFFF"), 1)

    def test_long_string_all_same_non_prime(self):
        # Extreme Input / Edge Case: Long string consisting of only one repeated non-prime digit
        # Expected: 0 prime digits
        self.assertEqual(hex_key("EEEEEEEEEEEEEEEEEEEE"), 0)