import unittest
import sut.problem_HumanEval_24 as mod

class TestHybrid(unittest.TestCase):
    def test_example_from_docstring(self):
            """
            Test case from the function's docstring.
            Verifies a typical composite number.
            """
            self.assertEqual(mod.largest_divisor(15), 5)

    def test_smallest_prime(self):
            """
            Boundary test: The smallest prime number (2).
            Should return 1, as it's the only divisor smaller than 2.
            Catches off-by-one errors if 1 is excluded from divisor checks.
            """
            self.assertEqual(mod.largest_divisor(2), 1)

    def test_another_small_prime(self):
            """
            Edge case: Another small prime number (3).
            Verifies behavior for prime numbers, which should always return 1.
            """
            self.assertEqual(mod.largest_divisor(3), 1)

    def test_smallest_composite(self):
            """
            Boundary test: The smallest composite number (4).
            Should return 2. Catches logic mutations where '<' might become '<='
            and return n itself, or if the divisor finding logic is flawed.
            """
            self.assertEqual(mod.largest_divisor(4), 2)

    def test_medium_composite(self):
            """
            Typical input: A composite number with multiple divisors (12).
            Ensures the largest proper divisor is correctly identified.
            """
            self.assertEqual(mod.largest_divisor(12), 6)

    def test_perfect_square(self):
            """
            Extreme/Unusual input: A perfect square (9).
            Tests scenarios where the square root of n is a divisor.
            """
            self.assertEqual(mod.largest_divisor(9), 3)

    def test_large_prime(self):
            """
            Extreme/Unusual input: A larger prime number (97).
            Confirms consistent behavior for prime numbers, returning 1.
            """
            self.assertEqual(mod.largest_divisor(97), 1)

    def test_large_composite_power_of_two(self):
            """
            Extreme/Unusual input: A power of two (64).
            For powers of two, the largest divisor is always n/2.
            """
            self.assertEqual(mod.largest_divisor(64), 32)

    def test_large_composite_odd_factors(self):
            """
            Extreme/Unusual input: A composite number with odd factors (99).
            Ensures correct identification of the largest divisor even with complex factorizations.
            """
            self.assertEqual(mod.largest_divisor(99), 33) # 99 = 3 * 3 * 11, largest divisor < 99 is 33

    def test_another_composite(self):
            """
            Typical input: Another composite number (20).
            Further verifies the function's general correctness for composite numbers.
            """
            self.assertEqual(mod.largest_divisor(20), 10)

    def test_normal_composite_15(self):
            # Normal case: A composite number, finding its largest proper divisor.
            self.assertEqual(mod.largest_divisor(15), 5)

    def test_normal_composite_10(self):
            # Normal case: Another composite number.
            self.assertEqual(mod.largest_divisor(10), 5)

    def test_normal_composite_12(self):
            # Normal case: A composite number with multiple divisors.
            self.assertEqual(mod.largest_divisor(12), 6)

    def test_edge_smallest_prime_2(self):
            # Edge case: The smallest valid input number (prime).
            self.assertEqual(mod.largest_divisor(2), 1)

    def test_edge_prime_7(self):
            # Edge case: A prime number, its only divisor smaller than itself is 1.
            self.assertEqual(mod.largest_divisor(7), 1)

    def test_edge_perfect_square_4(self):
            # Edge case: A perfect square.
            self.assertEqual(mod.largest_divisor(4), 2)

    def test_edge_power_of_2_8(self):
            # Edge case: A power of 2.
            self.assertEqual(mod.largest_divisor(8), 4)

    def test_error_n_is_float(self):
            # Error case: Input 'n' is a float.
            with self.assertRaises(TypeError):
                mod.largest_divisor(15.5)

    def test_error_n_is_string(self):
            # Error case: Input 'n' is a string.
            with self.assertRaises(TypeError):
                mod.largest_divisor('abc')

