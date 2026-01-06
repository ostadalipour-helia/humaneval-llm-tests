import unittest
from sut.problem_HumanEval_78 import hex_key

class Test_hex_key(unittest.TestCase):
    def test_normal_one_prime(self):
        # Description: Contains one prime hex digit 'B'.
        self.assertEqual(hex_key("AB"), 1)

    def test_normal_multiple_primes_repeated(self):
        # Description: Contains two prime hex digits '7' and '7'.
        self.assertEqual(hex_key("1077E"), 2)

    def test_normal_mixed_primes_and_non_primes(self):
        # Description: Contains four prime hex digits 'B', 'D', '3', '3'.
        self.assertEqual(hex_key("ABED1A33"), 4)

    def test_normal_all_prime_digits_present(self):
        # Description: Contains six prime hex digits '2', '3', '5', '7', 'B', 'D'.
        self.assertEqual(hex_key("123456789ABCDEF0"), 6)

    def test_edge_empty_string(self):
        # Description: Empty input string should result in zero prime digits.
        self.assertEqual(hex_key(""), 0)

    def test_edge_no_prime_digits(self):
        # Description: String containing no prime hexadecimal digits.
        self.assertEqual(hex_key("01468ACEF"), 0)

    def test_edge_only_prime_digits(self):
        # Description: String containing only prime hexadecimal digits.
        self.assertEqual(hex_key("2357BD"), 6)

    def test_edge_single_prime_digit(self):
        # Description: Single prime hexadecimal digit.
        self.assertEqual(hex_key("2"), 1)

    def test_edge_single_non_prime_digit(self):
        # Description: Single non-prime hexadecimal digit.
        self.assertEqual(hex_key("0"), 0)

    def test_error_non_string_input_int(self):
        # Description: Input `num` is not a string (integer).
        with self.assertRaises(TypeError):
            hex_key(123)

    def test_error_non_string_input_null(self):
        # Description: Input `num` is null.
        with self.assertRaises(TypeError):
            hex_key(None)

    def test_normal_repeated_prime_two(self):
        # Description: Contains two prime hex digits '2', '2'.
        self.assertEqual(hex_key("2020"), 2)