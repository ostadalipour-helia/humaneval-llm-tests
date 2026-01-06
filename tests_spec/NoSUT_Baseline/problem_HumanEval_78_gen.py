import unittest
import sut.problem_HumanEval_78 as mod

class TestHybrid(unittest.TestCase):
    def test_empty_string(self):
            # Edge Case: Empty input string
            # Expected: 0 prime digits
            self.assertEqual(mod.hex_key(""), 0)

    def test_single_prime_digit(self):
            # Edge Case: Single character input, which is a prime hex digit
            # Expected: 1 prime digit
            self.assertEqual(mod.hex_key("2"), 1)

    def test_single_non_prime_digit(self):
            # Edge Case: Single character input, which is a non-prime hex digit
            # Expected: 0 prime digits
            self.assertEqual(mod.hex_key("A"), 0)

    def test_mixed_digits_one_prime(self):
            # Typical Input / Logic Mutation: String with one prime and one non-prime
            # Example from docstring: "AB" (B is prime, A is not)
            # Expected: 1 prime digit
            self.assertEqual(mod.hex_key("AB"), 1)

    def test_mixed_digits_multiple_same_primes(self):
            # Typical Input / Logic Mutation: String with multiple occurrences of the same prime digit
            # Example from docstring: "1077E" (two 7s are prime)
            # Expected: 2 prime digits
            self.assertEqual(mod.hex_key("1077E"), 2)

    def test_all_prime_digits(self):
            # Boundary Test: String containing all possible prime hex digits
            # Primes: 2, 3, 5, 7, B, D
            # Expected: 6 prime digits
            self.assertEqual(mod.hex_key("2357BD"), 6)

    def test_all_non_prime_digits(self):
            # Boundary Test: String containing all possible non-prime hex digits
            # Non-primes: 0, 1, 4, 6, 8, 9, A, C, E, F
            # Expected: 0 prime digits
            self.assertEqual(mod.hex_key("014689ACEF"), 0)

    def test_long_mixed_string_from_example(self):
            # Extreme Input / Typical: Long string with a mix of prime and non-prime digits
            # Example from docstring: "123456789ABCDEF0"
            # Primes: 2, 3, 5, 7, B, D -> 6 primes
            # Expected: 6 prime digits
            self.assertEqual(mod.hex_key("123456789ABCDEF0"), 6)

    def test_long_string_with_one_isolated_prime(self):
            # Extreme Input / Logic Mutation: Long string where only one digit is prime, surrounded by non-primes
            # Expected: 1 prime digit
            self.assertEqual(mod.hex_key("FFFFF3FFFFF"), 1)

    def test_long_string_all_same_non_prime(self):
            # Extreme Input / Edge Case: Long string consisting of only one repeated non-prime digit
            # Expected: 0 prime digits
            self.assertEqual(mod.hex_key("EEEEEEEEEEEEEEEEEEEE"), 0)

    def test_normal_one_prime(self):
            # Description: Contains one prime hex digit 'B'.
            self.assertEqual(mod.hex_key("AB"), 1)

    def test_normal_multiple_primes_repeated(self):
            # Description: Contains two prime hex digits '7' and '7'.
            self.assertEqual(mod.hex_key("1077E"), 2)

    def test_normal_mixed_primes_and_non_primes(self):
            # Description: Contains four prime hex digits 'B', 'D', '3', '3'.
            self.assertEqual(mod.hex_key("ABED1A33"), 4)

    def test_normal_all_prime_digits_present(self):
            # Description: Contains six prime hex digits '2', '3', '5', '7', 'B', 'D'.
            self.assertEqual(mod.hex_key("123456789ABCDEF0"), 6)

    def test_edge_empty_string(self):
            # Description: Empty input string should result in zero prime digits.
            self.assertEqual(mod.hex_key(""), 0)

    def test_edge_no_prime_digits(self):
            # Description: String containing no prime hexadecimal digits.
            self.assertEqual(mod.hex_key("01468ACEF"), 0)

    def test_edge_only_prime_digits(self):
            # Description: String containing only prime hexadecimal digits.
            self.assertEqual(mod.hex_key("2357BD"), 6)

    def test_edge_single_prime_digit(self):
            # Description: Single prime hexadecimal digit.
            self.assertEqual(mod.hex_key("2"), 1)

    def test_edge_single_non_prime_digit(self):
            # Description: Single non-prime hexadecimal digit.
            self.assertEqual(mod.hex_key("0"), 0)

    def test_error_non_string_input_int(self):
            # Description: Input `num` is not a string (integer).
            with self.assertRaises(TypeError):
                mod.hex_key(123)

    def test_error_non_string_input_null(self):
            # Description: Input `num` is null.
            with self.assertRaises(TypeError):
                mod.hex_key(None)

    def test_normal_repeated_prime_two(self):
            # Description: Contains two prime hex digits '2', '2'.
            self.assertEqual(mod.hex_key("2020"), 2)

