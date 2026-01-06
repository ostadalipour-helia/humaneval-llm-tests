import unittest
import sut.problem_HumanEval_49 as mod

class TestHybrid(unittest.TestCase):
    def test_n_is_zero(self):
            # Boundary/Edge case: n=0. 2^0 = 1. 1 % p should be 1 (unless p=1).
            # Catches mutations like returning 0 for n=0.
            self.assertEqual(mod.modp(0, 7), 1)

    def test_p_is_one(self):
            # Boundary/Edge case: p=1. Any x % 1 is 0.
            # Catches mutations where modulo by 1 is not handled correctly.
            self.assertEqual(mod.modp(10, 1), 0)

    def test_p_is_two(self):
            # Boundary/Edge case: p=2. 2^n % 2 is 0 for n > 0, 1 for n=0.
            # Catches off-by-one for n=1 vs n=0, and general modulo by 2 logic.
            self.assertEqual(mod.modp(1, 2), 0)

    def test_two_power_n_less_than_p(self):
            # Typical case: 2^n < p. Result should be 2^n.
            # Catches mutations that incorrectly apply modulo when not needed.
            self.assertEqual(mod.modp(2, 7), 4) # 2^2 = 4, 4 % 7 = 4

    def test_two_power_n_greater_than_p_small_n(self):
            # Typical case: 2^n > p, small n.
            # Tests basic modular arithmetic. Off-by-one for n=4 vs n=3 (docstring example).
            self.assertEqual(mod.modp(4, 5), 1) # 2^4 = 16, 16 % 5 = 1

    def test_two_power_n_is_multiple_of_p(self):
            # Extreme/Unusual case: 2^n is an exact multiple of p. Result should be 0.
            # This implies p must be a power of 2.
            self.assertEqual(mod.modp(5, 32), 0) # 2^5 = 32, 32 % 32 = 0

    def test_fermat_little_theorem_case(self):
            # Extreme/Unusual case: n = p-1 for prime p. 2^(p-1) % p = 1.
            # Tests large n, large prime p, and verifies a specific mathematical property.
            # Catches issues with modular exponentiation for large n.
            self.assertEqual(mod.modp(100, 101), 1) # From docstring, good for logic mutation (n=p-1)

    def test_n_equals_p_for_prime_p(self):
            # Off-by-one error: n = p for prime p.
            # Following test_fermat_little_theorem_case, tests n=p vs n=p-1.
            self.assertEqual(mod.modp(101, 101), 2) # 2^101 % 101 = (2^100 * 2^1) % 101 = (1 * 2) % 101 = 2

    def test_large_n_composite_p(self):
            # Extreme/Unusual case: Large n, composite p.
            # Verifies modular exponentiation works for non-prime moduli.
            self.assertEqual(mod.modp(10, 9), 7) # 2^10 = 1024, 1024 % 9 = 7

    def test_medium_n_medium_p_result_p_minus_one(self):
            # Typical case: n and p are moderate, result is p-1.
            # Tests a specific return value path (max possible non-zero remainder).
            self.assertEqual(mod.modp(6, 13), 12) # 2^6 = 64, 64 % 13 = 12 (which is 13-1)

    def test_normal_case_2_pow_3_mod_5(self):
            # 2^3 mod 5 = 8 mod 5 = 3
            self.assertEqual(mod.modp(3, 5), 3)

    def test_normal_case_large_exponent(self):
            # 2^1101 mod 101 = 2 (large exponent)
            self.assertEqual(mod.modp(1101, 101), 2)

    def test_normal_case_2_pow_3_mod_11(self):
            # 2^3 mod 11 = 8 mod 11 = 8
            self.assertEqual(mod.modp(3, 11), 8)

    def test_edge_case_exponent_is_zero(self):
            # Exponent is zero: 2^0 mod 101 = 1 mod 101 = 1
            self.assertEqual(mod.modp(0, 101), 1)

    def test_edge_case_fermat_little_theorem(self):
            # Fermat's Little Theorem case: 2^(p-1) mod p = 1 for prime p (101 is prime)
            self.assertEqual(mod.modp(100, 101), 1)

    def test_edge_case_modulo_by_2(self):
            # Modulo by 2: 2^5 mod 2 = 32 mod 2 = 0
            self.assertEqual(mod.modp(5, 2), 0)

    def test_edge_case_2_pow_n_less_than_p(self):
            # 2^n < p
            self.assertEqual(mod.modp(2, 5), 4)

    def test_error_p_is_zero(self):
            # p must be greater than 1. Modulo by zero is undefined.
            with self.assertRaises(ZeroDivisionError):
                mod.modp(3, 0)

    def test_error_n_is_not_integer(self):
            # n must be an integer.
            with self.assertRaises(TypeError):
                mod.modp("abc", 5)

    def test_error_p_is_not_integer(self):
            # p must be an integer.
            with self.assertRaises(TypeError):
                mod.modp(3, "xyz")

