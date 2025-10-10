import unittest
from sut.problem_HumanEval_49 import modp

class TestModp(unittest.TestCase):

    def test_n_is_zero(self):
        # Boundary/Edge case: n=0. 2^0 = 1. 1 % p should be 1 (unless p=1).
        # Catches mutations like returning 0 for n=0.
        self.assertEqual(modp(0, 7), 1)

    def test_p_is_one(self):
        # Boundary/Edge case: p=1. Any x % 1 is 0.
        # Catches mutations where modulo by 1 is not handled correctly.
        self.assertEqual(modp(10, 1), 0)

    def test_p_is_two(self):
        # Boundary/Edge case: p=2. 2^n % 2 is 0 for n > 0, 1 for n=0.
        # Catches off-by-one for n=1 vs n=0, and general modulo by 2 logic.
        self.assertEqual(modp(1, 2), 0)

    def test_two_power_n_less_than_p(self):
        # Typical case: 2^n < p. Result should be 2^n.
        # Catches mutations that incorrectly apply modulo when not needed.
        self.assertEqual(modp(2, 7), 4) # 2^2 = 4, 4 % 7 = 4

    def test_two_power_n_greater_than_p_small_n(self):
        # Typical case: 2^n > p, small n.
        # Tests basic modular arithmetic. Off-by-one for n=4 vs n=3 (docstring example).
        self.assertEqual(modp(4, 5), 1) # 2^4 = 16, 16 % 5 = 1

    def test_two_power_n_is_multiple_of_p(self):
        # Extreme/Unusual case: 2^n is an exact multiple of p. Result should be 0.
        # This implies p must be a power of 2.
        self.assertEqual(modp(5, 32), 0) # 2^5 = 32, 32 % 32 = 0

    def test_fermat_little_theorem_case(self):
        # Extreme/Unusual case: n = p-1 for prime p. 2^(p-1) % p = 1.
        # Tests large n, large prime p, and verifies a specific mathematical property.
        # Catches issues with modular exponentiation for large n.
        self.assertEqual(modp(100, 101), 1) # From docstring, good for logic mutation (n=p-1)

    def test_n_equals_p_for_prime_p(self):
        # Off-by-one error: n = p for prime p.
        # Following test_fermat_little_theorem_case, tests n=p vs n=p-1.
        self.assertEqual(modp(101, 101), 2) # 2^101 % 101 = (2^100 * 2^1) % 101 = (1 * 2) % 101 = 2

    def test_large_n_composite_p(self):
        # Extreme/Unusual case: Large n, composite p.
        # Verifies modular exponentiation works for non-prime moduli.
        self.assertEqual(modp(10, 9), 7) # 2^10 = 1024, 1024 % 9 = 7

    def test_medium_n_medium_p_result_p_minus_one(self):
        # Typical case: n and p are moderate, result is p-1.
        # Tests a specific return value path (max possible non-zero remainder).
        self.assertEqual(modp(6, 13), 12) # 2^6 = 64, 64 % 13 = 12 (which is 13-1)